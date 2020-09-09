a = int(input("enter the number: "))
x=[1]

temp = 1

while (temp<=a):
    if(temp%2!=0 and temp!=1):
        last = x[len(x)-1]
        x.append(last+2)
        x.append(last+4)

    temp = temp + 1

print(x)