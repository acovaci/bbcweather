import boto3
import time

session = boto3.Session()
client = session.client("timestream-write", region_name="eu-west-1")

dimensions = [{
    "Name": "location_id",
    "Value": str(-1)
}]

record = {
    "Dimensions": dimensions,
    "MeasureName": "temperature",
    "MeasureValue": str(-1),
    "MeasureValueType": "BIGINT",
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