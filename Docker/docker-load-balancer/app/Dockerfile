FROM node

WORKDIR /usr/src/app

RUN npm init -y

RUN npm install express

COPY server.js .

CMD ["node", "server.js"]
