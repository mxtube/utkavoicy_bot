### Install

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

OPENDRIVE_USER = ''
OPENDRIVE_PASSWORD = ''
OPENDRIVE_PROJECT_DIRECTORY = ''
```

### @BotFather settings
В ```@BotFather``` настройте placeholder для ```Inline Mode```:

```Edit Bot``` > ```Edit inline placeholder``` 

и включите ```Inline Mode```:

```Bot Settings``` > ```Inline Mode``` > ```Turn inline mode on```

### OpenDrive
В качестве хостинга файлов используется сервис [OpenDrive](https://www.opendrive.com/personal) с открытым API 1.1.7, по документации нет метода получающего список директорий и файлов, в связи с этим необходимо получить ID директории проекта и установить в виртуальное окружение. Для работы с сервисом используется логин и пароль от учетной записи.

### Run
Для запуска воспользуйтесь командой ```python app.py```