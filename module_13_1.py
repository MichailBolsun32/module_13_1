import asyncio

#Необходимо сделать имитацию соревнований по поднятию шаров Атласа.
# Напишите асинхронную функцию start_strongman(name, power),
# где name - имя силача, power - его подъёмная мощность.
# Реализуйте следующую логику в функции:
#
#     В начале работы должна выводиться строка -
#     'Силач <имя силача> начал соревнования.'
#     После должна выводиться строка -
#     'Силач <имя силача> поднял <номер шара>' с задержкой обратно пропорциональной его силе power.
#     Для каждого участника количество шаров одинаковое - 5.
#     В конце поднятия всех шаров должна выводится строка
#     'Силач <имя силача> закончил соревнования.'

async def start_strongman(name, power):
    delay = 1 / power
    print(f'Силач {name} начал соревнования')
    for _ in range(5):
        await asyncio.sleep(delay)
        print(f" 'Силач {name} поднял {_ + 1} шар")

    print(f'Силач {name} закончил соревнования.')


#Также напишите асинхронную функцию start_tournament,
# в которой создаются 3 задачи для функций start_strongman.
# Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
#После поставьте каждую задачу в ожидание (await).

async def start_tournament():
    names = ['Pasha', 'Denis', 'Apollon']
    powers = [5, 4, 3]

    tasks = [asyncio.create_task(start_strongman(name, power))
                for name, power in zip(names, powers)]

    await asyncio.gather(*tasks)
    
#Запустите асинхронную функцию start_tournament методом run.
asyncio.run(start_tournament())
