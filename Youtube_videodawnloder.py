from pytube import YouTube

def download(link):
    Object = YouTube(link)
    Object = Object.streams.get_highest_resolution()
    try:
        Object.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: " )
download(link)