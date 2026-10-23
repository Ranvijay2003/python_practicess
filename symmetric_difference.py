n=int(input())
set1 = set()
for i in range(n):
    set1.add(int(input()))

m=int(input())
set2 = set()
for i in range(m):
    set2.add(int(input()))
result_set=set1.symmetric_difference(set2)
print(len(result_set))

