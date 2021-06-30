version: '3'

services:
  
  rabbitmq:
    image: 'rabbitmq:3.6-management-alpine'
    ports:
      - '5672:5672'
      - '15672:15672'

  server:
    build: server
    volumes:
      - ./server:/app
    ports:
      - 5000:5000