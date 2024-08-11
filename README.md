## Install
Создайте виртуальное окружение в директории ```src``` и установите библиотеки из файла ```requirements.txt```

В корне проекта создайте файл ```.env```

```
DEBUG = False

DB_HOST = 'ip'
DB_PORT = 5432
DB_NAME = 'database name'
DB_USER = 'database user'
DB_PASSWORD = 'user password'

BOT_TOKEN = 'get token from bot father'
BOT_NAME = ''
BOT_SHORT_DESCRIPTION = ''
BOT_DESCRIPTION = ''

ADMIN_IDS = '["first admin id", "second admin id"]' 
SKIP_UPDATES = False

DROPBOX_TOKEN = ''
```

## @BotFather settings
В ```@BotFather``` настройте placeholder для ```Inline Mode```:

```Edit Bot``` > ```Edit inline placeholder``` 

и включите ```Inline Mode```:

```Bot Settings``` > ```Inline Mode``` > ```Turn inline mode on```

## Run
Для запуска воспользуйтесь командой ```python app.py```