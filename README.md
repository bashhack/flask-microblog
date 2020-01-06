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

#### NOTE: Using the custom `translate` CLI
(venv) $ flask translate --help
(venv) $ flask translate init
(venv) $ flask translate update
(venv) $ flask translate compile
