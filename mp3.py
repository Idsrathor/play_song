# streamlit_music_player.py

import streamlit as st
import os

def play_audio(file_path):
    audio_bytes = open(file_path, "rb").read()
    st.audio(audio_bytes, format="audio/mp3")

def main():
    st.title("MP3 Music Player")

    # List of MP3 files (you can customize this)
    mp3_files = [
        "my_queen.mp3",
        "kale_kagaz.mp3",
        "matak_chalungi.mp3",
        # Add more songs here
    ]

    selected_song = st.selectbox("Select a song", mp3_files)

    if st.button("Play"):
        song_path = os.path.join("https://github.com/Idsrathor/play_song/blob/main", selected_song)
        play_audio(song_path)

if __name__ == "__main__":
    main()
