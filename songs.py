# Importing required libraries
import requests
from bs4 import BeautifulSoup

# URL of the website
URL = "https://www.billboard.com/charts/hot-100"


class SongList:
    """Scrapes the billboard website for the top 100 songs of a particular time frame"""
    def __init__(self, date):
        self.date = date

    def list_of_songs(self):
        """Uses the html data from the website and returns the list of songs"""
        # Scrapping the website using requests module
        response = requests.get(url=f"{URL}/{self.date}")
        website_data = response.text
        # Using beautiful soup to create readable html data from the web scrapping process
        soup = BeautifulSoup(website_data, "html.parser")
        # Getting all the songs tags
        all_song_tags = soup.select("li h3")
        # Creating a list of song tags
        songs_name = [tags.getText() for tags in all_song_tags][0:100]
        # Creating and returning list of songs
        list_of_songs = [(songs.split("\n\n\t\n\t\n\t\t\n\t\t\t\t\t")[1].split("\t\t\n\t\n"))[0] for songs in
                         songs_name]
        return list_of_songs
