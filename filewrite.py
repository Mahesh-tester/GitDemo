# read the file and store all the lines in list
#reverse the list
#write the list back to the file

with open('text.txt','r') as reader:
    content=reader.readlines() #[here all will be converted to list]
    reversed(content) #[here it will be reversed
    # ]
    with open('text.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)