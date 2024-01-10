a = ["1", "2", "3", "4", "5"]
b = []
for x in a:
    x = int(x)
    b.append(x)
print(b)

c = []
for i in range(0,21):
    if(i%2==1):
        c.append(i)
print(c)

d = []
for j in range(0,101):
    if(j%3==0):
        d.append(j)
print(d)

positive = True
add = 0
count = 0
while positive:
    numbers = int(input("Enter next number (negative number to stop): "))
    if(numbers < 0):
        print("Sum of all positive numbers: ",add)
        print("Average of all positive numbers: ",(add/count))
        positive = False
    add = add+numbers
    count+=1

