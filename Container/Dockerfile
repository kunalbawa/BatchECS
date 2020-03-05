FROM python:latest
RUN pip install awscli boto3
RUN mkdir app
COPY push_to_s3.py /app
WORKDIR /app
CMD python ./push_to_s3.py