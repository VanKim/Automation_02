from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import csv
from time import sleep
from selenium.webdriver.common.keys import Keys


class TestSearchWiki:

    def read_data_from_file(file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            keywords = []
            for row in csv_reader:
                keywords.append(row['keyword'])
            # print(keywords)
            return keywords

    testdata = read_data_from_file('./testdata/data.csv')

    @pytest.mark.parametrize("keyword", testdata)
    def test_search_wikipedia1(self, keyword):
        driver = webdriver.Chrome()
        driver.get('https://vi.wikipedia.org/wiki/Trang_Chính')
        sleep(5)
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        sleep(5)
        driver.quit()