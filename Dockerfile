FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app

COPY ./main.py /app

RUN pip install -r requirements.txt

CMD ["sleep", "infinity"]
