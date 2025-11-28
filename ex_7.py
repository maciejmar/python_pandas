list_a = [1,2,3,2,1,3,4,3,2,1,2,3,4,2,1,2,2,2,3,2]
dict ={}
for li in list_a:
    dict[li] = dict.get(li,0)+1
print(f"dict is {dict}")