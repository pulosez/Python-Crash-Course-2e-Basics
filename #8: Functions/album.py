# 8.7-8.
def make_album(artist, title, tracks=None):
    album = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album['tracks'] = tracks
    return album

# print(make_album('nirvana', 'nevermind', tracks=12))
# print(make_album('the beatles', 'please please me'))
# print(make_album('queen', 'innuendo'))

while True:
    print("\nLet's make album:")
    print("(enter 'q' at any time to quit)")

    n_artist = input("Artist: ")
    if n_artist == 'q':
        break

    n_title = input("Title: ")
    if n_title == 'q':
        break

    album = make_album(n_artist, n_title)
    print(album)

print("Thank you!")
