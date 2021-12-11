from influxdb import InfluxDBClient
from datetime import timedelta


class InfluxDBV1:
    def __init__(self,
                 host='localhost',
                 port=8086,
                 username='root',
                 password='root',
                 database='default'):
        self.batch_size = 1000
        self.batches = []
        self.client = InfluxDBClient(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database
        )

    def finish(self):
        if len(self.batches):
            self.client.write_points(self.batches, batch_size=self.batch_size)
        self.batches = []

    def insert(self, kv, table, tags, dt):
        self.batches.append({
            "measurement": table,
            "time": dt + timedelta(hours=-8),
            "tags": tags,
            "fields": kv
        })

        if len(self.batches) > self.batch_size:
            self.finish()
