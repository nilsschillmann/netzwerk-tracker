FROM python:3.9.9

COPY tracker.py ./
COPY auswertung.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./tracker.py" ]