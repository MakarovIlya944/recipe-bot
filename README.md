# icqbot
Recipe bot for icqnew

# Init program

* Установить Python расширение для Visual Studio Code

* Создаем виртуальное окружения для питона
```sh
python -m venv venv  
```
* Закрываем консоль на корзинку  
* Открываем консоль Ctrl+Shift+~  
* Устанавливаем сторонние библиотеки
```sh
pip install -r req.txt
```

# Парсить рецепты

```sh
python ./shef.py
```

# Запустить бота

Вставить токен бота в ковычки
```py
TOKEN = ""
```

```sh
python ./main.py
```

# Остановить бота

Ctrl+C в консоли
(можно много раз потыкать он не сразу стопается)