FROM node:12-alpine
WORKDIR /frontend
COPY ./package.json .
COPY ./jsconfig.json .
RUN yarn install --save
COPY ./src /frontend/src
CMD ["yarn", "run", "dev"]