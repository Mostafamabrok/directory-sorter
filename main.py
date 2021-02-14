import shutil
import os

directory = input("Folder you want to organize, Full path please: ")
targets = [os.path.join(directory,"pdfs"), os.path.join(directory,"Pictures"), os.path.join(directory,"worddocs"), os.path.join(directory,"zipfiles"), os.path.join(directory,"misc"), os.path.join(directory,"txtfiles")]

def move():
    shutil.move(os.path.join(directory, filename), os.path.join(target, filename))

for paths in targets:
    if not os.path.isdir(paths):
        os.mkdir(paths)

for filename in os.listdir(directory):
        
    if filename.endswith(".zip"):
        target = targets[3]
        move()
        
    if filename.endswith(".png") or filename.endswith(".jpg"):
        target = targets[1]
        move
        
    if filename.endswith(".pdf"):
        target = targets[0]
        move()
        
    if filename.endswith(".docx"):
        target = targets[2]
        move
        
    if filename.endswith(".txt"):
        target = targets[5]
        move()    
        
    if os.path.isdir(os.path.join(directory, filename)):
        continue
    elif os.path.isfile(os.path.join(directory, filename)):
        target = targets[4]
        shutil.move(os.path.join(directory, filename), os.path.join(target, filename))

        
                    