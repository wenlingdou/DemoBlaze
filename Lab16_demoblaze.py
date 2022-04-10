# 1. Using Selenium WebDriver, open the web browser.
# 2. Maximize the browser window.
# 3. Navigate to web page URL - https://www.demoblaze.com/ (Links to an external site.)
# 4. Check URL and title are as expected.
# 5. On the home page, find the Nexus 6 model and click on it.
# 6. On the product page, check Nexus 6 h2 title is displayed. Use assert.
# 7. Click by Add to Cart button. If you'll see an alert at the top, use this command - driver.switch_to.alert.accept()
# 8. Go to Cart at the top menu and click on it.
# 9. Check the order is displayed and click by Delete link.
# 10. Close the browser and display a user-friendly message.

import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # add this import for drop down lists
from selenium.webdriver import Keys

s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

app = 'demoblaze'
demo_homepage_url = 'https://www.demoblaze.com/'
demo_homepage_title = 'STORE'
demo_productpage_url = 'https://www.demoblaze.com/prod.html?idp_=3'
demo_cartpage_url = 'https://www.demoblaze.com/cart.html'


def setUp():
    print(f'Launch {app} App')
    print(f'--------------------------------------------------')

    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(demo_homepage_url)
    if driver.current_url == demo_homepage_url and driver.title == demo_homepage_title:
        print('HoHoHo! {app} App website launched successfully!')
        print(f'{app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Homepage title: {driver.title}')
        tearDown()

def tearDown():
    if driver is not None:
        print('See you next time!')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()

def navigation():
    if driver.current_url == demo_homepage_url:
        driver.find_element(By.LINK_TEXT, 'Nexus 6').click()
        sleep(0.25)

        if driver.current_url == demo_productpage_url:
            assert driver.current_url == demo_productpage_url
            assert driver.find_element(By.XPATH, '//h2[contains(., "Nexus 6")]').is_displayed()
            sleep(0.25)
            print(f'The product page is located.')
            print(f'Nexus 6 h2 is displayed successfully!')
        else:
            print(f'Nexus 6 h2 is not displayed. Please check your code.')


        driver.find_element(By.XPATH, '//a[contains(., "Add to cart")]').click()
        sleep(0.25)
        driver.switch_to.alert.accept()
        sleep(0.25)
        driver.find_element(By.LINK_TEXT, 'Cart').click()
        sleep(0.25)
        if driver.current_url == demo_cartpage_url:
             print(f'Cart page: {demo_cartpage_url} is located.')
             assert driver.find_element(By.XPATH, '//td[contains(., "Nexus 6")]').is_displayed()
             print(f'The product Nexus 6 is found in the cart.')
             sleep(0.25)
        else:
            print(f'The product is not found in cart. Please try again.')
        driver.find_element(By.XPATH, '//a[contains(., "Delete")]').click()
        print(f'The product in the cart is deleted successfully!')
        sleep(0.25)


setUp()
navigation()
tearDown()