#FROM gcr.io/deeplearning-platform-release/tf2-cpu.2-0
#
#WORKDIR /root
#
#RUN pip install pandas numpy google-cloud-storage scikit-learn opencv-python
#RUN apt-get update; apt-get install git -y; apt-get install -y libgl1-mesa-dev
#
#ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
#RUN git clone https://github.com/sergiovirahonda/AutomaticTraining-Dataset.git
#ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
#RUN git clone https://github.com/sergiovirahonda/AutomaticTraining-CodeCommit.git
#
#RUN mv /root/AutomaticTraining-CodeCommit/model_assembly.py /root
#RUN mv /root/AutomaticTraining-CodeCommit/task.py /root
#RUN mv /root/AutomaticTraining-CodeCommit/data_utils.py /root
#RUN mv /root/AutomaticTraining-CodeCommit/email_notifications.py /root
#
#ENTRYPOINT ["python","task.py"]
FROM python:3.9-slim
RUN mkdir /app
WORKDIR /app

RUN pip install pandas numpy google-cloud-storage scikit-learn opencv-python

COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python" , "app.py"]