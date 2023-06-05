1.  create virtual environment: `py -m venv venv`
2. activate virtual env: `./venv/Scripts/activate`
3. install requirements: `pip install -r requirements.txt`
4. make migrations :
```
    python pickleclicker/manage.py makemigrations
    python pickleclicker/manage.py makemigrations backend
    python pickleclicker/manage.py migrate
```
5. run server: `python pickleclicker/manage.py runserver`