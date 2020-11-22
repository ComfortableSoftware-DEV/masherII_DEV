import inspect
import math
from re import sub as SUB
import time
import os
import getopt as GO
from sys import argv as ARGV


from dataStuff import constants as C


PATH = os.path
ABSPATH = os.path.abspath


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# *
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getDebugInfo(varListed):
	previous_frame = inspect.currentframe().f_back
	(filename, line_number, function_name, lines, index) = inspect.getframeinfo(previous_frame)
	outStr = f"""file {filename},
line {line_number},
function {function_name}
{varListed}
"""
	return outStr


LCurrentMilis = lambda: int(round(time.time() * 10000))
