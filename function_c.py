
shows = {'Секретные материалы': 'фантастика',
         'Ведьмак': 'фэнтази',
         'Клан Сопрано': 'криминал',
         '24': 'драма',
         'Черное зеркало': 'фантастика',
         'Во все тяжкие': 'криминал',
         'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма',
         'Рик и Морти': 'фантастика'
         }
ratings = {'Секретные материалы': 0.9,
           'Ведьмак': 0.95,
           'Клан Сопрано': 0.8,
           '24': 0.75,
           'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85,
           'Игра престолов': 0.87,
           'Карточный домик': 0.82,
           'Рик и Морти': 1
           }
list = []


def medium_raiting():
    print("Введите названия сериалов из списка для расчета среднего райтинга\n Секретные материалы\n Ведьмак\n Клан Сопрано\n 24\n Ченрное зеркало\n Во все тяжкие\n Игра престолов \nКарточный домик \nРик и Морти")
    while True:
        series = ratings.get(input())
        if series != ratings.get(""):
            list.append(series)
        else:
            print(sum(list) / len(list))
            break


def compilation():
    # the program takes as input data from the user about the genre
    # that he wants to watch and returns him the names of the series
    while True:
        error = "Введите жанр сериала из списка \nфантастика \nкриминал \nфэнтази \nдрама\n"
        print(error)
        try:
            user_input_genre = input()
            keys = [key for key in shows if shows[key] == user_input_genre]
            print("вот сериалы из выбранного жанра", keys)
        except BaseException:
            print(error)

