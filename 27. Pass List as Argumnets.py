def evenodd(ls):
    even=0
    odd=0
    for i in ls:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    return even,odd

ls=[10,34,55,77,99,34,50,89,55,33]

even,odd=evenodd(ls)

print("even nums is : {} \nOdd num is : {} ".format(even,odd))