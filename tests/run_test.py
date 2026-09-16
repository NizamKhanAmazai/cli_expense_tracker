import unittest
from .storage import Storage_Test

def run_test(): 
    suite = unittest.TestSuite()

    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Storage_Test))
    # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(Services_Test))

    #Add the cleanup/final test 
    # suite.addTest(Storage_Test('test_zzz_cleanup'))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    #result is a TestResult object you can check
    if result.failures:
        print("Failures:", result.failures)
    return result
