FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=0
RUN apk --update add gcc build-base vim
RUN pip install --no-cache-dir kubernetes slackclient
ADD py-operator.py /
ADD slackbot.py /
CMD python -u /py-operator.py
