FROM python:alpine
LABEL Maintainer="Jayesh"
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 9090
CMD ["python", "src/app.py"]
