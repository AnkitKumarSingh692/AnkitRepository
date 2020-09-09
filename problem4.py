size = int(input())

inp_list = []

for i in range(0, size):
    temp = int(input())
    inp_list.append(temp)

dict = {}

for i in range(1,10):
    count = 0
    for j in inp_list:
        if((j % i==0)):
            count = count + 1

    dict[i] = count

print(dict)