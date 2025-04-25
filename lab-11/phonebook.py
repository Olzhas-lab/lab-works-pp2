import psycopg2

def connect():
    return psycopg2.connect(
        dbname="Tsk_2",
        user="postgres",
        password="KeyToLife",
        host="localhost",
        port="5432"
    )

# 1. Поиск по шаблону
def find_by_pattern():
    pattern = input("Введите шаблон (часть имени или номера): ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM find_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# 2. Вставка/обновление одного пользователя
def insert_or_update_user():
    name = input("Имя пользователя: ")
    phone = input("Телефон: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Готово.")

def connect():
    return psycopg2.connect(
        dbname="Tsk_2",  # Заменить на имя своей базы данных
        user="postgres",  # Заменить на имя пользователя
        password="KeyToLife",  # Заменить на свой пароль
        host="localhost",  # Или IP сервера
        port="5432",  # Порт по умолчанию для PostgreSQL
        options="-c client_encoding=utf8"
    )

# Процедура массовой вставки пользователей
def insert_users_batch():
    users = []
    count = int(input("Сколько пользователей добавить? "))
    for _ in range(count):
        name = input("Имя: ")
        phone = input("Телефон: ")
        # Формируем строку вида "имя,телефон" для каждого пользователя
        users.append(f"{name},{phone}")

    conn = connect()
    cur = conn.cursor()

    # Преобразуем список в массив для передачи в PostgreSQL
    users_for_db = users

    # Вызываем процедуру с массивом пользователей
    cur.execute("CALL insert_users(%s)", (users_for_db,))
    conn.commit()
    cur.close()
    conn.close()
    print("Готово. Проверяй консоль сервера на ошибки в номерах.")



# 4. Пагинация
def get_paginated():
    limit = int(input("Сколько записей показать? "))
    offset = int(input("С какой позиции начать? "))
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# 5. Удаление по имени или телефону
def delete_by_proc():
    val = input("Введите имя пользователя или номер телефона для удаления: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s)", (val,))
    conn.commit()
    cur.close()
    conn.close()
    print("Пользователь удален.")


# 🧭 Главное меню
def menu():
    while True:
        print("\n==== PhoneBook Pro Menu ====")
        print("1. Поиск по шаблону")
        print("2. Вставить/обновить пользователя")
        print("3. Массовая вставка пользователей")
        print("4. Получить записи с пагинацией")
        print("5. Удалить по имени/номеру")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            find_by_pattern()
        elif choice == "2":
            insert_or_update_user()
        elif choice == "3":
            insert_users_batch()
        elif choice == "4":
            get_paginated()
        elif choice == "5":
            delete_by_proc()
        elif choice == "0":
            print("До встречи!")
            break
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    menu()