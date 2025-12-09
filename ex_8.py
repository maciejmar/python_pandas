"""generator"""
suma = 0
lista = (x*2 for x in range(10))
suma = sum(lista)
print (f"list {suma}")


'''list comprehenshion'''
lista_a = [x*2 for x in range(10)]
suma_a = sum(lista_a)
print (f"list {suma_a}")