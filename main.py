from generate_password import generate_password
from save_password import save_password
from encryption_utils import generate_key, save_key, load_key


def main():
    # Генерация и сохранение ключа шифрования, если он еще не создан
    try:
        key = load_key()
    except FileNotFoundError:
        key = generate_key()
        save_key(key)

    # Генерация пароля
    password = generate_password(length=15)
    print(f'Сгенерированный пароль: {password}')

    # Сохранение пароля
    save_password(password, key=key)
    print('Пароль успешно сохранен и зашифрован.')


if __name__ == '__main__':
    main()
