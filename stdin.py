import fileinput
import sys

# %load TestHarness
debugging = False
#debugging = True

debugging2 = False

logging = True


def dbg(f, *args):
    if debugging:
        print(('  DBG:' + f).format(*args))

def dbg2(f, *args):
    if debugging2:
        print(('  DBG2:' + f).format(*args))
        
def log(f, *args):
    if logging:
        print((f).format(*args))
        
def log_error(f, *args):
    if logging:
        print(('*** ERROR:' + f).format(*args))   
        
log('-- Feed me')

with sys.stdin as f:
    for line in f:
    #for line in fileinput.input():
        log('The line is : "{0}"', line.rstrip())
log('-- Eat me')
