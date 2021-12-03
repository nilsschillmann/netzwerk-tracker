FROM python:3.9.9

RUN mkdir tracker

COPY tracker.py ./tracker
COPY requirements.txt ./tracker

WORKDIR /tracker

RUN mkdir log

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "tracker.py" ]