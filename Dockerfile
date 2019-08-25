FROM python:3.7-alpine3.9

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
ADD . /opt/app
WORKDIR /opt/app

RUN pip install -r requirments.txt
CMD ["python", "main.py"]