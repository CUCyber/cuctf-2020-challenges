FROM debian:jessie-slim

RUN apt-get update \
    && apt-get install -y socat \
    && apt-get clean -y

RUN useradd -d /home/challenge -m -p challenge -s /bin/bash challenge
RUN apt-get install python3 -y

WORKDIR /home/challenge

COPY pow.py .
COPY dr_xorisaurus .
COPY ld-2.32.so .
COPY libc.so.6 .
COPY flag.txt .

RUN chmod +x /home/challenge/pow.py
RUN chmod +x /home/challenge/dr_xorisaurus
RUN chmod +x /home/challenge/ld-2.32.so
RUN chmod +x /home/challenge/libc.so.6
RUN chmod 644 flag.txt

RUN chown -R root:root /home/challenge

USER challenge
CMD ["socat", "TCP-LISTEN:9200,reuseaddr,fork", "EXEC:/home/challenge/pow.py"]
