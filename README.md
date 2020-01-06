## Commands
### Flask
(venv) $ flask run

### DB
(venv) $ flask db migrate -m "name for migration"
(venv) $ flask db upgrade
(venv) $ flask db downgrade

### Translations
(venv) $ pybabel extract -F babel.cfg -k _l -o messages.pot .
(venv) $ pybabel update -i messages.pot -d app/translations