import random
import time
import re
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PlaceData:

    def __init__(self):
        self.keyword = ""
        self.name = ""
        self.category = ""
        self.address = ""
        self.phone = ""
        self.website = ""
        self.plus_code = ""
        self.rating = ""
        self.reviews = ""
        self.hours = ""


class GoogleMapsScraper:

    def __init__(self, image_output_folder):
        self.driver = None
        self.error_count = 0
        self.image_output_folder = image_output_folder

        self.config = {
            "language": "--lang=en-GB",
            "stars_text": "stars",
            "reviews_text": "reviews",
            "address_text": "Address: ",
            "website_text": "Website: ",
            "phone_text": "Phone: ",
            "plus_code_text": "Plus code: ",
            "hours_text": "Hide open hours for the week",
            "replace_hours": [
                ". Hide open hours for the week",
                "Hours might differ",
                "; "
            ]
        }

    def start_driver(self):

        try:
            chrome_options = webdriver.ChromeOptions()

            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--log-level=3")
            chrome_options.add_argument(self.config["language"])

            service = Service(ChromeDriverManager().install())

            self.driver = webdriver.Chrome(
                service=service,
                options=chrome_options
            )

            self.driver.get("https://www.google.com/maps")

            try:
                accept_button = WebDriverWait(self.driver, 7).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//*[@aria-label="Accept all"]')
                    )
                )
                accept_button.click()
            except:
                pass

            time.sleep(2)

            return True

        except Exception as e:
            print(e)
            print("Chrome driver error")

            return False

    def remove_accents(self, text):

        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )

        for a, b in replacements:
            text = text.replace(a, b).replace(a.upper(), b.upper())

        return text

    def scrape_place(self, keyword):

        try:

            place = PlaceData()
            place.keyword = keyword

            if self.error_count == 5:
                self.error_count = 0
                self.driver.get("https://www.google.com/maps")
                time.sleep(2)

            time.sleep(random.randint(1, 3))

            search_box = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    (By.ID, "searchboxinput")
                )
            )

            search_box.clear()
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.ENTER)

            time.sleep(4)

            if not self.is_loaded(keyword):
                return None

            panel = self.driver.find_element(
                By.XPATH,
                '//*[@id="pane"]/following-sibling::div'
            )

            place.name = panel.find_element(By.TAG_NAME, "h1").text

            try:

                rating_block = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            '//*[contains(@aria-label,"stars") and @role="img"]'
                        )
                    )
                )

                if "(" in rating_block.text:

                    split_data = rating_block.text.replace(")", "").split("(")

                    place.rating = split_data[0]
                    place.reviews = split_data[1]

                else:

                    rating_label = rating_block.get_attribute("aria-label")

                    place.rating = rating_label.replace("stars", "").strip()

                    review_block = self.driver.find_element(
                        By.XPATH,
                        '//*[contains(@aria-label,"reviews")]'
                    )

                    review_label = review_block.get_attribute("aria-label")

                    place.reviews = review_label.replace(
                        "reviews", ""
                    ).strip()

            except:
                pass

            try:

                img_src = panel.find_element(
                    By.XPATH,
                    '//img[@decoding="async"]'
                ).get_attribute("src")

                if "gstatic" not in img_src:

                    filename = keyword.lower()

                    filename = self.remove_accents(filename)

                    filename = re.sub(r"[^\w\s-]", "", filename)

                    filename = filename.replace(" ", "-")

                    filename = re.sub(r"-+", "-", filename)

                    full_path = f"{self.image_output_folder}{filename}.jpg"

                    urllib.request.urlretrieve(img_src, full_path)

            except:
                print("Image download failed")

            place.category = self.safe_find(
                '//button[contains(@jsaction,"pane.") and contains(@jsaction,".category")]'
            )

            place.address = self.extract_label("Address: ")

            place.website = self.extract_label("Website: ")

            place.phone = self.extract_label("Phone: ")

            place.plus_code = self.extract_label("Plus code: ")

            place.hours = self.get_hours()

            return place

        except Exception as e:

            print(e)

            self.error_count += 1

            return None

    def safe_find(self, xpath):

        try:
            return self.driver.find_element(By.XPATH, xpath).text
        except:
            return ""

    def extract_label(self, label):

        try:

            element = self.driver.find_element(
                By.XPATH,
                f'//*[contains(@aria-label,"{label}")]'
            )

            return element.get_attribute("aria-label").replace(label, "").strip()

        except:

            return ""

    def get_hours(self):

        try:

            hours = self.driver.find_element(
                By.XPATH,
                '//*[contains(@aria-label,"Hide open hours for the week")]'
            ).get_attribute("aria-label")

            for item in self.config["replace_hours"]:
                hours = hours.replace(item, "\n")

            return hours

        except:

            return ""

    def is_loaded(self, keyword):

        panel = self.driver.find_element(
            By.XPATH,
            '//*[@id="pane"]/following-sibling::div'
        )

        titles = panel.find_elements(By.TAG_NAME, "h1")

        for title in titles:

            if title.text != "":
                return True

        try:

            result = self.driver.find_element(
                By.XPATH,
                f'//div[contains(@aria-label,"{keyword}")]'
            )

            result.find_element(By.TAG_NAME, "a").click()

            time.sleep(3)

            return True

        except:

            return False

    def close(self):

        self.driver.quit()