def Bbit_print(i):
    res = ""
    for j in range(7, -1, -1):
        res += "1" if i & (1<<j) else "0"
    print(res)

Bbit_print(4)


############################################
###########################################

tmp = '0000000111100000011000000111100110000110000111100111100111111001100111'

# for i in range(0, 70, 7):
#     print(int(tmp[i:i+7], 2))

for i in range(0, 70, 7):
    num = tmp[i:i+7]
    res = 0
    for j in range(6, -1, -1):
        res += (int(num[j]) * 2**(6-j))
    print(res)

###########################################
############################################

a = '01D06079861D79F99F'
# a = '0F97A3'
# a = '0F97A33'

i = -1  # idx for reading 'a'
b = ''
res = []

while i < len(a)-1:
    if len(b) < 7:
        i += 1
        b += bin(int(a[i], 16))[2:].zfill(4)
    else:
        res.append(int(b[:7], 2))
        b = b[7:]
while len(b) >= 7:
    res.append(int(b[:7], 2))
    b = b[7:]
if b:
    res.append(int(b, 2))
print(*res, sep=", ")


##############################################
#############################################

pattern = [
    '001101',
    '010011',
    '111011',
    '110001',
    '100011',
    '110111',
    '001011',
    '111101',
    '011001',
    '101111'
]

a = '0DEC'
b = ''
for i in range(len(a)):
    b += bin(int(a[i], 16))[2:].zfill(4)

print(b)

i = 0
while i < len(b)-7:
    if b[i:i+6] in pattern:
        print(pattern.index(b[i:i+6]))
        i += 6
    else:
        i += 1

#############################################
#############################################



