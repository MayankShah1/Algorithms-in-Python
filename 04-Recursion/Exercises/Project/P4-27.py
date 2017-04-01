import os

def walk(path):
    #print(path)
    if os.path.isdir(path):
        dirs = []
        files = []
        for file in os.listdir(path):
            childpath = os.path.join(path,file)
            if os.path.isfile(childpath):
                files.append(file)
            else:
                dirs.append(file)
            walk(childpath)
        res_tup = (path, dirs, files)
        print(res_tup)
        #yield res_tup

#Testing
walk('/home/mayank/Desktop/Algorithms-in-Python')
#for res in walk('/home/mayank/Desktop/Algorithms-in-Python'):
 #   print(res)

