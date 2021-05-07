print("başladı")
a = int(input("bir sayı gir "))
b = int(input("bir sayı gir "))

for c in range(a,b):
	for d in range(1,11):
		print(c, "x", d, "=", c*d)
	print("==============")
print("program bitti")