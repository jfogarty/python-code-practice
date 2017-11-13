import inspect
import time
from datetime import timedelta

debugging = False
debugging = True

debugging2 = False

logging = True

def printf(f, *args):
    if len(args): 
        print(f.format(*args))
    else:
        print(f)   

def dbg(f, *args):
    if debugging:
        if len(args):
            printf('  DBG:' + f, *args)
        else:
            print(f)

def dbg2(f, *args):
    if debugging2:
        if len(args):
            printf('  DBG2:' + f, *args)
        else:
            print(f)
        
def log(f, *args):
    if logging:
        printf(f, *args)
        
def log_error(f, *args):
    if logging:
        if len(args):
            printf('*** ERROR:' + f, *args)
        else:
            print('*** ERROR:', f)
        
def class_name(instance):
    return type(instance).__name__

#------------------------------------------------------------------------------
class TestCase(object):
    def __init__(self, name, method, inputs, expected, catchExceptions=False):
        self.name = name
        self.method = method
        self.inputs = inputs
        self.expected = expected
        self.catchExceptions = catchExceptions
        
    def run(self):
        if self.catchExceptions:
            try:
                return self.method(*self.inputs)
            except Exception as x:
                return x
        else:
                return self.method(*self.inputs)

#------------------------------------------------------------------------------
class TestSet(object):
    def __init__(self, cases):
        self.cases = cases
    
    def run_tests(self, repeat=1):
        count = 0
        errors = 0
        total_time = 0
        for case in self.cases:
            count += 1
            start_time = time.time()
            for iteration in range(repeat):
                dbg2("*** Running '{0}' iteration {1}", case.name, iteration+1)
                result = case.run()
            elapsed_time = time.time() - start_time
            total_time += elapsed_time
            if callable(case.expected):
                if not case.expected(result):
                    errors += 1
                    log_error("Test {0} failed. Returned {1}", case.name, result)
            elif result != case.expected:
                errors += 1
                log_error('Test {0} failed. Returned "{1}", expected "{2}"', case.name, result, case.expected)
        if errors:
            log_error("Tests passed: {0}; Failures: {1}", count-errors, errors)
        else:
            log("All {0} tests passed.", count)
        log("Elapsed test time: {0}", timedelta(seconds=total_time))

#------------------------------------------------------------------------------
def elapsed_time(func, *args, msg=''):
    ''' Display the elapsed time of the function.
        Return the function value.
    '''
    stime = time.time()
    result = func(*args)
    etime = time.time() - stime
    log(msg + "Elapsed test time: {0}", timedelta(seconds=etime))
    return result
        
