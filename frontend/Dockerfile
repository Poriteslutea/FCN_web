# First stage
FROM node:18.17.0 AS build

WORKDIR /app

COPY package*.json yarn.lock /app/

RUN yarn install

COPY . /app

RUN yarn build

# Second stage
FROM node:lts-alpine as deploy

WORKDIR /app

COPY --from=build /app/.output /app/.output

CMD ["node", ".output/server/index.mjs"]