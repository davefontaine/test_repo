#!/usr/bin/python

import sys
import numpy as np

print np.recfromcsv(sys.argv.pop())
print "new branch for testing"
print "testing if I modify file but do not git add, only git commit"


