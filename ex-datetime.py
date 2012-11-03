from datetime import datetime
import random

mystr = datetime.now().strftime("%Y%m%d-%H%M%S%f") + ":" \
        +  str(random.randint(1,100000))

print mystr
