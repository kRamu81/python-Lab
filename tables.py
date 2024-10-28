def multiplicationTable(number):
    for i in range(1,11):
        print(f"{number}*{i}={number*i}")

num=int(input("enter the value:"))
multiplicationTable(num)
