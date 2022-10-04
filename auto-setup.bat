python setup.py install
python setup.py develop

touch config.prod.ini
touch config.dev.ini

touch token.txt

printf "[Telegram]\nTOKEN = " > config.prod.ini
printf "[Telegram]\nTOKEN = " > config.dev.ini
printf "This file is created in order to store your local TOKEN. The file is not visible for git." > token.txt