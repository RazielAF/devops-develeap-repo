# FROM alpine:3.15 as build
# WORKDIR project
# RUN apk add npm
# COPY ./flask-app flask-app
# RUN if [ ! -d project/flask-app/node_modules ]; then npm install --prefix flask-app; else echo "skip install"; fi
# RUN npm run build --prefix flask-app

FROM alpine:3.15 as run
WORKDIR project
RUN apk add --update --no-cache python2 && ln -sf python2 /usr/bin/python
RUN python -m ensurepip
# COPY --from=build /project/flask-app flask-app
COPY ./flask-app/app.py ./flask-app/app.py
COPY ./flask-app/requirements.txt ./flask-app/requirements.txt
COPY ./utils utils
RUN pip install -r flask-app/requirements.txt 
ENTRYPOINT ["python", "flask-app/app.py"]



