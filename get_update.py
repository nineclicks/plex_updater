import requests
import json

def update_check(config):
    url = f"{config['host']}/updater/check?download=1"

    payload={}
    headers = {
      'X-Plex-Token': config['token'],
      'Accept': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    return response.status_code

def update_status(config):
    url = f"{config['host']}/updater/status"

    payload={}
    headers = {
      'X-Plex-Token': config['token'],
      'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json().get('MediaContainer', {}).get('downloadURL')

def download_update(url):
    filename = 'plex_update.deb'
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)

def plex_users(config):
    url = f"{config['host']}/status/sessions"

    payload={}
    headers = {
      'X-Plex-Token': config['token'],
      'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    num_users = response.json()['MediaContainer']['size']
    return num_users

with open('config.json', 'r') as fp:
    config = json.load(fp)

num_users = plex_users(config)
print('Number of plex users online:', num_users)
if num_users > 0:
    print('Plex is currently in use')
    exit(1)

update_check(config)
update_url = update_status(config)
if update_url is not None:
    print('update found')
    download_update(update_url)
else:
    print('no update found')
    exit(1)
