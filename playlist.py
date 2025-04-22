#!/usr/bin/python3


from bs4 import BeautifulSoup
import sys


ALBUM_PATH ="data-music/album/"
ARTIST_PATH = "data-music/artists/"
SONG_PATH = "data-music/songs/"
GENERE_PATH = "data-music/genere/"


version = 0.5
app_title = "Playlist v" + str(version)

print(app_title)
print("-" * len(app_title))

def main_menu():
    while True:
        print("\n--- Main menu ---")
        print("1. Albums")
        print("2. Songs")
        print("3. Artists")
        print("4. Genres")
        print("0. Exit")

        option = input("Select an option: ")
        
        if option.isdigit():
            option = int(option)
            if 0 <= option <= 4:
                return option
            else:
                print("Option selected is invalid, try again.")
        else:
            print("Please enter a valid number.")


def album_menu():
    while True:
        print("\n--- Albums menu ---")
        print("1. Show all albums")
        print("2. Search album")
        print("0. Back")

        option = input("Select an option: ")
        if option.isdigit():
            option = int(option)
            if 0 <= option <= 2:
                return option
            else:
                print("Option selected is invalid, try again.")
        else:
            print("Please enter a valid number.")


def song_menu():
    while True:
        print("\n--- Songs menu ---")
        print("1. Show all songs")
        print("2. Search song")
        print("0. Back")

        option = input("Select an option: ")
        
        if option.isdigit():
            option = int(option)
            if 0 <= option <= 2:
                return option
            else:
                print("Option selected is invalid, try again.")
        else:
            print("Please enter a valid number.")


def artist_menu():
    while True:
        print("\n--- Artists menu ---")
        print("1. Show all artists")
        print("2. Search artist")
        print("0. Back")

        option = input("Select an option: ")
        
        if option.isdigit():
            option = int(option)
            if 0 <= option <= 2:
                return option
            else:
                print("Option selected is invalid, try again.")
        else:
            print("Please enter a valid number.")

def genre_menu():
    while True:
        print("\n--- Genres menu ---")
        print("1. Show all genres")
        print("2. Search genre")
        print("0. Back")

        option = input("Select an option: ")
        
        if option.isdigit():
            option = int(option)
            if 0 <= option <= 2:
                return option
            else:
                print("Option selected is invalid, try again.")
        else:
            print("Please enter a valid number.")


            

def open_xml(file_path):
    album_xml = open(file_path, "r").read()
    return BeautifulSoup(album_xml, 'xml')


def load_album (album_num):
    global ALBUM_PATH
    file_name = "album" + str(album_num) + ".xml"
    file_path = ALBUM_PATH + file_name
    album_xml = open_xml(file_path)
    
    album = {
        "id":1,
        "title":"Title",
        "cover":"IMAGE",
        "artists": [
            {
                "id":1,
                "title":"...."
           

            },
            {
                "id":2,
                "title":"...."
           

            },
        ],
        "songs": [
            {
                "id":1,
                "title":"...."
            },
            {
                "id":2,
                "title":"...."
        
            },  
            ]
         
        }
    return album_xml


print (load_album(2))
sys.exit()

main_menu()
