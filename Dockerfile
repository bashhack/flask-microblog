FROM python:3.8-slim-buster

RUN adduser --disabled-login microblog

ENV DEBIAN_FRONTEND noninteractive

# Python, don't write bytecode!
ENV PYTHONDONTWRITEBYTECODE 1

# -- Install Pipenv:
RUN apt-get update && apt-get install python3-dev libffi-dev gcc curl libenchant1c2a -y
RUN curl --silent https://bootstrap.pypa.io/get-pip.py | python3.8

RUN pip3 install pipenv

WORKDIR /home/microblog

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --deploy --system --dev
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R microblog:microblog ./
USER microblog

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
