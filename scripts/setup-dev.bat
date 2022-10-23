pip install -r requirements_dev.txt

python setup.py install
python setup.py develop

touch config.dev.ini

printf "[Telegram]\nTOKEN = " > config.dev.ini
