FileName = input("Enter a file name: ") #take file name as input
FileHandle = open(FileName, mode='r') #open that file
for line in FileHandle: #iterate the file line by line
    l = line.rstrip()
    print(l.upper()) #print the lines by converting in upper case

