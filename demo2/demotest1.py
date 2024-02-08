#with open ("demo.txt", r)
#print()

#Open a file in read-only mode
# f = open ("demo.txt", "r")
# print(f.read())

f = open ("demo.txt", "w")
f.write(" How are you") 
print("done!")


f = open ("demo2.txt", "w")
Lines = f.readlines()
print("Lines:", Lines)
# Strips the newline characters
for line in Lines:
    print(line.strip())
    