FROM python:3.12.5-alpine3.20

COPY src/requirements.txt /temp/requirements.txt

RUN pip install --prefer-binary -r /temp/requirements.txt

COPY src /opt/utkabot

WORKDIR /opt/utkabot

RUN adduser --disabled-password mxtube

RUN chown mxtube /opt/

USER mxtube

CMD ["python", "app.py"]

