# homework 181204 crash course ex. 8.8

def make_album(artist, album):
    my_album = {"artist":artist, "album":album}
    return my_album

while True:
    artist = input("Enter an artist name > ")
    album = input("Enter an album name > ")
    a_album = makealbum(artist, album)
    print(a_album)

    message = input("continue? (y/n)")
    print(message)
    if message == "n":
        break
    else:
        continue
