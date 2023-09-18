open_new_day = open('dairy.txt.', 'a')
print('Здравствуйте это ваш личный дневник пожалуйста введите дату и событие которое вы хотите записать')
open_new_day.write('\n')
open_new_day.write(input())
past_entries = open('dairy.txt.', 'r')
print(past_entries.read())
past_entries.close()

