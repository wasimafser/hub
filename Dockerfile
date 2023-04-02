FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /hub
COPY requirements.txt /hub/
RUN pip install -r requirements.txt
COPY . /hub/
