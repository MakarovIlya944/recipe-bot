# icqbot
Recipe bot for telegram

# Init program

* Установить Python расширение для Visual Studio Code

* Создаем виртуальное окружения для питона
```sh
python -m venv venv  
```
* Устанавливаем сторонние библиотеки
```sh
pip install -r req.txt
```

# Парсить рецепты

```sh
python ./scrap.py
```

# Запустить бота

Вставить токен бота в ковычки
```py
TOKEN = ""
```

```sh
python ./recipebot.py
```

# Остановить бота

Ctrl+C в консоли
(можно много раз потыкать он не сразу стопается)