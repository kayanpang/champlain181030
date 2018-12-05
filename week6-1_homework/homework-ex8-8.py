# homework 181204 crash course ex. 8.8 while loop

def make_album(artist, album):
    return "{0}, {1}".format(artist, album)

artist = input("Enter an artist name > ")
while artist != 'quit':
    album = input("Enter an album name > ")
    print("{}".format(artist) + ", " + "{}".format(album))

make_album()