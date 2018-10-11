l = ["raj ", "ajwlaiya", "jbspl", 98845, True]
for i in l:
    for j in range(1, 11):
        print(j, end="")
    print(" ", i)

# find i*i*i nummbers below 500

i = 0
for i in range(1, 10):
    j = 0
    j = i * i * i
    if j <= 500:
        print(str(i) + " :- " + str(j) + " ")
