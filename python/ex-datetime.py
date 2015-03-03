# -*- coding: utf-8 -*-
# Directive	Meaning Notes
# %a		Locale’s abbreviated weekday nameself.
# %A		Locale’s full weekday nameself.
# %b		Locale’s abbreviated month nameself.
# %B		Locale’s full month nameself.
# %c		Locale’s appropriate date and time representationself.
# %d		Day of the month as a decimal number [01,31]self.
# %f		Microsecond as a decimal number [0,999999], zero-padded on the left	(1)
# %H		Hour (24-hour clock) as a decimal number [00,23]self.
# %I		Hour (12-hour clock) as a decimal number [01,12]self.
# %j		Day of the year as a decimal number [001,366]self.
# %m		Month as a decimal number [01,12]self.
# %M		Minute as a decimal number [00,59]self.
# %p		Locale’s equivalent of either AM or PMself.(2)
# %S		Second as a decimal number [00,61]self.(3)
# %U		Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0self.(4)
# %w		Weekday as a decimal number [0(Sunday),6]self.
# %W		Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0self.(4)
# %x		Locale’s appropriate date representationself.
# %X		Locale’s appropriate time representationself.
# %y		Year without century as a decimal number [00,99]self.
# %Y		Year with century as a decimal numberself.
# %z		UTC offset in the form +HHMM or -HHMM (empty string if the the object is naive)self.(5)
# %Z		Time zone name (empty string if the object is naive)self.
# %%		A literal '%' character.

from datetime import datetime
import random

mystr = datetime.now().strftime("%Y%m%d-%H%M%S%f") + ":" \
        +  str(random.randint(1,100000))

print mystr
