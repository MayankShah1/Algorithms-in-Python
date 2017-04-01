# Reading from file

# Method 1 :
file_handler = open('//home//mayank//Desktop//demo.py','r')
print('File contains : \n ',file_handler.read())

# Method 2 :
line = file_handler.readline()
while line != '':
    line = line.strip('\n')
    print(line)
    line = file_handler.readline()

# Method 3 :
for line in file_handler:
    print(line.strip('\n'))

# Write contents in another file
file_handler_write = open('//home//mayank//Desktop//demo.txt','w')
print('File contains : \n ',file_handler.read(),file=file_handler_write)
