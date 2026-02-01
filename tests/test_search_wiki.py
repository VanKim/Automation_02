from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import csv
from time import sleep
from selenium.webdriver.common.keys import Keys
from utils.data_reader import DataReader

class TestSearchWiki:
    def test_json(self):
        DataReader.read_data_from_json_file('./testdata/test_json.json')


    testdata = DataReader.read_data_from_csv_file('./testdata/data.csv')
    @pytest.mark.parametrize("keyword", testdata)
    def search_wikipedia1(self, keyword):
        driver = webdriver.Chrome()
        driver.get('https://vi.wikipedia.org/wiki/Trang_Chính')
        sleep(5)
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        sleep(5)
        driver.quit()
