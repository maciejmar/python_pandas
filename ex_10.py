'''dict comprehension'''
diction = {"apple": 3.0, "banana": 2.5, "milk": 6.0, "coco":22.0}
vat=1.23
prices_vat = { k : round(v*vat,2) for k , v in diction.items()  }
print("prices_vat ",prices_vat)

prices = {"apple": 3.0, "banana": 2.5, "milk": 6.0}
vat = 1.23

prices_gross = {k: round(v * vat) for k, v in prices.items()}
print(f" prices_gross={prices_gross}")

'''dict generator'''
def dict_c(diction, vat):
    for d in diction:
        d= d.items()*vat     
    yield d
for i in dict_c(diction, vat):
    print(f"dictionary ", i)
'''lists comprehension'''
list_a = [k for k in range(10)]
print(f"list_a comprehension ", list_a)



'''list generator'''
list_b = (k for k in range(10))
print(f"list_b ", {list_b})

list_c = (l+3 for l in range(10) if l%2 == 0)
print(f"list_c {list_c}")


'''another examples'''
#comprehenshive list
list_a = [ k**3 for k in range(10) ]
print("======================")
print(f"list_a , {list_a}")
#list generator
list_b = (k**3 for k in range(10))
for li in list_b :
   print(f" list_gen {li}")
   
#comprehenshive dict 
dict_a = {"ala":4, "mac":45, "ada":4, "zoa":43, "anla":34, "edu":23 }
vat=1.23
dict_c = (k,v )
print()
dict_vat = { k: v*vat for k,v in dict_a.items()}
print(f"dict = {dict_vat}")
dict_vat_2 = ( (k,v*vat) for k,v in dict_a.items())
dict_vat_2 = dict(dict_vat_2)
print(f"dict 2 = {dict_vat_2}")

#generator dict
dict_b =  dict( (k,v*vat) for k,v in dict_a.items() )

print(f"dict_b_gen {dict_b}" )

#generator without list or dict

gen_a = sum(v*vat for v in dict_a.values())
for i in dict_a:
    print(f"dict{i} = {gen_a}")