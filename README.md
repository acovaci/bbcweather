# bbcweather
This repo contains an AWS Lambda function handler that scrapes the temperature from the BBC Weather website and logs it into Amazon Timestream.

## Files

The code inside `src/` is deployed to AWS Lambda. The function is set through CloudWatch to run every hour. Inside this folder there are three files:
1. `lambda_function.py` is called by the AWS Lambda service
2. `bbc_weather_scraper.py` handles the web scraping and extracting the temperature
3. `temperature_logger.py` connects to Amazon Timestream and logs the temperature

Finally, inside `tests/` you can find unit tests for the scraper. Ideally should've written some for the logger as well, but it's 2am :)

## System architecture

![System architecture diagram](https://user-images.githubusercontent.com/6562353/123092519-77ded180-d422-11eb-9aaf-946d263f6a36.png)
