#city name
def city_name(city, country):
    '''返回整洁的名字'''
    location = f"{city}, {country}"
    return location.title()

vacation_location = city_name("santiago", "chile")
print(vacation_location)

#album
def make_album(singer,album_name,song_num=None):
    album_info = {'singer':singer, 'album_name':album_name}
    if song_num:
        album_info['song_num'] = song_num
    return album_info


while True:
    print("\nPlease enter album's information:")
    print("(enter 'q' at any time to quit)")

    singer_name = input ("Singer's name:")
    if singer_name == 'q':
        break

    al_name = input ("Album's name: ")
    if al_name == 'q':
        break

    song_number = input ("The number of song: ")
    if song_number == 'q':
        break

    if song_number:
          album = make_album(singer_name, al_name, int(song_number))
    else:
          album = make_album(singer_name, al_name)

    
    print(album)
