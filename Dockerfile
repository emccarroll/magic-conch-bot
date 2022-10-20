FROM python:3.10-slim-bullseye

LABEL app.maintainer="emccarroll"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py bot.py

CMD [ "python", "./bot.py" ]