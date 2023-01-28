FROM python:3.7.3-slim

RUN mkdir /home/app
WORKDIR /home/app
COPY . .
ENV PATH="/home/app:${PATH}"
RUN chmod +x test run

CMD test
