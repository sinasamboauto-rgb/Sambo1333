with open("rwx/Write_note.txt","w") as f:
    f.write("Hello World!\n")
    f.write("World, Hello!\n")
print("Write_note was created!")

with open("rwx/Write_note.txt","r") as f:
    content = f.read()
    
print(content)

with open("rwx/Write_note.txt","r") as f:
    firstline = f.readline()
print(firstline.strip())

with open("rwx/Write_note.txt","r") as f:
    countline = f.readline()
print("Total lines: ", len(countline))