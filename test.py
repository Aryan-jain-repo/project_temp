import streamlit as st
from googleapiclient.discovery import build

# YouTube API key (replace 'YOUR_API_KEY' with your actual API key)
API_KEY = 'AIzaSyDbkN_1mjfjG4wst54kDUQWKu74554TKXY'

# Function to search for movie trailer on YouTube
def get_trailer(movie_name):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Search for movie trailer on YouTube
    search_response = youtube.search().list(
        q=movie_name + ' trailer',
        part='id,snippet',
        maxResults=1
    ).execute()

    # Extract trailer video ID
    trailer_video_id = search_response['items'][0]['id']['videoId']

    # Generate trailer video URL
    trailer_url = f'https://www.youtube.com/watch?v={trailer_video_id}'

    return trailer_url

# Function to play movie trailer on Streamlit
def play_trailer(movie_name):
    st.title('Movie Trailer Player')
    
    try:
        # Retrieve trailer URL
        trailer_url = get_trailer(movie_name)
        st.write(f"Trailer found for '{movie_name}'. Watch it below:")
        st.video(trailer_url)
    except Exception as e:
        st.error(f'Error: {e}')
