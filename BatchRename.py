import os
import shutil

class Rename():
    # 获取当前工作目录
    def __init__(self):
        self.image_folder = os.getcwd()
        # print(image_folder)
    def rename(self):
        
        # 存储重命名规则的字符串列表
        rename_list = ["image1", "image2", "image3","image4"]
        image_size_width=input("请输入图片Width:")
        image_size_height=input("请输入图片Height:")
        # 遍历指定目录下的所有文件夹
        for root, dirs, files in os.walk(self.image_folder):
            for i,file in enumerate(files):
                if file.lower().endswith(('.bmp','.png','.jpg')):
                    # 获取当前文件夹名称
                    folder_name = os.path.basename(root)
                    old_file_path = os.path.join(root, file)
                    new_file_name = folder_name+"_" + rename_list[i % len(rename_list)] + "_"+ image_size_width + "_" + image_size_height + "_"+ '{:03d}'.format(i) + os.path.splitext(file)[1]
                    new_file_path = os.path.join(root, new_file_name)
                    os.rename(old_file_path, new_file_path)
                    print('Convert %s to %s ...'%(old_file_path, new_file_path))

if __name__ =='__main__':
    run =Rename()
    run.rename()                 