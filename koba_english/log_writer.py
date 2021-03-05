#!/usr/bin/env python3

import os
import datetime

def find_logfile():
    dir_name = "logfiles"

    if os.path.isdir(dir_name):
        write_log(dir_name)

    else:
        os.mkdri(dir_name)
        write_log(dir_name)

def write_log(dir_name):

    os.chdir(dir_name)
    file_name = "log.txt"

    date_day = str(datetime.datetime.today()) + "\n"

    with open(file_name, "a") as f:
        f.write(date_day)

