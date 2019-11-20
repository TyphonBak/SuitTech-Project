import os
from imgurpython import ImgurClient
import requests

def authenticate():

    config = os.environ.get('imgur_credentials')

    client_id = config.get('client_id', None)
    client_secret = config.get('client_secret', None)

    imgur_username = config.get('imgur_username', None)
    imgur_password = config.get('imgur_password', None)
    access_token = config.get('access_token', None)
    refresh_token = config.get('refresh_token', None)

    client = ImgurClient(client_id, client_secret)
    client.set_user_auth(access_token, refresh_token)
    return client

def refresh_token():
    config = os.environ.get('imgur_credentials')

    new_access = {
	"refresh_token": config.get('refresh_token', None),
	"client_id": config.get('client_id', None),
	"client_secret": config.get('client_secret', None),
	"grant_type": "refresh_token"
    }
    request = requests.post('https://api.imgur.com/oauth2/token', json=new_access)
    refresh_token, access_token = map(request.get, ('refresh_token','access_token'))

    config['refresh_token'] = refresh_token
    config['access_token'] = access_token

def upload_image(bin_image):
    client = authenticate()
    album = None # quando houver gerenciamento do album, receber o id 
    image_path = bin_image
    config = {
		'album': album
	}
    #substituir o image_path para o numero binario
    try:
        image = client.upload_from_path(image_path, config=config, anon=False)
    except Exception:
        refresh_token()
        client = authenticate()
        image = client.upload_from_path(image_path, config=config, anon=False)

    id, link, deletehash = map(image.get, ('id','link','deletehash'))
    return {"imgur_id": id, "url": link, "delete_hash": deletehash}

def delete_image(image_id):
    client = authenticate()
    try:
        delete_image = client.delete_image(image_id)
        return True
    except Exception:
        return False
