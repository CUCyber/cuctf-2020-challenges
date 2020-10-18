FROM golang:1.15-alpine

RUN apk update

RUN adduser -D challenge

RUN mkdir -p /var/www

COPY app /var/www
WORKDIR /var/www/

RUN go build -o server

EXPOSE 8080
USER challenge
CMD ["./server"]
