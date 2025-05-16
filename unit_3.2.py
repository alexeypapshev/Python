"""
Контекстный менеджер для управления транзакциями
Условие: Напишите контекстный менеджер для управления транзакциями в базе данных. 
Если во время выполнения блока with возникает исключение, транзакция должна откатываться, иначе — подтверждаться.
"""

class DBContextManager:
    def __init__(self, word: str):
        self.word = word

    def __enter__(self):
        print('Начало транзакции')
        if self.word == 'успешно':
            # print('Транзакция подтверждена')
            return self  # Возвращаем объект для использования в блоке with
        elif self.word == 'ошибка':
            # print('Транзакция откатана')
            raise ValueError("Транзакция откатана")  # Выдаём ошибку, если слово не успешно

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Пример использования
try:
    with DBContextManager(input()) as db_manager:
        print('Транзакция подтверждена')
except ValueError as e:
    print(e)


# ВАРИАНТ ПРЕПОДАВАТЕЛЯ
class TransactionManager:
    def __enter__(self):
        print("Начало транзакции")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Транзакция подтверждена")
        else:
            print("Транзакция откатана")
        # Вернем True, чтобы исключение не было выброшено дальше
        return True

operation = input()

with TransactionManager() as transaction:
    if operation == "ошибка":
        raise ValueError("Ошибка операции")