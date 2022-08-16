FROM ubuntu
RUN apt-get update -y
RUN apt-get install -y python3-pip build-essential
ADD py py
RUN pip install -r py/requirements.txt
EXPOSE 8080
CMD ["/bin/bash","-c","python3 py/mailService.py"]
