x = int(input())
sum = 0
for i in range(0,x+1):
    if i% 2!=0:
        sq=i**2
        sum = sum+sq
print(sum)