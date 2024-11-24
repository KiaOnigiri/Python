def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


n = int(input())
sp = ''

for _ in range(n):
    x = int(input())
    x = convert_to(x,12)
    sp+=str(x)

print(sp.count('0')+sp.count('1')+sp.count('2')+sp.count('3'))
