import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyPlaylist:
    def __init__(self, list_of_songs, year):
        self.client_id = "0f6951c8b75b4c3da215c8be09d39ffe"
        self.client_secret = "7eae357f003e48caaa721b3a4f985ed9"
        self.songs = list_of_songs
        self.year = year
        self.manage_playlist()

    def auth_manager(self):
        """Returns the spotipy object authenticating user's spotify account"""
        # Using Spotipy's auth manager to authenticate the spotify account
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri="https://open.spotify.com/",
            scope="playlist-modify-private"
        )
        )
        return sp

    def search_songs(self):
        """Returns the list of found songs uri and count of the songs not found"""
        # Count to keep track of the songs not found
        count = 0
        # Empty list to store the songs uri
        found_songs_uri = []
        # Authenticating the access to spotify
        sp = self.auth_manager()
        # Searching the songs from song URI
        for songs in self.songs:
            try:
                result = sp.search(q=songs, type="track")
                found_songs_uri.append(result['tracks']['items'][0]['uri'])
            # Catching exception for tracks not found
            except IndexError:
                count += 1
        return found_songs_uri, count

    def manage_playlist(self):
        """Creating the playlist and adding found tracks to the playlist"""
        # Authenticating spotify access
        sp = self.auth_manager()
        # Getting user ID
        user_id = sp.current_user()["id"]
        # Creating the playlist
        playlist = (sp.user_playlist_create(user_id, name=f"billboard top 100 - {self.year}", public=False))
        songs_uri, count = self.search_songs()
        # Adding tracks to the playlist
        sp.playlist_add_items(playlist["id"], songs_uri)
        print(f"Playlist created successfully!")
        if count > 0:
            print(f"{count} songs not found ")



