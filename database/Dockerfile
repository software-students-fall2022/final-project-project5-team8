#base image
FROM python:3.9-bullseye

#set work directory insideimage
WORKDIR /database

# copy current dir contents into image dir
ADD . /database

#install requirments
RUN pip install --upgrade pip
RUN apt -y update
RUN pip install pymongo
ENV DATA_OP=database.py
COPY . .

EXPOSE 4000

#run app when container launches
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]