Billboard Hot 100 to Spotify Playlist Creator -  Musical Time Machine
Overview
This Python project scrapes the Billboard Hot 100 chart for a specified date and creates a Spotify playlist with the top 100 songs from that time period. The project leverages web scraping with BeautifulSoup, API interaction with Spotify using the Spotipy library, and user input for date selection.

Features
Scrapes Billboard Hot 100: Retrieves the list of top 100 songs for a given date from the Billboard Hot 100 chart.
Spotify Playlist Integration: Authenticates with Spotify and creates a private playlist with the retrieved songs.
Error Handling: Handles cases where some songs might not be found on Spotify.
Requirements
Python 3.x
requests
beautifulsoup4
spotipy
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/dhingra30/billboard-to-spotify.git
Navigate to the project directory:

bash
Copy code
cd billboard-to-spotify
Install the required packages:

bash
Copy code
pip install requests beautifulsoup4 spotipy
Usage
Update the SpotifyPlaylist class with your Spotify API credentials (client ID and client secret).

Run the script:

bash
Copy code
python script.py
Enter the desired date in the format year month day when prompted. For example:

sql
Copy code
Enter the year, month and date separated with spaces: 2023 08 01
The script will:

Scrape the Billboard Hot 100 for the provided date.
Search for each song on Spotify.
Create a private playlist on Spotify with the found songs.
Contributing
Feel free to submit issues, fork the repository, and make pull requests. Contributions to improve the functionality or fix bugs are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.

