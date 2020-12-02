try:
    with open('filelog.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)
    #print("soemhow how i reache this block because there is failure in try block")

finally:
    print("cleaning up resources")