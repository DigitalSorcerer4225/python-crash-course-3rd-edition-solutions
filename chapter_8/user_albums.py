# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while  loop that allows users to enter an album’s artist and title. Once you have that  information, call make_album() with the user’s input and print the dictionary  that’s created. Be sure to include a quit value in the while loop. 

def make_album(artist_name, album_title, songs=None):
    album = {'artist': artist_name, 'album': album_title}
    if songs:
        album['song'] = songs
    return album

while True:
    print('Enter "q" to quit anytime.')
    
    artist_name = input("Name of the artist: ")
    if artist_name == 'q':
        break
    
    album_title = input("Title of the album: ")
    if album_title == 'q':
        break

    album = make_album(artist_name, album_title)
    print(album)
    


