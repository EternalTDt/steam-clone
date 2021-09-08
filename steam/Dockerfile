FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /steam
COPY requirements.txt /steam/
RUN pip install -r requirements.txt
COPY . /steam/