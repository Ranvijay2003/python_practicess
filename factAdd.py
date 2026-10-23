x = int(input())
sum = 0
for i in range(1,x+1):
    sum = sum + i
print("Sum =", sum)

y = int(input())
mul = 1
for j in range(1,y+1):
    mul = mul * j
print("mul=", mul)

for k in range(1,100+1):
    if k% 2 == 0:
        print(k)


for z in range(1,20,3):
    print(z)


l = []
for t in range(1,20,3):
    l.append(t)
print(l)