shows = {
    'Секретные материалы': 'фантастика',
    'Ведьмак': 'фэнтази',
    'Клан Сопрано': 'криминал',
    '24': 'драма',
    'Черное зеркало': 'фантастика',
    'Во все тяжкие': 'криминал',
    'Игра престолов': 'фэнтази',
    'Карточный домик': 'драма',
    'Рик и Морти': 'фантастика'
}


result = ({k for k, v in shows.items() if v == 'фантастика' or v == 'фэнтази'})
# print(list({k for k, v in shows.items() if v == 'фантастика' or v == 'фэнтази'}))
result_1 = [i for i in result] # по заданию надо было использовать list comprehension но выше можно решить это изначально выведя результат List это было бы логичнее в рамках обучения функциональности
print(result_1)
