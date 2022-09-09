# csv_processor

## Задача
Написать сервис на Python, который имеет 3 REST ендпоинта:
* получает по HTTP имя CSV-файла (пример файла во вложении) в хранилище и
суммирует каждый 10й столбец
* показывает количество задач на вычисление, которые на текущий момент в работе
* принимает ID задачи из п.1 и отображает результат в JSON-формате
Сервис должен поддерживать обработку нескольких задач от одного клиента
одновременно.  
Сервис должен иметь возможность горизонтально масштабироваться и загружать
данные из AWS S3 и/или с локального диска.  
Количество строк в csv может достигать 3*10^6.  
Подключение к хранилищу может работать нестабильно.  

## Запуск
Необходимо настроить переменные окружения для docker-compose.yml
```
  - CELERY_BROKER_URL=redis://redis:6379/0
  - CELERY_RESULT_BACKEND=redis://redis:6379/0
  
  - PATH_TO_LOCAL_FILES=/usr/src/storage
  
  - USE_S3_STORAGE=False
  - S3_BUCKET='bucket_name'
  - S3_KMS_KEY_ID='kms-key-id'
```
```
PATH_TO_LOCAL_FILES=/path/to/local/files docker-compose up -d --build
```

## Доступные ендпоинты (порт: 8004)
- `/docs` - Интерактивная API Документация
- `/api/file/sum-every/{delta}/columns?filename={filename}` - Добавление задачи по подсчету в csv файле каждого `delta` столбца
- `/api/tasks` - Получение количества активных задач
- `/api/tasks/{task_id}` - Получение статуса задачи. Содержит результат, если задача выполнена.

Также доступен дашборд для мониторинга очереди задач (порт: 5556) 