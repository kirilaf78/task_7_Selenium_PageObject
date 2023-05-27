import json

from hamcrest import assert_that, equal_to
from page_objects import PageObject, PageElement
from selenium.webdriver.common.by import By


class FormPage(PageObject):
    customer_name = PageElement(name="custname")
    telephone = PageElement(name="custtel")
    email = PageElement(name="custemail")
    small = PageElement(xpath="//input[@name='size' and @value='small']")
    medium = PageElement(xpath="//input[@name='size' and @value='medium']")
    large = PageElement(xpath="//input[@name='size' and @value='large']")
    bacon = PageElement(xpath="//input[@name='topping' and @value='bacon']")
    cheese = PageElement(xpath="//input[@name='topping' and @value='cheese']")
    onion = PageElement(xpath="//input[@name='topping' and @value='onion']")
    mushroom = PageElement(xpath="//input[@name='topping' and @value='mushroom']")
    delivery_time = PageElement(name="delivery")
    instructions = PageElement(name="comments")
    submit = PageElement(xpath="//button")


class FillFormSteps:

    def __init__(self, browser):
        self.parsed_json = None
        self.browser = browser
        self.page = FormPage(self.browser, root_uri="https://httpbin.org")

    def open(self):
        self.page.get("/forms/post")

    def fill_form(self, form: dict):
        if form.get("custname"):
            self.page.customer_name = form.get("custname")

        if form.get("custtel"):
            self.page.telephone = form.get("custtel")

        if form.get("custemail"):
            self.page.email = form.get("custemail")

        if form.get("size"):
            self.page.__getattribute__(form.get("size")).click()

        if form.get("topping"):
            [self.page.__getattribute__(x).click() for x in form["topping"]]

        if form.get("delivery"):
            self.page.delivery_time = form.get("delivery")

        if form.get("comments"):
            self.page.instructions = form.get("comments")

    def submit(self):
        self.page.submit.click()

    def get_response(self):
        content = self.browser.find_element(By.TAG_NAME, "pre").text
        self.parsed_json = json.loads(content)

    def verify_form(self, expected_form):
        assert_that(self.parsed_json["form"], equal_to(expected_form))
