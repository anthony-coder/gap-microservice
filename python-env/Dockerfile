# This dockerfile load the dependencies for flask to run and launch containers
# in a threaded manner. It also takes in the hello.py app and is configured
# to run it
FROM python
RUN pip install flask
RUN pip install docker-py
RUN pip install flask-script
RUN curl https://get.docker.com | sh
COPY hello.py /home
EXPOSE 5000
CMD ["python", "/home/hello.py", "runserver", "--threaded", "--host", "0.0.0.0"]
