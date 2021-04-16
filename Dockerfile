FROM python:3.9
COPY requirements.txt ./requirements.txt
COPY main.py ./main.py
RUN pip install -r requirements.txt
CMD ["python", "./app.py"]
