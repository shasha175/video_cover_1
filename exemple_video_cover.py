# from video_cover_extractor import extract_video_covers_from_url
#
# # 调用函数示例
# video_urls = [
#     'https://v.douyin.com/iMPtA9po/.mp4',
# ]
# output_folder = 'D:/Baching_cover_video_result'
# extract_video_covers_from_url(video_urls, output_folder)



from video_cover_extractor import set_video_cover_from_url

# 示例用法
if __name__ == "__main__":
    video_urls = [
        "https://example.com/video1.mp4",
        "https://example.com/video2.mp4"
    ]
    set_video_cover_from_url(video_urls, frame_time=2)
