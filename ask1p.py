a = raw_input('Dose keimeno')
mikosa = len(a)
counter = mikosa-1
ex = 0
flag = True

while flag:
    if (a[counter] == '!'):
        ex = ex + 1
        counter = counter - 1
    else:
        flag = False;

end = (mikosa - ex)
a = a[:end]

print a.replace('!', ' ') + (ex)*'!'
