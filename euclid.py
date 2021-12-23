import math

format_string = "{:<10}{:<8}{:<10}{:<8}{:<10}{:<8}"

def ext_gcd(a, b):
	if b == 0: 
		print(format_string.format(*[a, b, '-', a, 1, 0]))
		return (a, 1, 0)
	q = math.floor(a/b)
	temp_d, temp_x, temp_y = ext_gcd(b, a % b)
	d, x, y = temp_d, temp_y, temp_x - (q * temp_y)
	print(format_string.format(*[a,b,q,d,x,y]))
	return (d, x, y)

print()
print(format_string.format(*['A', 'B', '[A/B]', 'D', 'x', 'y']))
d, x, y = ext_gcd(1970, 1066)
print()
print(f"gdc = {d}")
print(f"x = {x}")
print(f"y = {y}")