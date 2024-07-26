import os
from moviepy.editor import VideoFileClip
# 设置视频文件夹路径
path = 'D:/test'
result='D:/Baching_cover_video_result'

# 获取文件夹中的所有文件路径 ,满足条件的文件路径将被收集到列表  中
files = [os.path.join(path, file) for file in os.listdir(path) if file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]

# 对每个视频文件提取封面并保存为图片
for i, file in enumerate(files):
    try:
        my_clip = VideoFileClip(file)
        video_filename = os.path.basename(file)
        video_name, _ = os.path.splitext(video_filename)
        output_image_path = os.path.join(result, f"{video_name}_cover.png")
        my_clip.save_frame(output_image_path, t=2)
        print(f"Extracted and saved frame from {video_filename} as {output_image_path}")
    except Exception as e:
        print(f"Failed to process {file}: {e}")


