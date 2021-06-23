import boto3
import time



class TemperatureLogger:
    def __init__(self, table_name: str, location_id: int):
        self.table_name = table_name
        self.location_id = location_id
        self._session = boto3.Session()
        self._client = self._session.client("timestream-write", region_name="eu-west-1")
    

    def log_temperature(self, temperature: int):
        record = self._generate_record_from_temperature(temperature)

        try:
            result = self._client.write_records(
                DatabaseName="bbcweather-db",
                TableName=self.table_name,
                Records=[record]
            )
        except Exception as e:
            print(e)

    
    def _get_dimensions(self) -> list:
        return [{
            "Name": "location_id",
            "Value": str(self.location_id)
        }]

    
    def _generate_record_from_temperature(self, temperature: int) -> dict:
        dimensions = self._get_dimensions()

        return {
            "Dimensions": dimensions,
            "MeasureName": "temperature",
            "MeasureValue": str(temperature),
            "MeasureValueType": "BIGINT",
            "Time": str(TemperatureLogger._get_timestamp())
        }
    

    @staticmethod
    def _get_timestamp() -> int:
        return int(round(time.time() * 1000))



if __name__ == "__main__":
    temp_logger = TemperatureLogger("test-temperature", 10)
    temp_logger.log_temperature(100)