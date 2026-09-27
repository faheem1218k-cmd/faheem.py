Number = int(input("Enter a Number"))
for i in range(1,11):
    print(f"{Number} * {i} = {Number * i}")
    if Number * i == 40:
     break