FROM python:3
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "app.py", "0.0.0.0:5000"]
