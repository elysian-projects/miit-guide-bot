python setup.py install
python setup.py develop

touch config.prod.ini
touch config.dev.ini

touch token.txt

printf "[Telegram]\nTOKEN = " > config.prod.ini
printf "[Telegram]\nTOKEN = " > config.dev.ini
printf "В этом файле можно хранить тестовый токен бота. Файл не учитывается токеном" > token.txt