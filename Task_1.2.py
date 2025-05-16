# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

our_seconds = int(input('Введите пожалуйста время в секундах: '))

# секунды
seconds = our_seconds % 60
our_seconds = our_seconds - seconds
# часы
hours = our_seconds // 3600
our_seconds = our_seconds - (hours * 3600)
# минуты
minutes = our_seconds // 60


print(f'{hours}:{minutes}:{seconds}')
