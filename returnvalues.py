def calculate(a,b):
    sum = a+b
    sub = a-b
    product = a*b

    return sum,sub,product
a,b =10,5
result = calculate(a,b)

sum,sub,product = result

print(f"sum is{sum}\n subtrsction is {sub}\n multiplication is {product}")
