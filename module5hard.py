import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = User

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f"Пользователь {nickname} уже существует")

    def add(self, video, *other):
        other = []
        video = [v1.title, v1.duration, v1.adult_mode]
        self.videos = video
        self.other = other
        if self.videos is not self.other:
            self.videos += self.other
        else:
            if self.videos in self.other:
                return self.videos

    def log_in(self, nickname, password):
        login = nickname, hash(password)
        login = self.users
        if login in self.users:
            self.current_user = login


u1 = User('genj', 2710,46)
print(u1.nickname, u1.password, u1.age)
ur = UrTube('genj', Video, 'vera')
print(ur.users, ur.videos, ur.current_user)
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
print(ur.add(v1, v2))
# Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')
