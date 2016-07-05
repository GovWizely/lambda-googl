# Lambda Googl

This project provides a simple AWS Lambda around [Google's URL Shortener service](https://developers.google.com/url-shortener/) 
at [goo.gl](goo.gl). It has a retry mechanism to 
work around goo.gl's rate limiting. The idea is to call this Lambda, probably via an AWS API Gateway, instead of goo.gl when you want a
shortened URL and would rather wait a bit for an answer than get an error message about exceeding rate limits.

## Prerequisites

Follow instructions from [python-lambda](https://github.com/nficano/python-lambda) to ensure your basic development environment is ready,
including:

* Python
* Pip
* Virtualenv
* Virtualenvwrapper
* AWS credentials

Then make sure you have your [Google API Key](https://developers.google.com/url-shortener/v1/getting_started#APIKey) handy.

## Getting Started

	git clone git@github.com:loren/lambda-googl.git
	cd lambda-googl
	mkvirtualenv -r requirements.txt lambda-googl

## Configuration

* Edit `service.py` and change the GOOGL_API_KEY to use your key
* Define AWS credentials in either `config.yaml` or in the [default] section of ~/.aws/credentials.
* Edit `event.json` if you want to change the test value for the URL
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the API key or AWS credentials to version control

## Invocation

	lambda invoke -v

{u'kind': u'urlshortener#url', u'id': u'http://goo.gl/fbsS', u'longUrl': u'http://www.google.com/'}
 
## Deploy

	lambda deploy
