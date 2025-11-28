gen = (x**2 for x in range(20))
print(next(gen))  # 0
print(next(gen))  # 1

print(next(gen))
print(list(gen))