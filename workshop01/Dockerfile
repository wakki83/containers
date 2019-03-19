FROM node:latest

LABEL "name"="myapp"

ENV DB_HOST=mydb DB_PORT=3306 DB_USER=root DB_PASSWORD=changeit
ENV APP_DIR=/app APP_PORT=3000

RUN mkdir ${APP_DIR}
WORKDIR ${APP_DIR}

ADD package.json .
ADD package-lock.json .
RUN npm install

ADD config config
ADD public public
ADD views views
ADD main.js .

EXPOSE ${APP_PORT}

ENTRYPOINT ["node", "main.js"]