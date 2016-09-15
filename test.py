import unittest
import HTMLTestRunner
from pydoc_search import PythonOrgSearch

if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PythonOrgSearch))
    buf = file("TestReport.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
            stream=buf,
            title='Test the Report',
            description='Result of tests'
            )
    runner.run(suite)
