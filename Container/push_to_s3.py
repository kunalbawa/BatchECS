import boto3
import sys
import argparse
import time

client = boto3.client('s3')

if __name__ == "__main__":
    # if (len(sys.argv) >= 1 and sys.argv[1] == '-h') \
    #         or len(sys.argv) < 1:
    #     print "Script used to add a file to S3 with message." \
    #           "Example: " \
    #           "./push_to_s3.py <message>"

    filename = "log-%s.txt" % int(round(time.time() * 1000))
    file = open(filename, "w")
    file.write('TEST')
    file.close()

    client.upload_file(filename, 'batchprocesstest', filename)