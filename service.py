# -*- coding: utf-8 -*-

import googl
from retrying import retry

GOOGL_API_KEY='YOUR_KEY_HERE'

@retry(stop_max_attempt_number=5,wait_fixed=30000)
def retryable_shorten(client, url):
    return client.shorten(url)

def handler(event, context):
    return retryable_shorten(googl.Googl(GOOGL_API_KEY), event.get('url'))
