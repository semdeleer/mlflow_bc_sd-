FROM python:3.8
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /opt/
WORKDIR /opt
EXPOSE 5000
CMD mlflow ui --host=0.0.0.0 --port=5000
