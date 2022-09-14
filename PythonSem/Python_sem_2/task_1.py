nomber = input('enter a real number: ')
res_nomber = int(''.join(nomber[i] for i in range(len(nomber)) if (nomber[i] != '.' and nomber[i] != ',')))
sum = 0
while res_nomber > 0:
    sum += res_nomber % 10;
    res_nomber //= 10
print (sum)
