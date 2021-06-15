FROM python:3.9

RUN mkdir /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
WORKDIR /code
CMD gunicorn bbbs.wsgi:application --bind 0.0.0.0:8000