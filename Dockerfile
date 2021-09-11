# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /invest

# Copy project
COPY . /invest/

RUN pip3 install -r requirements.txt

EXPOSE 80
EXPOSE 443

CMD gunicorn invest.wsgi:application --bind 0.0.0.0:$PORT

