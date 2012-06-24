import unittest
def run_tests():
    """ run available tests """
    loader = unittest.TestLoader()
    tests = loader.discover("./tests/")
    runner = unittest.runner.TextTestRunner()
    runner.run(tests)

if __name__ == "__main__":
    run_tests()

