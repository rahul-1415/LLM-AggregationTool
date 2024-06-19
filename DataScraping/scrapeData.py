import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FetchData:
    def setup_method(self):
        options = Options()
        options.headless = True  # Run in headless mode
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_fetch_data(self):
        # Open a CSV file to store the article data
        with open('article_data.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Counter", "Article Data"])

            self.vars["counter"] = 1
            while self.vars["counter"] <= 100:
                print("Counter: {}".format(self.vars["counter"]))
                self.driver.get("https://www.c40knowledgehub.org/s/global-search/%40uri#t=Articles&sort=relevancy&numberOfResults=100")
                self.driver.set_window_size(1420, 851)
                
                # Wait until the main content is loaded
                WebDriverWait(self.driver, 60).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".coveo-list-layout"))
                )
                
                # Select the article based on the counter
                selector = f".coveo-list-layout:nth-child({self.vars['counter']}) img"
                try:
                    # Wait until the article element is present
                    WebDriverWait(self.driver, 60).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    article_element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    article_element.click()
                    
                    # Wait for the article content to load
                    WebDriverWait(self.driver, 60).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".knowledgeBody"))
                    )

                    # Retrieve article data
                    article_body = self.driver.find_element(By.CSS_SELECTOR, ".knowledgeBody")
                    actions = ActionChains(self.driver)
                    actions.double_click(article_body).perform()
                    self.vars["articleData"] = article_body.text
                    
                    print("Article Data: {}".format(self.vars["articleData"]))
                    
                    # Write the counter and article data to the CSV file
                    writer.writerow([self.vars["counter"], self.vars["articleData"]])
                except Exception as e:
                    print(f"Error on counter {self.vars['counter']}: {e}")
                    
                self.vars["counter"] += 1

if __name__ == "__main__":
    fetch_data = FetchData()
    fetch_data.setup_method()
    try:
        fetch_data.test_fetch_data()
    finally:
        fetch_data.teardown_method()
