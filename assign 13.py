'''
ASSIGNMENT-13
File Handling

1.Write a Python program to read  lines of a file.
2. Write a Python program to copy the contents of a file to another file

3.Write a Python program to combine each line from first file with the corresponding line in second file.


'''











'''
f=open("Mynewnew.txt","w")
f.write("hi hello")
f.close()
f=open("Mynewnew.txt","r")
print(f.readlines())


a=open("a.txt","w")
a.write("a b c d ")
a.close()

b=open("b.txt","w")
b.write("1 2 3 4 5 ")
b.close()


with open("in.txt") as f:
    lines = f.readlines()
    with open("out.txt", "w") as f1:
        f1.writelines(lines)
    
'''
with open("in.txt") as f:
    lines = f.readlines()
    with open("out.txt", "a") as f1:
        f1.writelines(lines)
