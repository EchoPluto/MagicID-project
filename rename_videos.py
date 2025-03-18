import os
import re

def rename_videos_in_directory(directory):
    # 获取目录下所有的mp4文件
    video_files = [f for f in os.listdir(directory) if f.endswith('.mp4')]
    
    # 按文件名排序
    video_files.sort()
    
    # 重命名文件
    for index, old_name in enumerate(video_files, start=1):
        old_path = os.path.join(directory, old_name)
        new_name = f"{index}.mp4"
        new_path = os.path.join(directory, new_name)
        
        try:
            os.rename(old_path, new_path)
            print(f"已重命名: {old_name} -> {new_name}")
        except Exception as e:
            print(f"重命名 {old_name} 时出错: {str(e)}")

def main():
    # 视频根目录
    base_dir = "static/images/videos"
    
    # 遍历所有子目录
    for root, dirs, files in os.walk(base_dir):
        if any(f.endswith('.mp4') for f in files):
            print(f"\n处理目录: {root}")
            rename_videos_in_directory(root)

if __name__ == "__main__":
    main() 