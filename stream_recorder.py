import requests


radios = {
	'cheriefm': {
                 'name': 'CherieFM',
                 'flux': 'http://cdn.nrjaudio.fm/audio1/fr/30201/mp3_128.mp3',
                }
}

stream_url = radios['cheriefm']['flux']
r = requests.get(stream_url, stream=True)

with open(radios['cheriefm']['name'] + '.mp3', 'wb') as f:
    try:
        for block in r.iter_content(1024):
            f.write(block)
    except KeyboardInterrupt:
        pass
