def complexinput():
    real=float(input("enter the real part:"))
    img=float(input("enter the img part:"))
    return complex(real,img)

print("enter the first complex number?")
c1=complexinput()

print("enter the second complex number?")
c2=complexinput()

add=c1+c2
multiply=c1*c2

print(f"addtion is {add},multiplaation is{multiply}")
