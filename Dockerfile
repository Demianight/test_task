FROM python:3.10-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN python3 manage.py collectstatic --no-input

CMD ["gunicorn", "foods.wsgi:application", "--bind", "0:8000"]