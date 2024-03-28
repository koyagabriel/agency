import csv, os
import logging
from balance_manager.models import Agency, Consumer, Balance
from django import conf

import boto3
from botocore.exceptions import ClientError


class IngestionService:
    def __init__(self, object_name, agency_id):
        self.__aws_access_key_id = conf.settings.AWS_ACCESS_KEY_ID
        self.__aws_secret_access_key = conf.settings.AWS_SECRET_ACCESS_KEY
        self.bucket_name = conf.settings.AWS_BUCKET_NAME
        self.object_name = object_name
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=self.__aws_access_key_id,
            aws_secret_access_key=self.__aws_secret_access_key
        )
        self.agency_id = agency_id

    def download_file(self):
        local_filename = f"tmp/{self.object_name}"
        try:
            self.s3_client.download_file(self.bucket_name, self.object_name, local_filename)
        except ClientError as e:
            logging.error(e)
            return None
        return local_filename

    def save_to_database(self, data):
        reference_no = data[0]
        balance = data[1]
        balance_statuses = {i: i for i in conf.settings.BALANCE_STATUS}
        status = balance_statuses.get(data[2].upper())
        consumer_name = data[3].lower().strip()
        consumer_address = data[4]
        ssn = data[5].strip()

        agency = Agency.objects.filter(pk=self.agency_id).first()
        consumer = Consumer.objects.create_consumer(consumer_name, ssn, consumer_address, agency)
        Balance.objects.create(amount=float(balance), status=status, consumer=consumer, reference_no=reference_no)

    def upload_data_to_db(self):
        local_filename = self.download_file()

        if local_filename is None:
            return False

        with open(local_filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader, None)
            for row in csv_reader:
                self.save_to_database(row)

        os.remove(local_filename)
