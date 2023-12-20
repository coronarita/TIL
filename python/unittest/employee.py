import requests

class Employee:
    # Sample Employee class

    raise_amt = 1.05

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    @property    
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

        # Mocking ! : Check whether just the code is ok or not, not related to the status of webpage.
        # not depend on website

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else : 
            return 'Bad Response!'
        