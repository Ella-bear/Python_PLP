#read and writes a modified file
with open ('day4/read.txt', 'r')as file:
    content = file.read()
    print(content)

#outputs Python is an intresting language

#write a modified file
#Python is an intresting langaugae was my initial text in read.txt file
with open ('day4/read.txt', 'a')as file:file.write('This is my week 4 task')

