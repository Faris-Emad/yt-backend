from yt_dlp import YoutubeDL

ydl_opts = {}

def fetch_raw_info(url):
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return ydl.sanitize_info(info)



if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    info = fetch_raw_info(url)
    print(f"Title: {info.get('title')}")
    print(f"Duration: {info.get('duration')}")
    print(f"Thumbnail: {info.get('thumbnail')}")
    print(f"Description: {info.get('description')}")