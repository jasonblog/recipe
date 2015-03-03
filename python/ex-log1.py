

import logging
plog = logging.getLogger('myapp')
pfile = logging.FileHandler('foo.log')
pfmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
pfile.setFormatter(pfmt)
plog.addHandler(pfile)
plog.setLevel(logging.WARNING)

plog.error('Show error')
plog.warn('Show warning')
plog.info('Show info')
