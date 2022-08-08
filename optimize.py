import os
import getpass
import shutil

user_name = getpass.getuser()
dir_path = "C:\\Users\\{name}\\source\\repos".format(name =user_name)
project_list = os.listdir(dir_path)

for project_dir in project_list:
    file_path = dir_path + "\\"+project_dir+"\\.vs\\"+project_dir
    try:
        dir_list = os.listdir(file_path)
    except:
        print( "The file doesn't exist in \'" + file_path+"\'")
        
    ver = []
    for dir in dir_list:
        if dir[0] == 'v':
            ver.append(dir)
            
    ver = list(map(lambda x: file_path + "\\" + x, ver))
    ver = list(map(lambda x: [x+"\\ipch",x+"\\Browse.VC.db"],ver))
    
    for files in ver:
        if os.path.exists(files[0]):
            shutil.rmtree(files[0])
        if os.path.exists(files[1]):
            os.remove(files[1])
    
