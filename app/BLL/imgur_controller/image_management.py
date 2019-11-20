from imgurpython import ImgurClient
import configparser
import requests

def authenticate():

    config = configparser.ConfigParser()
    config.read('auth.ini')

    client_id = config.get('credentials', 'client_id')
    client_secret = config.get('credentials', 'client_secret')

    imgur_username = config.get('credentials', 'imgur_username')
    imgur_password = config.get('credentials', 'imgur_password')
    access_token = config.get('credentials', 'access_token')
    refresh_token = config.get('credentials', 'refresh_token')

    client = ImgurClient(client_id, client_secret)
    client.set_user_auth(access_token, refresh_token)
    return client

def refresh_token():
    config = configparser.ConfigParser()
    config.read('auth.ini')

    new_access = {
	"refresh_token": config.get('credentials', 'refresh_token'),
	"client_id": config.get('credentials','client_id'),
	"client_secret": config.get('credentials','client_secret'),
	"grant_type": "refresh_token"
    }
    request = requests.post('https://api.imgur.com/oauth2/token', json=new_access)
    refresh_token, access_token = map(request.get, ('refresh_token','access_token'))

    config.set('credentials', 'refresh_token', refresh_token)
    config.set('credentials', 'access_token', access_token)

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
