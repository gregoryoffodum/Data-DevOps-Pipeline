FROM python:3.9
LABEL "Author" "Wave Data Ops"
COPY requirements.txt requirements.txt
COPY question1.py question1.py
COPY question2.py question2.py
COPY weather_all.csv weather_all.csv
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "question1.py"]

