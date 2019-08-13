import urllib2
url = "http://google.com"
respuesta = urllib2.urlopen(url)
contenido = respuesta.read()
print(contenido[0:300])