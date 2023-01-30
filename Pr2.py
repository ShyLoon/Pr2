import array as arr
months = arr.array('h', [31, 31, 31, 31, 31, 31, 31, 30, 30, 30, 30])

x = int(input("Введите год: "))

if(x > 0):
    if (x%4==0 and x%100!=0):
        february = 29
    else: february = 28
months.append(february)
def summa(month):
    i = 1
    month += 1
    itog = 0
    for i in range(month):
        if (month < 10):
            itog += i
        else: itog += (i // 10) + (i % 10)
    return itog
    
i = 0
itog = 0
for i in range(len(months)):
    itog += summa(months[i])
    


print(itog)









    
