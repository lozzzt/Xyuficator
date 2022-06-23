# Зарегистрировать бота

У `@BotFather` создать нового бота (`/newbot`), получить токен.
Токен вставить в config.yaml или передать в командной строке при запуске (предпочтительно)

# Установить зависимости:
```pip install -r requirements.txt```

# Подключить БД

### Скачивание, создание и запуск контейнера с mongoDB:
```sh
docker pull mongo  
docker container create mongo:latest  
docker container run -d -p 27017:27017 --name test-mongo mongo:latest  
```

# Запустить
```sudo python ./main.py```

# Запуск в виртуальной среде

```sh
mkdir -p /home/bots
python3 -m venv /home/bots
source /home/bots/bin/activate
pip install -r requirements.txt
python3 -m path/to/xyuinator_bot/main.py 'BOT_TOKEN'
```

# Описание бота

### Команды
+ `/start` - _запуск бота - задаётся вариант длины хуифицируемых предложений: 1_
+ `/set_message_length 1 2 3` - _Задать варианты длины хуифицируемых предложений в виде списка: 1 2 3_
+ `/stop` - _Выключить хуификатор - задаётся вариант длины хуифицируемых предложений: 0_
+ `/leave_chat` - _Убрать хуификатор из чата_

# Документация по API

### API Telegram:
https://core.telegram.org/api

### Библиотека aiogram:
https://docs.aiogram.dev/en/latest/

### Статьи с примерами aiogram:
https://surik00.gitbooks.io/aiogram-lessons/content/  
https://mastergroosha.github.io/telegram-tutorial-2/quickstart/  
