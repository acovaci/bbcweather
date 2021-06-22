import boto3
import time

session = boto3.Session()
client = session.client("timestream-write")

dimensions = [{
    "Name": "location_id",
    "Value": -1
}]

record = {
    "Dimensions": dimensions,
    "MeasureName": "temperature",
    "MeasureValue": str(-1),
    "MeasureValueType": "INT",
    "Time": str(int(round(time.time() * 1000)))
}

try:
    result = client.write_records(
        DatabaseName="bbcweather-db",
        TableName="test-temperature",
        Records=[record]
    )
except Exception as e:
    print(e)