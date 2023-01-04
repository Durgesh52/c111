import os
import shutil

source="C:/Users/HP/Downloads"
dest="F:/dest"

list_of_files=os.listdir(source)

for s in list_of_files:
    name,extension = os.path.splitext(s)
  
    if(extension==""):
        continue
    if extension in[".png",".gif",".jpg",".jpeg" ]:
        path1=source +  "/" +s
        path2=dest+ "/" +"Image_files"
        path3=dest+ "/" +"Image_files" + "/" + s
        if os.path.exists(path2):
            print("Moving ",s)
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving ",s)
            shutil.move(path1,path3)
    

