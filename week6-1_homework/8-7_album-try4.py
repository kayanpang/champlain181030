# homework 181204 crash course ex. 8.7

def make_album(artist, album, track = 0):
    my_album = {"artist":artist, "album":album, "track":track}
    return my_album

a_album = make_album("Shela", "Hikaru no Go", 12)
b_album = make_album("Okuda Miwako", "Chevalier", 10)
c_album = make_album("7!! Seven Oops", "Shigetsu wa Kimi no Uso", 1)

print(a_album)
print(b_album)
print(c_album)