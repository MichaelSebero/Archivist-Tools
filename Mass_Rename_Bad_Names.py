import os
import re
from tqdm import tqdm

def rename_files(dir_path, keyword, media_extensions):
    total_files = 0
    renamed_files = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.splitext(file_path)[1].lower() in media_extensions:
                total_files += 1
                for kw in keyword:
                    if kw in file:
                        new_file = re.sub(re.escape(kw), '', file)
                        os.rename(file_path, os.path.join(root, new_file))
                        renamed_files += 1
                        break
    return total_files, renamed_files

print("Enter the directory path: ")
dir_path = input()

keyword = ["(128kbit_AAC)", "(192kbit_AAC)", "(720p_30fps_H264-128kbit_AAC)", "(1080p_24fps_H264-128kbit_AAC)", "(480p_30fps_H264-128kbit_AAC)", "(1080p_30fps_H264-128kbit_AAC)", "(2160p_30fps_VP9 LQ-128kbit_AAC)", "(360p_30fps_H264-128kbit_AAC)", " (360p_30fps_H264-96kbit_AAC)", "(1080p_6fps_H264-128kbit_AAC)", "(360p_25fps_H264-128kbit_AAC)", "(480p_25fps_H264-128kbit_AAC)", "(720p_24fps_H264-192kbit_AAC)", "(240p_24fps_H264-96kbit_AAC)", "(1080p_60fps_H264-128kbit_AAC)", "(1080p_60fps_H264-128kbit_AAC)", "(720p_30fps_H264-192kbit_AAC)", "(2160p_24fps_VP9 LQ-128kbit_AAC)", "(2048p_25fps_VP9 LQ-128kbit_AAC)", "(470p_30fps_H264-128kbit_AAC)", "(1080p_25fps_H264-128kbit_AAC)", "(864p_24fps_H264-128kbit_AAC)", "(720p_25fps_H264-128kbit_AAC)", "(2160p_25fps_VP9 LQ-128kbit_AAC)", "(1440p_30fps_H264-128kbit_AAC)", " (720p_24fps_H264-128kbit_AAC)", "(1080p_30fps_AV1-128kbit_AAC)", "(720p_6fps_H264-128kbit_AAC)", "(240p_30fps_H264-96kbit_AAC)"] or [" (128kbit_AAC)", " (192kbit_AAC)", " (720p_30fps_H264-128kbit_AAC)", " (1080p_24fps_H264-128kbit_AAC)", " (480p_30fps_H264-128kbit_AAC)", " (1080p_30fps_H264-128kbit_AAC)", " (2160p_30fps_VP9 LQ-128kbit_AAC)", " (360p_30fps_H264-128kbit_AAC)", " (360p_30fps_H264-96kbit_AAC)", " (1080p_6fps_H264-128kbit_AAC)", " (360p_25fps_H264-128kbit_AAC)", " (480p_25fps_H264-128kbit_AAC)", " (720p_24fps_H264-192kbit_AAC)", " (240p_24fps_H264-96kbit_AAC)", " (1080p_60fps_H264-128kbit_AAC)", " (1080p_60fps_H264-128kbit_AAC)", " (720p_30fps_H264-192kbit_AAC)", " (2160p_24fps_VP9 LQ-128kbit_AAC)", " (2048p_25fps_VP9 LQ-128kbit_AAC)", " (470p_30fps_H264-128kbit_AAC)", " (1080p_25fps_H264-128kbit_AAC)", " (864p_24fps_H264-128kbit_AAC)", " (720p_25fps_H264-128kbit_AAC)", " (2160p_25fps_VP9 LQ-128kbit_AAC)", " (1440p_30fps_H264-128kbit_AAC)", " (720p_24fps_H264-128kbit_AAC)", " (1080p_30fps_AV1-128kbit_AAC)", " (720p_6fps_H264-128kbit_AAC)", " (240p_30fps_H264-96kbit_AAC)"]

media_extensions = [".mp4", ".m4a", ".oog", ".webm", ".mp4", ".avi", ".mkv", ".wmv"]

total_files, renamed_files = rename_files(dir_path, keyword, media_extensions)

print("Renamed", renamed_files, "out of", total_files, "files")
