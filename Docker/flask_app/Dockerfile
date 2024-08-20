#Python base image
FROM python:3.10-slim 

#Set the working directory inside the container
WORKDIR /app

#Copy the requirements.txt file from host and install the dependencies
COPY /app/requirements.txt .
RUN pip install -r requirements.txt

#Copy the application code
COPY app/ .

#Expose the port the app runs on
EXPOSE 5000

#Start the app (Entry point)
CMD [ "python3","main.py" ]

