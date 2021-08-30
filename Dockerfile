FROM python:3.7

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
