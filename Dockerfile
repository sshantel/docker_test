FROM python:3.8

ADD test_main.py .

RUN pip install unittest

CMD ["python", "./test_main.py"]