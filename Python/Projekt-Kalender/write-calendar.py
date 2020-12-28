#!/usr/bin/python3
import os
from datetime import datetime

date = datetime.now().day

calendar = os.popen('cal').read()
if date < 10:
    new_calendar = calendar.replace(f' {date} ', f'({date})')
else:
    new_calendar = calendar.replace(f'{date} ', f'({date})').replace(f' (', f'(')

open('/tmp/cal2.txt', 'w+').write(new_calendar)
