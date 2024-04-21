# streamlit_music_player.py

import streamlit as st
import os

def play_audio(file_path):
    audio_bytes = open(file_path, "rb").read()
    st.audio(audio_bytes, format="audio/mp3")

def main():
    st.title("MP3 Music Player")

    # List of MP3 files (you can customize this)
    mp3_files = ['Humare_Saath_Shri_Raghunath.mp3',
                 'Har_Har_Shambhu.mp3',
                 'Bajao_Dhol_Swagat_Me.mp3',
                 'Achutam_keshavam.mp3',
                 'yam_yam_yaksharupam_mahakal bhairav strotam.mp3',
                 'shiv_tandav_strot.mp3',
                 'my_queen.mp3',
                 'Meri_Jhopdi_Ke_Bhag_Aaj_Khul_Jayenge.mp3',
                 'matak_chalungi.mp3',
                 'kale_kagaz.mp3']

    selected_song = st.selectbox("Select a song", mp3_files)

    if st.button("Play"):
        song_path = selected_song
        play_audio(song_path)

if __name__ == "__main__":
    main()
