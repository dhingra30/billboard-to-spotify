from spotify_playlist import SpotifyPlaylist
from songs import SongList

print("Welcome to songs time machine to create the playlist please provide the date to get top 100 songs from that "
      "period")
# Request the date from user as year,month and day
year, month, date = input("Enter the year, month and date separated with spaces: ").split()
# Converting the date into YYYY-MM-DD
if len(date) < 2:
    date_range = f"{year}-{month}-0{date}"
else:
    date_range = f"{year}-{month}-{date}"
# Creating a list of songs using the SongList class from songs.py
songs = SongList(date=date_range)
list_of_songs = songs.list_of_songs()
# Creating a spotify playlist by using the SpotifyPlaylist class sending the list of songs and the year
pl = SpotifyPlaylist(list_of_songs=list_of_songs, year=year)

