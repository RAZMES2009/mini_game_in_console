import random
import json

#переменная для текущего рекорда
record = 0

#Открываем файд json для считывания рекорда
try:
    with open("record.json", "r") as read_file:
        #записали рекорд в old_record 
        old_record = json.load(read_file)

        #приветсвуем игрока и выводим рекорд за все время
        print("Добро пожаловать в игру 'камень, ножница, бумага' (для выхода из игры введите exit)")
        print("***Рекорд {}***".format(old_record))

#Если рекорда не было просто приветсвуем игрока и говорим что рекорд не установлен
except FileNotFoundError:

    print("Добро пожаловать в игру 'камень, ножница, бумага' (для выхода из игры введите exit)")
    print("***Рекорд 0***")
    old_record = 0

#Главная функция устанавливающая победителя
def main(player_choice, pc_choice):

    #используем глобальную record для записи текущего рекорда
    global record

    if player_choice == pc_choice:
        print ("Ничья!")

    elif player_choice == "камень" and pc_choice == "ножницы":
        print ("Игрок 1 победил!")  
        record += 1
    elif player_choice == "ножницы" and pc_choice == "бумага":
        print ("Игрок 1 победил!")
        record += 1
    elif player_choice == "бумага" and pc_choice == "камень":
        print ("Игрок 1 победил!")
        record += 1

    elif player_choice == "ножницы" and pc_choice == "камень":
        print ("Игрок 2 победил!")
        record -= 1
    elif player_choice == "бумага" and pc_choice == "ножницы":
        print ("Игрок 2 победил!")
        record -= 1
    elif player_choice == "камень" and pc_choice == "бумага":
        print ("Игрок 2 победил!")
        record -= 1
    #условие чтобы счёт не уходил в минус
    if record < 0:
        record = 0
    #вывод текущего и общего рекорда
    print("***{} уровень***".format(record))
    if old_record:
        print("***Рекорд за все время: {}***".format(old_record))

#функция для проверки ввода игроком
def action(player_choice, pc_choice):
    #если ок показываем выбор игрока и соперика и вызываем функцию main для установления победителя
    if player_choice == 'камень' or player_choice == 'ножницы' or player_choice == 'бумага':

        print("\nИгрок 1: {} --- Игрок 2: {}".format(player_choice, pc_choice))

        main(player_choice, pc_choice)
    #иначе просим ввести заново
    else:
        print("Неккоректный ввод, попробуйте снова")

#бесконечный цикл игры
while True:
    #запрос у игрока хода и рандомный выбор компьютера
    player_choice = input("\nВыберите: ")
    pc_choice= random.choice(['камень', 'ножницы', 'бумага'])
    #Если пользователь введет exit сохранение рекорда если он больше прошлого и выход из игры
    if player_choice == 'exit':
        if record > old_record:
            with open("record.json", "w") as write_file:
                json.dump(record, write_file)
        break
    #для корректной работы ввод пользователя переводим в нижний регистр
    player_choice = player_choice.lower()
    #вызов основной проверки победителя
    action(player_choice, pc_choice)