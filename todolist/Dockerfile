FROM python:3.12-slim

WORKDIR /todolist

COPY requirements.txt /todolist/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /todolist/

EXPOSE 8000

RUN ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
