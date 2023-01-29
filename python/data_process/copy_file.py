import os
import shutil


def move_file(dir_path, move_path, name_path):
    name_list = os.listdir(name_path)
    file_type = os.listdir(dir_path)[0].split('.')[-1]
    # 改同名文件的文件类型
    name_list = [name.split('.')[0] + '.' +  file_type for name in name_list]
    for name in name_list:
        shutil.copy(os.path.join(dir_path, name), os.path.join(move_path, name))





if __name__ == "__main__":
    dir_path = r"E:\data\zip\east_china_sea_20_34_117_132\2014"
    move_path = r"E:\data\eddy_dataset_augment\eddy_img"
    name_path = r"E:\data\eddy_dataset_augment\eddy_json"
    move_file(dir_path, move_path, name_path)
