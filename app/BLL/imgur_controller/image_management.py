import os
import base64
from imgurpython import ImgurClient
import requests
import json

def authenticate():

    config = json.loads(os.environ.get("imgur_credentials").replace("'", "\""))
    print("Auth: ", config)

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
    config = json.loads(os.environ.get("imgur_credentials").replace("'", "\""))
    print("Refresh: ", config)

    new_access = {
	"refresh_token": config.get('refresh_token', None),
	"client_id": config.get('client_id', None),
	"client_secret": config.get('client_secret', None),
	"grant_type": "refresh_token"
    }
    request = requests.post('https://api.imgur.com/oauth2/token', json=new_access)
    refresh_token, access_token = map(json.loads(request.text).get, ('refresh_token','access_token'))

    config['refresh_token'] = refresh_token
    config['access_token'] = access_token

def upload_image(bin_image):
    client = authenticate()
    album = None # quando houver gerenciamento do album, receber o id 
    image_path = base64_to_path(bin_image)
    config = {
		'album': album
	}
    try:
        image = client.upload_from_path(image_path, config=config, anon=False)
    except Exception:
        refresh_token()
        print("Faltou refresh")
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

def base64_to_path(img_b64):
    imgdata = base64.b64decode(img_b64)
    filename = 'some_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)

    return filename
