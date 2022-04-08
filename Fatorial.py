num = int(input("Digite o valor de n: "))
fat = 1
if((num == 0) or (num == 1)):
    print("1")
while (num>1):
    fat=num*fat
    num= num-1
print(fat)
    
