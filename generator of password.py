import string
import random
#составляем список символом
characters = list(string.ascii_letters + string.digits + "`~!@#$%^&*(){}[]:;\|?/,.<>-_=+"
def generate_random_password():
	#просим указать длину пароля
	length = int(input("Длина требуемого пароля: "))
	#перемешиваем символы
	random.shuffle(characters)
	#сохраняем пароль
	password = []
	for i in range(length):
		password.append(random.choice(characters))
	#подготавливаем результат
	random.shuffle(password)
	#конвертируем в иной формат
	#выводим пароль
	print("".join(password))
#запускаем
generate_random_password()
