FROM python:3.9
ADD . /code
WORKDIR /code
EXPOSE 5001
RUN pip install -r requirements.txt
CMD python server.py
