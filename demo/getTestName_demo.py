import inspect
# functions
def whoami():
    return inspect.stack()[1][3]

def testFunc():
	x = whoami()
	print()