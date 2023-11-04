import pytest
import requests
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from yaml_reader import data
import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

url_login = data["url_login"]
login = data["login"]
password = data["passwd"]


@pytest.fixture(scope="session")
def browser():
    browser = data['browser']
    if browser == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=option)
    else:
        service = Service(executable_path=GeckoDriverManager().install())
        option = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=option)
    yield driver
    driver.quit()


@pytest.fixture(scope="module", autouse=True)
def user_login():
    try:
        result = requests.Session().post(url=url_login, data={'username': login, 'password': password})
        response_json = result.json()
        token = response_json.get('token')
    except:
        logging.exception("Get token exception")
        token = None
    logging.debug("Return token success")
    return token


@pytest.fixture(scope="module", autouse=True)
def send_email():
    yield
    from_address = data.get("from_address")
    to_address = data.get("to_address")
    from_address_password = data.get("from_address_password")
    file = data.get("file")

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "Hi!!!"

    with open(file, "rb") as fl:
        part = MIMEApplication(fl.read(), Name=basename(file))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
        msg.attach(part)

    letter = data.get("letter")

    msg.attach(MIMEText(letter, "plain"))
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login(from_address, from_address_password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    server.quit()
