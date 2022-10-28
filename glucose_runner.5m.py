#!/usr/bin/env python3

from pydexcom import Dexcom

# set ous to True if outside the US, otherwise False
dexcom = Dexcom("username/email", "password", ous = True)

# read and display the blood sugar value and trend arrow
bg = dexcom.get_current_glucose_reading()
print(f'{bg.value} {bg.trend_arrow}')