FROM python:3.8
WORKDIR /home/hse-SE-course
RUN apt-get update && apt-get install git -y
RUN git clone https://github.com/bagryanova/hse-SE-course .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./app /app
EXPOSE 8000
CMD [ "uvicorn", "app.main:app" , "--reload", "--host=0.0.0.0"]
