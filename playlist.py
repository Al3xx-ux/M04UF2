#!/usr/bin/python3

from bs4 import BeautifulSoup

version = 0.5
app_title = ("Playlist v"+ str (version))

print (app_title)

print ("-"*len(app_title))

#xml_ejemplo = '<personaje><nombre>Jacinto</nombre><edad valor="33" /></personaje>'
#personaje = BeautifulSoup(xml_ejemplo, 'xml')
#print (personaje.prettify())
#nombre  = (personaje.nombre)
#print(nombre.text)


song_xml_file = open("songs/1.xml", "r")

song_xml = song_xml_file.read()



song = BeautifulSoup(song_xml, 'xml')

print (song.title.text)
print (int(song.duration["seconds"])/60)

for artist in song.artist.find("artist"):
	print (artist.text)
	print (int(artist["id"]), artist.text)



