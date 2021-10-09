'''
If instead of optimizing your program memory or CPU usage, you want to just straight up limit it to some hard number, then Python has a library for that too

Here we can see both options to set maximum CPU runtime as well as maximum memory used limit. 
For CPU limit we first get soft and hard limit for that specific resource ( RLIMIT_CPU) and then set it using number of seconds specified by argument and previously retrieved hard limit. 
Finally, we register signal that causes system exit if CPU time is exceeded. 
As for the memory, we again retrieve soft and hard limit and set it using setrlimit with size argument and retrieved hard limit
'''

import signal
import resource
import os

# To Limit CPU time
def time_exceeded(signo, frame):
	print("CPU exceeded...")
	raise SystemExit(1)

def set_max_runtime(seconds):
	# Install the signal handler and set a resource limit
	soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
	resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
	signal.signal(signal.SIGXCPU, time_exceeded)

# To limit memory usage
def set_max_memory(size):
	soft, hard = resource.getrlimit(resource.RLIMIT_AS)
	resource.setrlimit(resource.RLIMIT_AS, (size, hard))