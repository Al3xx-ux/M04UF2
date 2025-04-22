#!/usr/bin/python3


from bs4 import BeautifulSoup



albums_path ="album/"
artists_path = "artist/"
songs_path = "song/"
genres_path = "genre/"


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

mainmenu = main_menu()
print("Option selected:", mainmenu)

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

albummenu = album_menu()
print("Option selected:", albummenu)

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

songs_menu = song_menu()
print("Option selected:", songs_menu)

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

artistmenu = artist_menu()
print("Option selected:", artistmenu)
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


            
genremenu = genre_menu()
print("Option selected:", genremenu)


def load_menu (album_num):
    file_name = "album" + str(album_num) + ".xml"
