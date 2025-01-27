import os
import time

# # os.getcwd()
# # # print(os.getcwd())
# # # for i in os.walk('.'):
# # #     print(i)
# # os.chdir(r'C:\Users\Евгения\PycharmProjects\homework 1.py')
# # # print(os.getcwd())
# # os.path.join('.')
# # # print(os.path.join(r'C:\Users\Евгения\PycharmProjects\homework 1.py'))
# # os.path.getatime('.')
# # # print(os.path.getatime(r'C:\Users\Евгения\PycharmProjects\homework 1.py'))
# # os.path.getsize('.')
# # # print(os.path.getsize(r'C:\Users\Евгения\PycharmProjects\homework 1.py'))
# os.path.dirname('.')
# print(os.path.dirname(r'C:\Users\Евгения\PycharmProjects\homework 1.py'))
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(r'C:\Users\Евгения\PycharmProjects\homework 1.py')
        # filepath = os.path.join('.')
        filetime = os.path.getatime('.')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize('.')
        parent_dir = os.path.dirname('.')
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
