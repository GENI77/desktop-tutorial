import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(int(password))
        self.age = int(age)


class Video:

    def __init__(self, title, duration, time_now, adult_mode):
        self.title = str(title)
        duration = time.struct_time
        self.duration = duration
        time_now = 0
        adult_mode = False


class UrTube:

    def __init__(self, users, videos, current_user):
        self.users = users[User]
        self.videos = videos[Video]
        current_user = User

    def __register__(self, nickname, password, age):
        nickname = input('Введите имя: ')
        password = input('Введите пароль: ')
        age = input('Укажите ваш возраст: ')
        self.nickname = nickname
        self.password = password
        self.age = age
        if nickname not in User:
            nickname = User
        else:
            print(f'Пользователь {nickname} уже существует')
            return




    # def __log_in__(self, nickname, password):
    #     login = nickname, password
    #     self.login = self.users
    #     if login == User:
    #         current_user = login


