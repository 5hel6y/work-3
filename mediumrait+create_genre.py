import pickle
shows = {
    'Секретные материалы': {'Жанр': 'фантастика', 'Рейтинг': 0.9},
    'Ведьмак': {'Жанр': 'фэнтази', 'Рейтинг': 0.95},
    'Клан Сопрано': {'Жанр': 'криминал', 'Рейтинг': '0.8'},
    '24': {'Genre': 'драма', 'Rating': 0.75},
    'Черное зеркало': {'Жанр': 'фантастика', 'Рейтинг': 0.98},
    'Во все тяжкие': {'Жанр': 'криминал', 'Рейтинг': '0.85'},
    'Игра престолов': {'Жанр': 'фэнтази', 'Рейтинг': 0.87},
    'Карточный домик': {'Genre': 'драма', 'Rating': 0.82},
    'Рик и Морти': {'Жанр': 'фантастика', 'Рейтинг': 1}
        }

mediunrait = list()


def create_genre():
    #получает на вход от пользователя название жанра на выход получает закодированный файл с названиями сериалов
    #а в терминале выводит средний рейтинг количество сериалов и тот жанр который он выбрал
    created = input("Введите назнание жанра что бы получить подборку сериалов\n")
    for i in shows:
        try:
            b = list(shows[i].values())[0]
            c = list(shows[i].values())[1]
            if created == b:
             try:
                 with open(created, 'ab') as f:
                  new_file = dict()
                  new_file.setdefault(i)
                  for key, value in new_file.items():
                      pickle.dump(key, f)
             except:
              print('Ошибка работы с файлом')
             mediunrait.append(float(c))
             result = ((sum(mediunrait) / len(mediunrait)))
             mediunrait_2 = []
             mediunrait_2.append(result)
        except BaseException :
         print("что то пошло не так :)")
    print("Жанр который вы выбрали",created,'\nвсего сериалов',len(mediunrait), '\nсредняя оценка', mediunrait_2[-1])


create_genre()

