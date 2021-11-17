txt = input('enter anumber:').split(',')
a,l, u, p, d = 0, 0, 0, 0,0
if len(txt)>=6 and len(txt)<=12:
    for i in txt:
        if (i.islower()):
            l += 1
        if (i.isalpha()):
            a += 1
        if (i.isupper()):
            u += 1

        if (i.isdigit()):
            d += 1

        if (i == '@' or i == '$' or i == '#'):
            p += 1

if l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(txt):

    print("Valid Password",txt )

else:
    print("Invalid Password")






