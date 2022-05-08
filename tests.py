count = 0
length = 3
list = []
while True:
    try:
        number = int(input("Enter a number: "))
        list.append(number)
        if count == len-1:
            break
    except:
        continue
    count = count+1

print(list)
