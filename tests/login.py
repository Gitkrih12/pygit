
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://optum158-dev-ed.develop.my.salesforce.com/')
    #page.screenshot(path="test.png")
    #browser.close()

    ustextbox = page.wait_for_selector('#username')
    ustextbox.type('rao@company.sandbox')


    pswdtextbox = page.wait_for_selector('#password')
    pswdtextbox.type('Iamoptum123')


    loginbutton = page.wait_for_selector('#Login')
    loginbutton.click()
    page.wait_for_timeout(6000)