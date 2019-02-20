# 1928. Base64 Decoder

baseAZ = {chr(n+65): n for n in range(26)}
baseaz = {chr(n+71): n for n in range(26, 52)}
base09 = {chr(n-4): n for n in range(52, 62)}
base64 = {'+': 62, '/': 63}

base64 = dict(baseAZ, **base64)
base64 = dict(baseaz, **base64)
base64 = dict(base09, **base64)


for T in range(int(input())):
    enc = input()
    dec = ''
    for x in enc:
        dec += "%6.6d" % int(bin(base64[x])[2:])
    code = ''
    while len(dec):
        code += chr(int(dec[:8].lstrip('0'), 2))
        dec = dec[8:]
    print(f"#{T+1} {code}")









# sb else's code:
b = [chr(k) for k in range(65,91)] + [chr(k) for k in range(97,123)] + [str(k) for k in range(10)] + ['+','/']
for i in range(int(input())):
    n = input()
    l = [n[t*4:t*4+4] for t in range(len(n)//4)]
    print(f'#{i+1} ',end='')
    for j in l:
        c = ''
        for k in range(4):
            c += str(bin(b.index(j[k]))[2:].zfill(6))
        for m in range(3):
            a = chr(int(c[m*8:m*8+8],2))
            print(a,end='')
    print()


# sb else's code 2:
l=[chr(k) for k in range(65,91)]+[chr(k) for k in range(97,123)]+[str(k) for k in range(10)]+['+','/']
for i in range(int(input())):
    s=''
    print(f'#{i+1} ',end='')
    for j in input():
        s+=bin(l.index(j))[2:].zfill(6) 
    for i in [s[j*8:(j+1)*(8)] for j in range(len(s)//8)]:
        print(chr(int(i,2)),end='')
    print()