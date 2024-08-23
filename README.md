***Billboard Hot 100 to Spotify Playlist Creator -  Musical Time Machine***

**Overview**

This Python project scrapes the Billboard Hot 100 chart for a specified date and creates a Spotify playlist with the top 100 songs from that time period. The project leverages web scraping with BeautifulSoup, API interaction with Spotify using the Spotipy library, and user input for date selection.

**Features**

Scrapes Billboard Hot 100: Retrieves the list of top 100 songs for a given date from the Billboard Hot 100 chart.
Spotify Playlist Integration: Authenticates with Spotify and creates a private playlist with the retrieved songs.
Error Handling: Handles cases where some songs might not be found on Spotify.

**Requirements**

1. Python 3.x
2. requests
3. beautifulsoup4
4. spotipy

**Installation**

1. Clone the repository:   
```bash
git clone https://github.com/dhingra30/billboard-to-spotify.git
```

2. Navigate to the project directory:
```bash
cd billboard-to-spotify
```

3. Install the required packages:
```bash
pip install requests beautifulsoup4 spotipy
```

**Usage**

Update the SpotifyPlaylist class with your Spotify API credentials (client ID and client secret).

**Run the script:**

```bash
python script.py
```

>Enter the desired date in the format year month day when prompted. For example:
```bash
Enter the year, month and date separated with spaces: 2023 08 01
``` 

>The script will:
1. Scrape the Billboard Hot 100 for the provided date.
2. Search for each song on Spotify.
3. Create a private playlist on Spotify with the found songs.

**Contributing**

Feel free to submit issues, fork the repository, and make pull requests. Contributions to improve the functionality or fix bugs are welcome!
