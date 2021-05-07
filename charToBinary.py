#binary karşılık
test_str = "abc def"
res = '*'.join(format(i, 'b') for i in bytearray(test_str, encoding ='utf-8'))
print(res)
#ascii karşılığı
print(ord("a"), ord("A"))
#------
arr = list(test_str.split(" "))
print(arr)
#-------
strin = "How can mirrors be real if our eyes aren't real"
strin = strin.title()
arr = list(strin)
a = strin.find("'")
arr[a+1] = chr(ord(arr[a+1])+32)
strin = str(arr)
print(strin)