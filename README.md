Install dependencies into requirements.txt
```bash
pip freeze > requirements.txt
```
now install dependencies
```bash
pip install -r requirements.txt
```
create app
```bash
./manage.py startapp products
```
create a superuser
```bash
./manage.py createsuperuser
```
