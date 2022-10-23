pip install -r requirements.txt

python setup.py install
python setup.py develop

touch config.prod.ini

printf "[Telegram]\nTOKEN = " > config.prod.ini
