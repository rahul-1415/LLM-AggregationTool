import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestPromptTesting:
    def setup_method(self):
        chrome_options = Options()

        user_data_path = '/Users/rahul/Library/Application Support/Google/Chrome'  
        profile_name = 'Default'  

        chrome_options.add_argument(f"--user-data-dir={user_data_path}")
        chrome_options.add_argument(f"--profile-directory={profile_name}")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--remote-debugging-port=9222")  # Add this line
        # chrome_options.add_argument("--disable-extensions")  # Add this line to disable extensions
        # chrome_options.add_argument("--disable-plugins-discovery")

        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')

        webdriver_service = Service('/usr/local/bin/chromedriver')
        self.driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_chatGPT(self):
        self.vars["prompt1"] = "How to keep the house cool in extreme summer heat?"
        self.driver.get("https://chat.openai.com/")  # Corrected URL
        self.driver.set_window_size(1176, 875)
        
        # Wait for the input field to be visible and interact with it
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="prompt-textarea"]')))
        input_field = self.driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]')
        input_field.click()
        input_field.send_keys(self.vars["prompt1"])
        input_field.send_keys(Keys.RETURN)  # Simulate pressing Enter key
        
        # Wait for the response to be generated
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".markdown > p")))
        self.vars["chatgptResponse"] = self.driver.find_element(By.CSS_SELECTOR, ".markdown").text
        print("ChatGPT Response: {}".format(self.vars["chatgptResponse"]))

    def test_gemini(self):
        self.vars["prompt1"] = "How to keep the house cool in extreme summer heat?"
        self.driver.get("https://gemini.google.com/app")  # Corrected URL if necessary
        self.driver.set_window_size(1176, 875)
        self.driver.execute_script("window.scrollTo(0,0)")
        
        # Interact with the Gemini input field
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ql-editor > p")))
        element = self.driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        self.driver.execute_script("arguments[0].innerText = arguments[1]", element, self.vars["prompt1"])
        self.driver.find_element(By.CSS_SELECTOR, ".send-button > .mat-icon").click()
        
        # Wait for the response to be generated
        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".markdown")))
        self.vars["geminiResponse"] = self.driver.find_element(By.CSS_SELECTOR, ".markdown").text
        print("Gemini Response: {}".format(self.vars["geminiResponse"]))

if __name__ == "__main__":
    t1 = TestPromptTesting()
    t1.setup_method()
    try:
        # t1.test_chatGPT()
        t1.test_gemini()
    finally:
        t1.teardown_method()
