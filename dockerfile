FROM node:alpine

RUN npm install -g nodemon

WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["node", "server.js"]