#base image
FROM python:3.9-bullseye

#set work directory insideimage
WORKDIR /web_app

# copy current dir contents into image dir
ADD . /web_app

#install requirments
RUN pip install --upgrade pip
RUN apt -y update
RUN apt-get install -y portaudio19-dev
RUN apt-get install -y libleptonica-dev tesseract-ocr libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
RUN apt-get install -y flac
RUN pip install -r requirements.txt
ENV FLASK_APP=controller.py

#listen to 5000 on at runtime
EXPOSE 5000

#run app when container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]