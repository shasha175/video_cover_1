
import os
import requests
from moviepy.editor import VideoFileClip

def download_video(url, download_folder):
    """
    从URL下载视频文件到指定文件夹。
    :param url: 视频文件的URL。
    :param download_folder: 下载文件保存的文件夹路径。
    :return: 下载文件的本地路径。
    """
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(download_folder, exist_ok=True)
        filename = os.path.join(download_folder, url.split('/')[-1])
        with open(filename, 'wb') as file:
            file.write(response.content)
        return filename
    else:
        raise Exception(f"Failed to download video from {url}")

def set_video_cover_from_url(video_urls, frame_time=2_):
    """
    从视频URL列表中提取视频封面并设置为视频的封面。

    :param video_urls: 包含视频URL的列表。
    :param frame_time: 提取封面的时间点（秒），默认为2秒。
    """
    download_folder = "temp_videos"

    for url in video_urls:
        try:
            # 下载视频
            video_file = download_video(url, download_folder)

            # 提取封面
            my_clip = VideoFileClip(video_file)
            video_filename = os.path.basename(video_file)
            video_name, _ = os.path.splitext(video_filename)
            cover_frame = my_clip.get_frame(frame_time)

            # 将封面帧设置为视频的封面
            my_clip = my_clip.set_duration(my_clip.duration).set_cover(cover_frame)
            output_video_path = os.path.join(download_folder, f"{video_name}_with_cover.mp4")
            my_clip.write_videofile(output_video_path, codec='libx264')
            print(f"Set cover frame for {video_filename} and saved as {output_video_path}")
        except Exception as e:
            print(f"Failed to process {url}: {e}")
