import requests


def trouve(mot,phrase):
	#Return the list of indices of mot found in the phrase
	indices = []
	i = 0
	while(i < len(phrase)):
		if mot in phrase[i:]:
			indices.append(phrase[i:].index(mot) + i)
			i = indices[-1] + 1
		else:
			break
	return indices

def sanatize(liste_indice,result):
	list_url = []
	for i in liste_indice:
		try:
			indice_debut = trouve('["http',result[i-200:i])[-1] + i - 200 + 2
			indice_fin = trouve('"',result[i:i+5])[0] + i
			if result[indice_debut:indice_fin] != '':
				list_url.append(result[indice_debut:indice_fin])
		except:
			None

	return list_url

def get_url_image(query):
	url = "https://www.google.com/search?q="+query+"&tbm=isch"
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accept-Encoding": "gzip, deflate",
		"Connection": "close"
	}
	r = requests.get(url,headers=headers)
	result = r.text
	liste_indices_images = trouve('.jpeg"',result) + trouve('.jpg"',result) +trouve('.png"',result)
	return sanatize(liste_indices_images,result)

print(get_url_image	("test"))