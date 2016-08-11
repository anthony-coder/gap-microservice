FROM python
RUN pip install flask
RUN pip install docker-py
RUN curl https://get.docker.com | sh
COPY hello.py /home
EXPOSE 5000
CMD ["python", "/home/hello.py"]
