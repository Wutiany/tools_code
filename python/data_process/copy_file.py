import os
import shutil


def move_file(dir_path, move_path, name_list):
    name_list = os.listdir(name_list)
    file_type = os.listdir(dir_path)[0].split('.')[-1]
    # 改同名文件的文件类型
    name_list = [name.split('.')[0] + file_type for name in name_list]






if __name__ == "__main__":
    dir_path = r""
    move_path = r""
    name_list = []
    move_file(dir_path, move_path, name_list)
