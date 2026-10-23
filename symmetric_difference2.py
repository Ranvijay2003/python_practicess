n=int(input())
set1 = list(input().split(" "))

print(set1)
set1 = set(set1)
print(set1)

m=int(input())
set2 = set(list(input().split(" ")))

result_set=set1.symmetric_difference(set2)
print(len(result_set))