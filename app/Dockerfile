FROM python:3.6.4-alpine3.7
RUN ["mkdir", "/code"]
ADD app.py /code/app.py
ADD requirements.txt /code/requirements.txt
ADD start.sh /code/
WORKDIR /code
RUN ["pip", "install", "-r", "requirements.txt"]
EXPOSE 5000
ENTRYPOINT ["/bin/sh"]
CMD ["-c", "./start.sh"]
