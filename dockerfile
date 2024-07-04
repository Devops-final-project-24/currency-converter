FROM node:alpine

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# Set API_KEY environment variable
ARG API_KEY
ENV API_KEY=${API_KEY}
CMD ["npm", "start"]