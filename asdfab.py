while True:
    try:
        n = int(input("Введите число: "))
        if n < 1:
            raise Exception()
        print("Сумма чисел от 1 до n: ", sum([i for i in range(1,n+1)]))
        break
    except Exception as e:
        print('Неверный формат')


# print('\nInvalid input, phone number can only contain number\'s!!!\n')