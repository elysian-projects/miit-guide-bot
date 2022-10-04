python setup.py install
python setup.py develop

touch config.prod.ini
touch config.dev.ini

printf "[Telegram]\nTOKEN = " > config.prod.ini
printf "[Telegram]\nTOKEN = " > config.dev.ini
