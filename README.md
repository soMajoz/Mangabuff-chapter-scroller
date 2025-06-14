# MangaBuff Chapter Scroller

## Краткое описание

### Русский
**MangaBuff Chapter Scroller** — Python-скрипт для автоматизации просмотра глав манги на сайте mangabuff.ru. Скрипт выполняет авторизацию с использованием учетных данных из файла `config.txt`, переходит по указанным ссылкам на мангу, открывает заданные главы и плавно прокручивает их до конца. Использует `undetected_chromedriver` и `selenium` для управления браузером Chrome, поддерживает многопоточность и гибкую настройку через конфигурационный файл.

**Предупреждение**: Использование скрипта может нарушать правила mangabuff.ru. Убедитесь, что ваши действия соответствуют условиям сервиса и законодательству.

# Документация: MangaBuff Chapter Scroller

## Возможности
- Авторизация на сайте с использованием учетных данных из конфигурационного файла.
- Автоматическая прокрутка страниц глав манги.
- Поддержка многопоточности для обработки нескольких ссылок одновременно.
- Настройка через файл `config.txt` для управления несколькими аккаунтами.
- Гибкий выбор начальной главы и количества глав для обработки.

## Требования
- **Операционная система**: Windows(Остальные не тестировались).
- **Python**: 3.8 или выше.
- **Браузер**: Google Chrome (последняя версия).
- **Зависимости Python**:
  - `undetected-chromedriver`
  - `selenium`
  - `webdriver-manager`

## Установка
1. Установите Python:
   - Скачайте и установите Python 3.8+ с [официального сайта](https://www.python.org/downloads/).
   - Убедитесь, что `pip` добавлен в PATH.
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/soMajoz/Mangabuff-chapter-scroller.git
   cd Mangabuff-chapter-scroller
   ```
3. Установите зависимости:
   ```bash
   pip install undetected-chromedriver selenium webdriver-manager
   ```
4. Убедитесь, что Google Chrome установлен и обновлен.
5. Создайте файл `config.txt` в корневой директории проекта (см. раздел "Конфигурация").

## Конфигурация
Файл `config.txt` должен содержать учетные данные для авторизации. Пример структуры:
```
[Account1]
email=user1@example.com
password=pass1

[Account2]
email=user2@example.com
password=pass2
```
- `[Account1]`, `[Account2]` — уникальные имена секций для каждого аккаунта.
- `email` и `password` — учетные данные для входа на mangabuff.ru.
- Файл должен быть в кодировке UTF-8.

## Использование
1. Запустите скрипт:
   ```bash
   python main.py
   ```
2. Скрипт отобразит список аккаунтов из `config.txt`:
   ```
   Загруженные аккаунты:
   1. Account1
   2. Account2
   ```
3. Введите данные в формате:
   ```
   <ссылка> <номер_аккаунта> <номер_главы> <количество_глав>
   ```
   Пример:
   ```
   https://mangabuff.ru/manga/example-manga 1 100 10
   ```
   - `<ссылка>`: URL страницы манги.
   - `<номер_аккаунта>`: номер аккаунта из `config.txt` (1 для `Account1`, 2 для `Account2` и т.д.).
   - `<номер_главы>`: номер первой главы.
   - `<количество_глав>`: количество глав для обработки.
4. Для завершения ввода оставьте строку пустой и нажмите Enter.
5. Скрипт запустит обработку в отдельном потоке, открывая браузер Chrome для каждой ссылки.

## Технические детали
- **Браузер**: Используется `undetected_chromedriver` для обхода обнаружения автоматизации.
- **Авторизация**: Выполняется через JavaScript-запрос с CSRF-токеном, извлеченным со страницы.
- **Прокрутка**: Плавная прокрутка страниц с шагом 16 пикселей и задержкой 0.01 секунды.
- **Многопоточность**: Каждая ссылка обрабатывается в отдельном потоке через `threading.Thread`.
- **Обработка ошибок**: Скрипт перехватывает исключения при загрузке страниц или глав, выводя сообщения об ошибках.

## Ограничения
- Скрипт не поддерживает CAPTCHA или двухфакторную аутентификацию.
- Частые запросы могут привести к блокировке аккаунта или IP-адреса.
- Производительность зависит от скорости интернета и мощности компьютера.
- Скрипт предназначен только для mangabuff.ru и не адаптирован для других сайтов.

## Рекомендации
- Используйте скрипт с умеренной частотой, чтобы избежать блокировки.
- Храните `config.txt` в безопасном месте, так как он содержит учетные данные.
- Регулярно обновляйте Google Chrome и зависимости Python.

## Лицензия
Проект распространяется под лицензией MIT. См. файл `LICENSE` для подробностей.

## Устранение неполадок
- **Ошибка "No such file: config.txt"**: Убедитесь, что файл `config.txt` существует и находится в той же директории, что и скрипт.
- **Браузер не открывается**: Проверьте, установлен ли Google Chrome, и обновите `undetected-chromedriver`.
- **Сайт не загружается**: Проверьте подключение к интернету или попробуйте позже, так как сайт может блокировать запросы.

## Контакты
Для вопросов или предложений создайте issue в репозитории или свяжитесь с автором.

### English
# MangaBuff Chapter Scroller

## Summary

**MangaBuff Chapter Scroller** is a Python script for automating the viewing of manga chapters on the website mangabuff.ru. The script performs authentication using credentials from a `config.txt` file, navigates to specified manga links, opens designated chapters, and smoothly scrolls them to the bottom. It utilizes `undetected_chromedriver` and `selenium` to control the Chrome browser, supports multi-threading, and offers flexible configuration through a config file.

**Warning**: Using this script may violate mangabuff.ru's terms of service. Ensure your actions comply with the site's policies and applicable laws.

# Documentation: MangaBuff Chapter Scroller

## Features
- Authentication on the website using credentials from a configuration file.
- Automatic scrolling of manga chapter pages.
- Multi-threading support for processing multiple links simultaneously.
- Configuration via `config.txt` to manage multiple accounts.
- Flexible selection of the starting chapter and the number of chapters to process.

## Requirements
- **Operating System**: Windows (other systems not tested).
- **Python**: 3.8 or higher.
- **Browser**: Google Chrome (latest version).
- **Python Dependencies**:
  - `undetected-chromedriver`
  - `selenium`
  - `webdriver-manager`

## Installation
1. Install Python:
   - Download and install Python 3.8+ from [the official website](https://www.python.org/downloads/).
   - Ensure `pip` is added to your PATH.
2. Clone the repository:
   ```bash
   git clone https://github.com/soMajoz/Mangabuff-chapter-scroller.git
   cd Mangabuff-chapter-scroller
   ```
3. Install dependencies:
   ```bash
   pip install undetected-chromedriver selenium webdriver-manager
   ```
4. Ensure Google Chrome is installed and updated.
5. Create a `config.txt` file in the project's root directory (see "Configuration" section).

## Configuration
The `config.txt` file must contain authentication credentials. Example structure:
```
[Account1]
email=user1@example.com
password=pass1

[Account2]
email=user2@example.com
password=pass2
```
- `[Account1]`, `[Account2]` — unique section names for each account.
- `email` and `password` — credentials for logging into mangabuff.ru.
- The file must be saved in UTF-8 encoding.

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. The script will display a list of accounts from `config.txt`:
   ```
   Loaded accounts:
   1. Account1
   2. Account2
   ```
3. Enter details in the format:
   ```
   <link> <account_number> <chapter_number> <number_of_chapters>
   ```
   Example:
   ```
   https://mangabuff.ru/manga/example-manga 1 100 10
   ```
   - `<link>`: URL of the manga page.
   - `<account_number>`: Account number from `config.txt` (1 for `Account1`, 2 for `Account2`, etc.).
   - `<chapter_number>`: Starting chapter number.
   - `<number_of_chapters>`: Number of chapters to process.
4. To finish inputting, leave the line blank and press Enter.
5. The script will launch processing in a separate thread, opening a Chrome browser for each link.

## Technical Details
- **Browser**: Uses `undetected_chromedriver` to bypass automation detection.
- **Authentication**: Performed via a JavaScript request with a CSRF token extracted from the page.
- **Scrolling**: Smooth scrolling with a 16-pixel step and a 0.01-second delay.
- **Multi-threading**: Each link is processed in a separate thread using `threading.Thread`.
- **Error Handling**: The script captures exceptions during page or chapter loading, displaying error messages.

## Limitations
- The script does not support CAPTCHA or two-factor authentication.
- Frequent requests may lead to account or IP bans.
- Performance depends on internet speed and computer capabilities.
- The script is designed specifically for mangabuff.ru and is not adapted for other websites.

## Recommendations
- Use the script sparingly to avoid detection or bans.
- Store `config.txt` securely, as it contains sensitive credentials.
- Regularly update Google Chrome and Python dependencies.

## License
The project is distributed under the MIT License. See the `LICENSE` file for details.

## Troubleshooting
- **Error "No such file: config.txt"**: Ensure `config.txt` exists and is in the same directory as the script.
- **Browser fails to launch**: Verify Google Chrome is installed and updated; reinstall `undetected-chromedriver` if needed.
- **Website fails to load**: Check your internet connection or try again later, as the site may block requests.

## Contact
For questions or suggestions, create an issue in the repository or contact the author.
