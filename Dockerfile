FROM python:3.8

COPY . .

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD ["python", "main.py"]