# homework 181204 crash course ex. 8.7

def make_album(artist, album):
    return "{0}, {1}".format(artist, album)
thisdic = {"artist": "Evanescence", "album": "Fallen"}
thatdic = {"artist": "Okuda Miwako", "album": "Chevalier"}
anotherdic = {"artist": "Shela", "album": "Hikaru no Go"}
for x in thisdic.values():
    print(x)