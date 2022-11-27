# MIIT Guide Bot

Telegram бот, который проводит экскурсию по территории университета РУТ (МИИТ).

## Цели проекта
- познакомить студентов и гостей ВУЗа с историей РУТ (МИИТ)

## Задачи
- [x] собрать, обработать и структурировать тектовую и графическую информацию о памятниках, находящихся на территории ВУЗа
- [x] создать логику взаимодействия с пользователем
- [x] разработать систему отображения информации о памятниках пользователю


## Запуск

Требуемая версия python - `python >= 3.10`.

Нужно скачать исходный код проекта, после чего запустить скрипт `/scripts/setup-dev.bat` от имени администратора.

После этого необходимо вставить токен бота (создать и посмотреть в боте `BotFather` в `Telegram`) после `=` в файле `config.dev.ini` (без кавычек).

Для запуска бота необходимо запустить команду:
```bash
bot
```

## TODO:
- [x] добавить ссылки на источники с дополнительной информацией
- [x] отредактировать тексты, сократить информацию
- [x] добавить фотографии мест
- [ ] подключить базу данных, настроить взаимодействие с ней
