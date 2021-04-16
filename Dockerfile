FROM python:3.9
COPY requirements.txt /usr/app/
COPY app.py /usr/app/
COPY ./templates /usr/app/
COPY ./static  /usr/app/
WORKDIR /usr/app
RUN pip install -r requirements.txt
CMD ["python", "./app.py"]
