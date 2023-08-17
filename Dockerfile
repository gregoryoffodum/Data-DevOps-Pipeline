FROM python:3.9
LABEL "author" "WaveHQ Data Ops"
COPY requirements.txt requirements.txt
RUN pip install -r reqirements.txt
ENTRYPOINT ["python", "question1.py"] 
