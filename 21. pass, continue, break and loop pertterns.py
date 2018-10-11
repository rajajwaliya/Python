for i in range(1,20):

    if i%9==0:
        break
    if i%2!=0:
        pass
        #continue
    else:
        print(i)

#Patterns
# 1234
# 234
# 34
# 4

i=0
for i in range(1,5):
    print()
    for j in range (i,5):
        print(j,end="")

i=0
for i in range(66,70):
    print()
    for j in range (i,5):
        print(str(j),end="")

#Patterns
# APQR
# ABQR
# ABCR
# ABCD

i=0
j=0
for i in range(0,4):
    for j in range(65,66+i):
        print(chr(j),end="")
    for k in range(80+i,83):
        print(chr(k),end="")
    print()