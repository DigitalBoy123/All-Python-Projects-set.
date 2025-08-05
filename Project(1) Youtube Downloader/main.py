import yt_dlp

print("*"*135)
print("All Videos Downloader")
print("*"*135)

print("1: Download a video")
print("2: Download a full playlist")
print("3: Specific video in a playlist by a number")
print("4: Download an audio")
print("5: Exit")

while True:
    try:
       choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    try:
        if choice == 1:
            print("You chose to download a video.")
            url = input("Enter the URL of the video: ")
            if not url:
                print("Please enter a URL for downloading? ")
            elif "playlist?" in url and choice == 1:
                print(f"{url} is not a URL for video.")
            elif "youtube.com" not in url and choice == 1:
                print("This is not a YouTube URL.")
            else:
                print("Downloading your video...")
                yt_dlp.YoutubeDL({
                    'format': 'best',
                    'outtmpl': '%(title)s.%(ext)s',
                }).download([url])
                print("<"*135)
                print("Download successfully complete.")
                print(">"*135)


        elif choice == 2:
            print("You chose to download a full playlist.")
            url = input("Enter the URL of the playlist: ")
            if not url:
                print("Please enter a URL for downloading? ")
            elif "playlist?" not in url and choice == 2:
                print("This is not a url for playlist.")
            elif "youtube.com" not in url and choice == 2:
                print("This is not a YouTube URL.")
            else:
                print("Downloading your playlist...")
                yt_dlp.YoutubeDL({
                    'format': 'best',
                    'outtmpl': 'playlist Downloads/%(playlist_index)s/%(uploader)s - %(upload_date)s/%(title)s.%(ext)s',
                }).download([url])
                print("<"*135)
                print("Download successfully complete.")
                print(">"*135)

    
        elif choice == 3:
            print("You chose to download a specific video in a playlist by a number.")
            
            url = input("Enter the URL of the playlist: ")
            if not url:
                print("Please enter a URL for downloading? ")
            elif "playlist?" not in url and choice == 3:
                print("This is not a url for playlist.")
            elif "youtube.com" not in url and choice == 3:
                print("This is not a YouTube URL.")
            else:
                print("Your videos in playlist is downloading...")
                yt_dlp.YoutubeDL({
                "playliststart": int(input("Enter your playlist start number: ")),
                "playlistend": int(input("Enter your playlist end number: ")),
                "format": "best",
                "outtmpl": "%(title)s.%(ext)s"
                }).download([url])
                print("<"*135)
                print("Download successfully complete.")
                print(">"*135)
            

        elif choice == 4:
            print("You chose to download an audio.")
            
            url = input("Enter your URL of the audio: ")
            if not url:
                print("Please enter a URL for downloading? ")
            elif "playlist?" in url and choice == 4:
                print("This is not a url for audio.")
            elif "youtube.com" not in url and choice == 4:
                print("This is not a YouTube URL.")
            else:
                print("Downloading your audio...")
                yt_dlp.YoutubeDL({
                "format": "bestaudio",
                "outtmpl": "%(title)s.mp3",
                "postprocessors": [{
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192"
                }]
                }).download([url])
                print("<"*135)
                print("Download successfully complete.")
                print(">"*135) 
    
    
        elif choice == 5:
            break

        else:
            print("Invalid choice. Please try again.")

    except Exception:
        print("*"*130)
        print("Error: Something went wrong.")
        print("*"*130)
print("*"*135)
print("Thanks for using the Downloader!!!")
print("*"*135)
        
   
 