FROM python
MAINTAINER rwlaub
RUN pip install flask
RUN pip install docker-py
RUN pip install flask-script
RUN curl https://get.docker.com | sh
COPY hello.py /home
EXPOSE 5000
CMD ["python", "/home/hello.py", "runserver", "--threaded", "--host", "0.0.0.0"]
