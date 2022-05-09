count = 0
len = 5
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
