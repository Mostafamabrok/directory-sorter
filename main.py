import shutil
import os

directory = input("Folder you want to organize, Full path please: ")
targets = [os.path.join(directory,"pdfs"), os.path.join(directory,"Pictures"), os.path.join(directory,"worddocs"), os.path.join(directory,"zipfiles"), os.path.join(directory,"misc"), os.path.join(directory,"txtfiles")]


for filename in os.listdir(directory):
    
    for paths in targets:
        if not os.path.isdir(paths):
            os.mkdir(paths)

    
    if filename.endswith(".zip"):
        target = targets[3]
        shutil.move(os.path.join(directory, filename), os.path.join(target, filename))
    if filename.endswith(".png") or filename.endswith(".jpg"):
        target = targets[1]
        shutil.move(os.path.join(directory, filename), os.path.join(target, filename))
    if filename.endswith(".pdf"):
        target = targets[0]
        shutil.move(os.path.join(directory, filename), os.path.join(target, filename))
    if filename.endswith(".docx"):
        target = targets[2]
        shutil.move(os.path.join(directory, filename), os.path.join(target, filename))
    if filename.endswith(".txt"):
        target = targets[5]
        shutil.move(os.path.join(directory, filename), os.path.join(target, filename))    
    if os.path.isdir(os.path.join(directory, filename)):
        continue
    elif os.path.isfile(os.path.join(directory, filename)):
        target = targets[4]
        shutil.move(os.path.join(directory, filename), os.path.join(target, filename))

        
                    