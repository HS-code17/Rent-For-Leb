import unittest
from unittest import result
from phase_1 import validate_url
from phase_2 import check_data, scrape_url

class TestUrl(unittest.TestCase):
    def test_url_case(self):
        # the problem is with this site it is returning an error. 
        # another site works fine
        result = validate_url("https://www.olx.com.lb/")
        self.assertEqual(result, "200")
    def test_scraping_case(self):
        # check if the data exists or not
        res = scrape_url("https://www.olx.com.lb/en/properties/apartments-villas-for-rent/")
        checking_results = check_data(res)
        self.assertEqual(checking_results, True)

if __name__=="__main__":
    unittest.main()