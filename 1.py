 #Задача 2: Найдите сумму цифр трехзначного числа.

print("Введите 3х значное число")
number= int(input())
if 99<number<1000:
    c= number%10
    number= number//10
    b= number%10
    a= number//10
    print(f'Сумма чисел введенного числа:{a+b+c}')
else:
    print('Вы ввели неверное число, введите трехзначное число')


