import pytest

from task7_1 import FillFormSteps


@pytest.mark.parametrize('comments, name, delivery, size',
                         [('no onion', 'Jora', '17:15', 'large'), ('more sauce', 'Janna', '13:30', 'small'),
                          ('', 'Vasil', '16:00', 'medium')])
def test_pizza_form(browser, comments, name, delivery, size):
    step = FillFormSteps(browser)
    step.open()
    form = {'comments': comments,
            'custemail': 'kirill@gmail.com',
            'custname': name,
            'custtel': '+460665544333',
            'delivery': delivery,
            'size': size,
            'topping': ['bacon', 'cheese']}
    step.fill_form(form)
    step.submit()
    step.get_response()
    step.verify_form(form)
