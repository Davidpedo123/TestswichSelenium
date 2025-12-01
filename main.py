from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

options = Options()
options.add_argument("--ignore-certificate-errors")

service = Service("C:/Users/david/Downloads/edgedriver_win64/msedgedriver.exe")

driver = webdriver.Edge(service=service, options=options)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

def loginApp(driver, username, password,form):
    driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    
    
    username_field = driver.find_element("id", "email")
    password_field = driver.find_element("id", "password")
    login_button = driver.find_element("id", "submit")
    

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

 
    time.sleep(5)
    
    addTest(form)

   
    print("Revisa si el login fue exitoso en la página antes de cerrar el navegador.")


    time.sleep(10)  


    driver.quit()



def addTest(form):
    newContact = driver.find_element("id", "add-contact")
    newContact.click()
    firsnameField = driver.find_element("id", "firstName")
    lastnameField = driver.find_element("id", "lastName")
    birthdateField = driver.find_element("id", "birthdate")
    emailField = driver.find_element("id", "email")
    phoneField = driver.find_element("id", "phone")
    streeaddressField = driver.find_element("id", "street1")
    streeaddress2Field = driver.find_element("id", "street2")
    cityField = driver.find_element("id", "city")
    stateProvinceField = driver.find_element("id", "stateProvince")
    postalCodeField = driver.find_element("id", "postalCode")
    countryField = driver.find_element("id", "country")
    submitButton = driver.find_element("id", "submit")
    firsnameField.send_keys(form["first_name"])
    lastnameField.send_keys(form["last_name"])
    birthdateField.send_keys(form["date_of_birth"])
    emailField.send_keys(form["email"])
    phoneField.send_keys(form["phone"])
    streeaddressField.send_keys(form["address"])
    streeaddress2Field.send_keys(form["address2"])
    cityField.send_keys(form["city"])
    stateProvinceField.send_keys(form["state"])
    postalCodeField.send_keys(form["zip_code"])
    countryField.send_keys(form["country"])
    submitButton.click()
    time.sleep(5)
    
    
    
    
    
    
loginApp(driver, "davidtejadamoreta26@gmail.com", "David16261626#", form)

