# Youtube Downloader:
This project is designed on youtube downloader in different formates and qualities.
It uses the `yt-dlp` library to download videos and audio from YouTube.Everything is done in a simple way and every sort of error is handled in a user-friendly manner.Here is one thing to note that this project is not a GUI based project, it is a terminal based project becauuse it is a simple project and it is made just for learning purpose. Everyone can use this project to download videos and audios just by running the code and entering the URL of the video and audio you want to download.

# How to use:
1. Make sure you have Python installed on your system because this project need a Python environment to run. You can use the online complier but there will be issue of liberaries but the recommended one is to install the Python or use the replit which is an online compiler.
2. Install the required liberaries by running the following command:
  ```
  pip install yt_dlp
  ``` 
but keep in mind that you need to install the 'ffmpeg' before using the programm in your terminal or command by pip:
    ```
    pip install ffmpeg
    ```
3. After installing the required libraries, you can run the code by using the following command:
    ```
    python main.py
    ```
4. When you run the code, a menu will appear on the terminal. You can choose the option you want to use according to your need.The options are:
- If you wanna just to download the video then you can choose the first option.
- If you want to download the full palylist of the course/anything then you can choose the second option.
- If you want to download the video in a specific format then you can choose the third option but you need to enter the first video number to start and the the last video number to end.
- if you want to download the audio of the video then you can choose the fourth option.
- If you want to exit the program then you can choose the fifth option.
5. Enter the URL of the video or audio /playlist you want to download when prompted and the program will download the video/audio/ playlist. When the download is complete, a message will be displayed for successful download.
# Note:
- Make sure you have a stable internet connection while downloading the video/audio/playlist.
- The downloaded files will be saved in the same directory where the script is located.
# Bonus Feature:
- The program will handle errors gracefully and provide appropriate messages if something goes wrong during the download process.
- One thing is very shocking and mind blowing that the the video will not take too long like a normal downloader because it uses amazing library called 'yt_dlp which downloads the things of hours few in seconds and minutes.

# License:
This project is open source and available on the github. You can fork it and use it according to your needs and requirements. Feel free to modify the code and add new features to it. If you find any issues or bugs, please report them on the github issues page.