FROM python:3.9-slim-buster

ADD requeriments.txt requeriments.txt
RUN pip install -r requeriments.txt

COPY reports.py reports.py
COPY queries.py queries.py


CMD [ "python","-u","reports.py" ]