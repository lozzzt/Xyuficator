# Зарегистрировать бота

У `@BotFather` создать нового бота (`/newbot`), получить токен.
Токен вставить в config.yaml

# Установить зависимости:
```pip install -r requirements.txt```

# Запустить
```sudo python ./main.py```

# Описание бота

### Команды
+ `/start` - _запуск бота_
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
