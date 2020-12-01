#!/usr/bin/python3
import time


while True:
    sekunder_just_nu = time.time()

    local_time = time.ctime(sekunder_just_nu)
    print("Local time:", local_time)
    time.sleep(5)
