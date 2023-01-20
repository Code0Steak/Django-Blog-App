FROM python:3.9-alpine

WORKDIR /FirstProject 

RUN pip install --upgrade pip

COPY . /FirstProject

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]