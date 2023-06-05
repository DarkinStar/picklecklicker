1.  create virtual environment: `virtualenv venv --python=3.8`
2. activate virtual env: `source venv/bin/activate`
3. install requirements: `pip install -r requirements.txt`
4. make migrations :
```
    python pickleclicker/manage.py makemigrations
    python pickleclicker/manage.py makemigrations backend
    python pickleclicker/manage.py migrate
```
5. run server: `python pickleclicker/manage.py runserver`