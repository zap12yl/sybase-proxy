FROM node:16-alpine as build
WORKDIR /app
COPY webapp/frontend/package*.json ./
RUN npm install
COPY webapp/frontend/ ./
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY webapp/frontend/nginx.conf /etc/nginx/conf.d/default.conf