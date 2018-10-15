#f = open('demo.txt','r')
#r = open('MyNewFile','a')
#for i in f:
#    r.write(i)

img=open("m.jpg" , 'rb')

img2=open("m2.jpg",'ab')

for i in img:
    img2.write(i)

