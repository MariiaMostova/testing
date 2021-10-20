from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://material.io/")
    
def get_elem_by_class(value):
    return driver.find_element(By.CLASS_NAME, value)

def get_elem_by_name(value):
    return driver.find_element(By.NAME, value)

def click_button(button):
    button.click()

def print_in_input(input, text):
    input.send_keys(text)

def test_result(result, expected):
    assert result == expected
    
if __name__ == "__main__":
    search_button = get_elem_by_class("search-button")
    click_button(search_button)
    search_input = get_elem_by_name("q")
    test_result(search_input.value_of_css_property("visibility"), "visible")
    print_in_input(search_input, "AppBar")
    test_result(search_input.get_attribute('value'), "AppBar")
    driver.quit()
