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

def loginApp(driver, username, password):
    driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    
    # Encontrar los campos de usuario y contraseña, y el botón de login
    username_field = driver.find_element("id", "email")
    password_field = driver.find_element("id", "password")
    login_button = driver.find_element("id", "submit")
    
    # Ingresar las credenciales
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # Esperar unos segundos para ver si el login fue exitoso
    time.sleep(5)  # Esperar 5 segundos (ajusta según lo necesites)

    # Aquí podrías verificar si el login fue exitoso, por ejemplo, comprobando el cambio de URL
    print("Revisa si el login fue exitoso en la página antes de cerrar el navegador.")

    # Esperar más tiempo si lo necesitas
    time.sleep(10)  # Espera 10 segundos para revisar más antes de cerrar el navegador

    # Cerrar el navegador después de esperar
    driver.quit()

loginApp(driver, "davidtejadamoreta26@gmail.com", "David16261626#")

"""    
def loginApp(driver, username, password):
    driver.get("https://thinking-tester-contact-list.herokuapp.com/")
    
    username_field = driver.find_element("id", "email")
    password_field = driver.find_element("id", "password")
    login_button = driver.find_element("id", "submit")
    driver.implicitly_wait(5)
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    
loginApp(driver, "davidtejadamoreta26@gmail.com", "David16261626#")
driver.implicitly_wait(20)


"""