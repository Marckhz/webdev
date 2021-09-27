FROM python:3.9.7-bullseye

RUN mkdir /myapp
COPY . /myapp
WORKDIR /myapp
RUN chmod +x /myapp/run.sh
RUN ls
RUN pip install --upgrade pip && pip install -r requirements.txt && pip check

CMD ["./run.sh"]