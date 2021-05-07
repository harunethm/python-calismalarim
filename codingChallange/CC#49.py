str1 = input("1. string : ")
str2 = input("2. string : ")

_str1 = set(str1)
_str2 = set(str2)

print(_str1)
print(_str2)

for i in _str1:
  for j in _str2:
    if i == j:
      print(i + "-")

#iki stringi karşılaştır aynı olan harfleri say
