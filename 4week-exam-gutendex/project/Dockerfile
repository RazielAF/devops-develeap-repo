FROM python:3.8.14-alpine3.15
# RUN pip install --upgrade setuptools
# RUN pip install ez_setup
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add rsync
WORKDIR app
COPY . .
RUN pip install -r requirements.txt
RUN chmod 755 entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
# CMD tail -f /dev/null