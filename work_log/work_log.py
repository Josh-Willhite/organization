#!/usr/bin/env python
import sys
import logging
from datetime import date

today = date.today()

logging.basicConfig(format='%(asctime)s %(message)s', filename='{}'.format(str(today)),level=logging.INFO)

logging.info(sys.argv[1])




