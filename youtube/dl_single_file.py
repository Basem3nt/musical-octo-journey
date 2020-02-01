from pytube import YouTube
import os
from tqdm import tqdm


class DownloadSingleFile:

    def __init__(self, url: str):
        self.yt = YouTube(url)
        self.title = self.yt.title
        self.thumbnail = self.yt.thumbnail_url

        self.total_filesize = 0
        self.progress_bar = None

        self.yt.register_on_progress_callback(self.show_progress_bar)
        self.yt.register_on_complete_callback(self.on_download_complete)

    def on_download_complete(self, stream, file_handler):
        self.progress_bar.close()

    def show_progress_bar(self, stream, chunk, file_handler, bytes_remaining):
        self.progress_bar.update(bytes_remaining)
        return  # do work

    def download_audio(self):
        streams = self.yt.streams.filter(only_audio=True).all()
        if len(streams) == 0:
            print("No audio file available")
        else:
            self.total_filesize = streams[0].filesize
            self.progress_bar = tqdm(
                desc=self.title,
                total=self.total_filesize,
                leave=False,
                ncols=10,
                miniters=10,
                unit="Byte",
                smoothing=0.5,
            )
            streams[0].download()

    def download_video(self):
        streams = self.yt.streams.filter(only_video=True).all()
        if len(streams) == 0:
            pass
        else:
            pass

    def download_both(self):
        pass


if __name__ == "__main__":
    # DownloadSingleFile("https://youtu.be/9bZkp7q19f0").download_audio()
    DownloadSingleFile(
        "https://www.youtube.com/watch?v=x0ctImlIThY").download_audio()
