while True:

    height = int(input('Введите свой рост, см:  '))

    weight = int(input('Введите свой вес, кг:  '))

    total = weight/(height/100)**2

    print('Ваш индекс массы тела равен:  ' , \
          round(total, 1))

    if total < 16:
        print('У Вас ярко выраженный дефицит массы тела')

    elif total >= 16 and total < 18.5:
        print('У Вас дефицит массы тела')

    elif total >= 18.5 and total < 25:
        print('У Вас достаточный вес')

    elif total >= 25 and total < 30:
        print('У Вас предожирение')

    elif total >= 30 and total < 35:
        print('У Вас ожирение I степени')

    elif total >= 35 and total < 40:
        print('У Вас ожирение II степени')

    else:
        print('У Вас ожирение III степени')
        print (' ')
