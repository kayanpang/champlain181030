# homework 181204 crash course ex. 8.7

def make_album(artist, album, track = 0):
    return "{0}, {1}".format(artist, album)
thisdic = {"artist": "Evanescence", "album": "Fallen", "number": "9"}
thatdic = {"artist": "Okuda Miwako", "album": "Chevalier"}
anotherdic = {"artist": "Shela", "album": "Hikaru no Go"}
for x in thisdic.values():
    print(x)