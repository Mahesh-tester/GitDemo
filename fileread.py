file=open('text.txt')

# readlines gives a list
# Using for and readlines

for line in file.readlines():
    print(line)

file.close()

# Uisng while and readline
#line=file.readline()
#while line!="":
#    print(line)
#    line = file.readline()