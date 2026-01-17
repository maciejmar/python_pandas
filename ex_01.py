dict_start = {"first":1, "second":2, "third":"3"}
dict_nums = {name:numb*numb  for name,numb in dict_start.items() if isinstance(numb, (int, float))}
print(dict_nums)