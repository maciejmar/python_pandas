list_a = [1,1,20,30,20,10,3,2]
list_b =  [a*a for  a in list_a if a%2 == 0 ]
print(list_b)
list_b = (a*a for  a in list_a if a%2 == 0)
for b in list_b:
    print(b)