FROM python:3

WORKDIR /home/src
RUN pip install --no-cache-dir flask gunicorn

COPY . .
CMD ["gunicorn",  "--workers", "5", "--timeout", "2", "-b", "0.0.0.0:5000","app:app"]
EXPOSE 5000
