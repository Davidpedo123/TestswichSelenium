
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

# -----------------------------
# Rutas relativas
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
METRICS_DIR = PROJECT_ROOT / "metrics"
METRICS_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Datos del formulario
# -----------------------------
form = {
    "first_name": "David",
    "last_name": "Tejada",
    "phone": "809-555-5555",
    "email": "example@gmail.com",
    "date_of_birth": "1990-01-01",
    "address": "123 Main St, City, Country",
    "address2": "Apt 4B",
    "city": "CityName",
    "state": "StateName",
    "zip_code": "12345",
    "country": "CountryName"
}

# -----------------------------
# Utilidades
# -----------------------------
def elemento_existe(driver, by, value):
    return len(driver.find_elements(by, value)) > 0

def take_screenshot(driver, name):
    path = METRICS_DIR / f"{name}.png"
    driver.save_screenshot(str(path))

# -----------------------------
# Funciones principales
# -----------------------------
def loginApp(driver, username, password):
    driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)

def addTest(driver, form):
    newContact = driver.find_element(By.ID, "add-contact")
    newContact.click()

    firsnameField = driver.find_element(By.ID, "firstName")
    lastnameField = driver.find_element(By.ID, "lastName")
    birthdateField = driver.find_element(By.ID, "birthdate")
    emailField = driver.find_element(By.ID, "email")
    phoneField = driver.find_element(By.ID, "phone")
    streeaddressField = driver.find_element(By.ID, "street1")
    streeaddress2Field = driver.find_element(By.ID, "street2")
    cityField = driver.find_element(By.ID, "city")
    stateProvinceField = driver.find_element(By.ID, "stateProvince")
    postalCodeField = driver.find_element(By.ID, "postalCode")
    countryField = driver.find_element(By.ID, "country")
    submitButton = driver.find_element(By.ID, "submit")

    # Pruebas negativas y límites
    firsnameField.send_keys(form["first_name"])
    lastnameField.send_keys(form["last_name"])
    birthdateField.send_keys(form["date_of_birth"])

    emailField.clear()
    emailField.send_keys("invalidogmail.com")
    submitButton.click()
    time.sleep(1)

    emailField.clear()
    emailField.send_keys(form["email"])
    phoneField.clear()
    phoneField.send_keys(form["phone"])

    firsnameField.clear()
    firsnameField.send_keys("")
    submitButton.click()
    time.sleep(1)

    firsnameField.clear()
    firsnameField.send_keys(form["first_name"])

    long_email = "a" * 250 + "@example.com"
    emailField.clear()
    emailField.send_keys(long_email)
    submitButton.click()
    time.sleep(1)

    emailField.clear()
    emailField.send_keys(form["email"])

    long_phone = "809" + "5" * 30
    phoneField.clear()
    phoneField.send_keys(long_phone)
    submitButton.click()
    time.sleep(1)

    phoneField.clear()
    phoneField.send_keys(form["phone"])

    streeaddressField.send_keys(form["address"])
    streeaddress2Field.send_keys(form["address2"])
    cityField.send_keys(form["city"])
    stateProvinceField.send_keys(form["state"])
    postalCodeField.send_keys(form["zip_code"])
    countryField.send_keys(form["country"])

    submitButton.click()
    time.sleep(1)

    # Captura después de agregar contacto
    take_screenshot(driver, "crud_add")

def EditTest(driver):
    first_row = driver.find_element(By.XPATH, "//table[@id='myTable']//tr[@class='contactTableBodyRow'][1]")
    first_row.click()
    time.sleep(1)

    edit_button = driver.find_element(By.ID, "edit-contact")
    edit_button.click()
    time.sleep(1)

    firsnameField = driver.find_element(By.ID, "firstName")
    firsnameField.clear()
    firsnameField.send_keys("PruebaPasada")
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)

    driver.find_element(By.ID, "return").click()
    time.sleep(1)

    # Captura después de editar contacto
    take_screenshot(driver, "crud_edit")

def DeleteTest(driver):
    first_row = driver.find_element(By.XPATH, "//table[@id='myTable']//tr[@class='contactTableBodyRow'][1]")
    first_row.click()
    time.sleep(1)

    driver.find_element(By.ID, "delete").click()
    time.sleep(1)

    driver.switch_to.alert.accept()
    time.sleep(1)

    # Captura después de eliminar contacto
    take_screenshot(driver, "crud_delete")

def Logout(driver):
    if elemento_existe(driver, By.ID, "logout"):
        driver.find_element(By.ID, "logout").click()
        time.sleep(1)

def negativeLoginTest(driver):
    driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    driver.find_element(By.ID, "email").send_keys("usuario_incorrecto@gmail.com")
    driver.find_element(By.ID, "password").send_keys("contraseña_incorrecta")
    driver.find_element(By.ID, "submit").click()
    time.sleep(1)

    error_elements = driver.find_elements(By.ID, "error")
    assert len(error_elements) > 0, "No se encontró el mensaje de error"
    assert error_elements[0].text == "Incorrect username or password", "El mensaje de error no coincide"

# -----------------------------
# Fixture
# -----------------------------
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--ignore-certificate-errors")
    service = Service("C:/Users/david/Downloads/edgedriver_win64/msedgedriver.exe")
    drv = webdriver.Edge(service=service, options=options)
    yield drv
    drv.quit()


def test_login_correcto(driver):
    loginApp(driver, "davidtejadamoreta26@gmail.com", "David16261626#")
    take_screenshot(driver, "login_correcto")
    assert elemento_existe(driver, By.ID, "add-contact"), "El login correcto debería mostrar 'add-contact'"

def test_crud_contacto(driver):
    loginApp(driver, "davidtejadamoreta26@gmail.com", "David16261626#")
    assert elemento_existe(driver, By.ID, "add-contact")
    addTest(driver, form)
    EditTest(driver)
    DeleteTest(driver)
    Logout(driver)

def test_login_incorrecto(driver):
    negativeLoginTest(driver)
    take_screenshot(driver, "login_incorrecto")
