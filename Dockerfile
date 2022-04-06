FROM python:3.9

COPY . .

RUN pip install -r requirements.txt
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "nano"]

# By default, dagit listens on port 3000, so it needs to be exposed
EXPOSE 3000