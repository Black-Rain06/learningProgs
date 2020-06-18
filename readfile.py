'''

file = open('filename', mode)

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists




"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


'''

def readt():

  f = open("demofile.txt", "r")
  print(f.read())

#readt()

def readl():
  f = open("demofile.txt", "r")
  for i in f.readline():
    print(i)

#readl()

def iterf():
  f = open("demofile.txt", "r")
  for x in f:
    print(x)

#iterf()

def readlclose():
  f = open("demofile.txt", "r")
  print(f.readline())
  f.close()

#readlclose()
'-----------------'

def append():
  f = open("demofile2.txt", "a")
  f.write("\nNow the file has more content!")
  f.close()

append()

def write():
  f = open("demofile.txt", "w")
  f.write("Woops! I have deleted the content!")
  f.close()

#write()

##'__________________'

import os

def remove():
  os.remove("demofile.txt")

#remove()

def remove2():
  if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
  else:
    print("The file does not exist")

#remove2()

def remove3():
  os.rmdir("myfolder")

remove3()
