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

import time
from datetime import timedelta

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
                    logError("Test {0} failed. Returned {1}", case.name, result)
            elif result != case.expected:
                errors += 1
                logError('Test {0} failed. Returned "{1}", expected "{2}"', case.name, result, case.expected)
        if errors:
            logError("Tests passed: {0}; Failures: {1}", count-errors, errors)
        else:
            log("All {0} tests passed.", count)
        log("Elapsed test time: {0}", timedelta(seconds=total_time))

        