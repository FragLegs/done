# -*- coding: utf-8 -*-
import os
import subprocess
import sys

import done_sns.sns

def done():
    # get the command
    cmd = sys.argv[1:]

    # get the topic for this SNS feed
    arn = os.environ['DONE_ARN']

    # the subject is the text of the command
    subject = ' '.join(cmd)

    # run the command and capture the output
    output = []
    p = subprocess.Popen(cmd,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)

    # pretend we are using `tee` so that the user can see the output and
    # we can email it to them
    for line in iter(p.stdout.readline, ''):
        print(line)
        output.append(line)

    sns.publish(arn, subject, '\n'.join(output))


if __name__ == '__main__':
    done()
