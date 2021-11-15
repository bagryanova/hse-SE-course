FROM python:3.8
WORKDIR /home/hse-SE-course
RUN apt-get update && apt-get install git -y
RUN git clone https://github.com/bagryanova/hse-SE-course .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m pip install fastapi[all]
COPY ./app /app
CMD ["python3", "-m", "pytest", "tests/unit_tests.py"]
