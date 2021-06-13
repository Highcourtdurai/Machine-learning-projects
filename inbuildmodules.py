import os
print(os.getcwd())

#os.mkdir("test")#mkdir-make directory

os.chdir("sample")#chdir-change directory
print(os.getcwd())

os.chdir("..")# again come back to files

print(os.listdir("/Users/Galaxy/Documents/Anaconda(Spyder)"))

for i in os.walk("/Users/Galaxy/Documents/file.py"):
    print(i)

print(os.path.isfile("/Users/Galaxy/Documents/sample"))

path=input("Enter path:")

folder_count=0
file_count=0

if os.path.exists(path):
    for i in os.listdir(path):
         # print(path+"/"+i)
         # print(os.path.join(path,i))
        if os.path.isfile(path+"/"+i):
            file_count+=1
        elif os.path.isdir(path+"/"+i):
            folder_count+=1
else:
    print("The given path doesnot exist")
    

print(f"The given path contains {folder_count} folders")

print(f"The given path contains {file_count} files")





import datetime

print(datetime.datetime.now())

obj=datetime.datetime(2020,9,28)

print(obj.year)
print(obj.date)
print(obj.month)

print(obj.strftime("%m %d %y %w %a"))

str1="09 28 20"
obj=datetime.datetime.strptime(str1, "%m %d %y")
print(obj)

import time
time.sleep(2)

time.time()



# import csv
# import openpyxl
# import json
# import BeautifulSoup
# import requests
