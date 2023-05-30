import os

# 执行 makemigrations 命令
os.system("python manage.py makemigrations")

# 执行 migrate 命令
os.system("python manage.py migrate")
