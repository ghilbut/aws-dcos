FROM node:8.11.1-slim

EXPOSE 3000

COPY . /usr/share/mynode
WORKDIR /usr/share/mynode

RUN npm config set package-lock false
RUN npm install

ENTRYPOINT [ "node", "." ]
