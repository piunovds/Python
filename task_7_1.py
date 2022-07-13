'''
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
'''
import os.path

proj_path = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for foler in folders:
    os.makedirs(os.path.join(os.curdir, proj_path, foler), exist_ok=True)
