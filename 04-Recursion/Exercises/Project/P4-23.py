import os

def find(path, filename):
    if os.path.isdir(path):
        for file in os.listdir(path):
            if filename == file:
                print(path+'/'+file)
            childpath = os.path.join(path, file)
            #print(childpath)
            find(childpath,filename)
    else:
        if path == filename:
            print(path)

find('/home/mayank/Desktop/Algorithms-in-Python','P4-23.py')