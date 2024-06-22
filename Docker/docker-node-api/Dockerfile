FROM node:latest

WORKDIR /app

COPY package*.json ./

# ensures packages exist before copying app code
RUN npm install

COPY . ./

EXPOSE 3000

CMD ["npm", "start"]
