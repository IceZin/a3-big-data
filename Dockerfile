FROM python:3.10-alpine

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY app /app

CMD ["python3", "app/main.py"]