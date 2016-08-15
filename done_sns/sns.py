# -*- coding: utf-8 -*-
"""
Blatantly stolen from
https://github.com/BashtonLtd/sns-pipe/blob/master/snspipe/__init__.py

I feel no shame (ok, maybe a little)
"""
import collections
import json
import sys

import boto3

EXIT_STATUS_SUCCESS = 0
EXIT_STATUS_INCORRECT_USAGE = 3
EXIT_STATUS_INVALID_ARGUMENT = 4
EXIT_STATUS_BAD_RESPONSE = 5
EXIT_STATUS_TESTS_FAILED = 6


ARN = collections.namedtuple(
    typename='ARN',
    field_names='arn partition service region account resource',
)


def parse_arn(arn):
    fields = arn.split(':')
    try:
        return ARN(*fields)
    except Exception:
        raise ValueError(
            'ARNs must be in the format ' + ':'.join(ARN._fields)
        )


def publish(topic_arn, subject, body):

    region_name = parse_arn(topic_arn).region

    sns = boto3.resource('sns', region_name=region_name)
    topic = sns.Topic(topic_arn)

    response = topic.publish(
        Subject=subject,
        Message=body,
    )

    http_status_code = response.get('ResponseMetadata', {}).get('HTTPStatusCode')
    message_id = response.get('MessageId')
    response_ok = bool(http_status_code == 200 and message_id)

    try:
        response_str = json.dumps(response, indent=2)
    except Exception:
        response_ok = False
        response_str = repr(response)

    if response_ok:
        sys.stdout.write(response_str)
        sys.stdout.write('\n')
    else:
        sys.stderr.write(response_str)
        sys.stderr.write('\n')
        sys.exit(EXIT_STATUS_BAD_RESPONSE)
