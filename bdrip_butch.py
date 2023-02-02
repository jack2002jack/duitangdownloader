import os
import shutil
def buntch(path,target_list=["CDs","SPs","Scans","Menus"]):
    dirs=os.listdir(path)
    for dir in dirs:
        dir=path+"/"+dir
        ddirs=os.listdir(dir)
        print(dir+"正在处理。。。")
        if not "Extra" in ddirs:
           extra_dir=dir+'/'+"Extra"
           os.mkdir(extra_dir)
           count = 0
           name_list=["A","B","C","D"]
           for ddir in ddirs:
               ddir=dir+'/'+ddir #dir=W:/Anime/Charlotte ddir= dir+s1
               if os.path.isdir(ddir):
                   for i in os.listdir(ddir):
                       if i in target_list:
                            target= ddir+"/"+i
                            os.renames(target,extra_dir+"/"+name_list[count]+"/"+i)
                            count += 1
           print(dir + "处理完成")
        else:
            print(dir+"已存在EXtra")
            extra_dir = dir + '/' + "Extra"
            extra_dirs=os.listdir(extra_dir)
            if not ".ignore" in extra_dirs:
                with open(extra_dir+"/"+".ignore","w"):
                    print("为您创建了.ignore")

if __name__=="__main__":
    target_path = r"W:\Anime"
    buntch(target_path)
