import os
import time
import random
import requests
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

LINKS = os.getenv("LINKS")
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36",
]
WAIT_TO_RENDER_S = 10
PAGE = 0


user_agent = random.choice(USER_AGENTS)

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f"User-Agent={user_agent}")

driver = webdriver.Chrome(
    options=options, service=Service(ChromeDriverManager().install())
)
driver.get(f"{LINKS}")
driver.implicitly_wait(WAIT_TO_RENDER_S)

cards_links = driver.find_elements(By.TAG_NAME, "img")

src_links = [cards_links[i].get_attribute("src") for i in range(len(cards_links))]

while True:
    try:
        PAGE += 1
        print(f"Page - {PAGE}")

        for i, link in enumerate(src_links):

            time.sleep(random.randint(1, 5))
            # ur.urlretrieve(link, f"./data/train/train_{i}.jpg")

            img_data = requests.get(link, timeout=1).content
            with open(f"./data/train/train_{PAGE}_{i}.png", "wb") as fileimage:
                fileimage.write(img_data)

            time.sleep(random.randint(1, 5))

        driver.find_element(
            By.CSS_SELECTOR,
            "#app > div.layoutPage__top.bodyBackground > div.container > div > div.pageGrid__left > div.paginator.paginator_position > a.paginator__item.paginator__item_last",
        ).click()

        time.sleep(random.randint(1, 5))
    except:
        break


driver.close()
