import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import threading
import time, configparser

ChromeDriverManager().install()

config = configparser.ConfigParser()
config.read("config.txt", encoding="utf-8")

# Настройка браузера и автозагрузка Chromedriver
def get_driver():
    uc_options = uc.ChromeOptions()
    uc_options.add_argument("--disable-gpu")
    uc_options.add_argument("--no-sandbox")
    uc_options.add_argument("--start-maximized")
    uc_options.page_load_strategy = 'eager'
    driver = uc.Chrome(options=uc_options)
    return driver


# Прокрутка страницы вниз
def scroll_to_bottom(driver):
    scroll_step = 16  # Плавный шаг
    scroll_pause_time = 0.01  # Плавная задержка между шагами

    last_scroll_position = 0
    while True:
        driver.execute_script(f"window.scrollBy(0, {scroll_step});")
        time.sleep(scroll_pause_time)

        new_scroll_position = driver.execute_script("return window.scrollY + window.innerHeight")
        total_height = driver.execute_script("return document.body.scrollHeight")

        if new_scroll_position >= total_height:
            break

        if new_scroll_position == last_scroll_position:
            # Больше не прокручивается — выходим
            break

        last_scroll_position = new_scroll_position


def authorization(driver, account_number):
    driver.get("https://mangabuff.ru/login")

    account_name = config.sections()[int(account_number) - 1]
    email = config[account_name]["email"]
    password = config[account_name]["password"]

    # --- Получаем CSRF-токен со страницы ---
    csrf_token = driver.execute_script(
        "return document.querySelector('meta[name=\"csrf-token\"]').getAttribute('content');"
    )

    # --- Формируем и выполняем JS-запрос авторизации ---
    js_code = f"""
    fetch("https://mangabuff.ru/login", {{
        method: "POST",
        headers: {{
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-CSRF-TOKEN": "{csrf_token}",
            "X-Requested-With": "XMLHttpRequest"
        }},
        body: "email={email}&password={password}"
    }}).then(res => res.text())
      .then(text => console.log("✅ Ответ сервера:", text))
      .catch(err => console.error("❌ Ошибка:", err));
    """

    driver.execute_script(js_code)
    time.sleep(2)

# Обработка одной основной ссылки
def process_main_link(link, account_number: int, number: int = 1, cnt: int = 90**5):
    number = int(number)
    cnt = int(cnt)
    driver = get_driver()
    authorization(driver, account_number)
    driver.get(link)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "chapters__list"))
        )
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div[4]/div[1]/button[2]").click()
        time.sleep(2)
    except Exception as e:
        print(f"[{link}] Не удалось загрузить страницу: {e}")
        driver.quit()
        return

    try:
        chapter_block = driver.find_element(By.CLASS_NAME, "chapters__list")
        chapter_links = [a.get_attribute("href") for a in chapter_block.find_elements(By.TAG_NAME, "a")]
        chapter_links.reverse()
    except Exception as e:
        print(f"[{link}] Ошибка при получении глав: {e}")
        driver.quit()
        return

    count = 0
    chapter_driver = driver
    for i in range(len(chapter_links)):
        if i in range(number - 1, number + cnt - 1):
            try:
                chapter_driver.get(chapter_links[i])

                WebDriverWait(chapter_driver, 20).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                scroll_to_bottom(chapter_driver)
                count += 1
            except Exception as e:
                print(f"[{chapter_links[i]}] Ошибка при обработке: {e}")

    chapter_driver.quit()
    print(f"\nГотово: {link}\nГлав обработано: {count}\n")


def main():
    print(f"Загруженные аккаунты:")
    for i, section in enumerate(config.sections(), start=1):
        print(f"{i}. {section}")
    print("Введите ссылку, номер аккаунта, номер главы, сколько глав (например, 'mangabuff.ru 1 100 10', пустая строка — завершение ввода):")
    while True:
        inp = input().strip().split(" ")
        if inp == ['']:
            break
        threading.Thread(target=process_main_link, args=(*inp,)).start()

if __name__ == "__main__":
    main()
