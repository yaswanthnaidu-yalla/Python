try:
    with open ('file.txt','w') as file:
        file.write("hi")
    with open('file.txt','r') as file:
        content=file.read()
        print(content)
except FileNotFoundError as e:
    print(e)
finally :
    with open ('file.txt', 'a') as file:
        file.write("i am done")

raise ValueError("something went wrong")


