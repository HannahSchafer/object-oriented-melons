"""This file should have our order classes in it."""

from random import randint
from datetime import date, time


class AbstractMelonOrder(object):
    """Parent class for melon orders.
    """

    def __init__(self, species, qty, order_date, order_type=None, tax=None):
        """Initialize melon order attributes"""

        self.order_date = order_date
        self.species = species
        self.qty = qty
        self.shipped = False

        if order_type and tax:
            self.order_type = order_type
            self.tax = tax



    def get_base_price(self):
        """ Add splurge and morning rush pricing M-F, 8-11am"""

        splurge_price = randint(5, 10)

        ## Morning rush pricing need be defined
        # self.order_date
        #         datetime.time
        #         date.weekday()

        return base_price

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "Christmas melons":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_date = None###############

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes"""

    #     return super(DomesticMelonOrder, self).__init__(species, qty,
    #                                                     order_type="domestic",
    #                                                     tax=0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_date = None###############
    # def __init__(self, species, qty, country_code):
    #     """Initialize melon order attributes"""

    #     self.country_code = country_code
    #     return (super(InternationalMelonOrder, self)
    #                                 .__init__(species, qty,
    #                                           order_type="international",
    #                                           tax=0.17))

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self, international_fee=3):
        """ Add international fee of $3 to orders with less than 10 melons"""

        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total += international_fee

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """ """

    def __init__(self, species, qty, order_date, passed_inspection=False):
        self.passed_inspection = passed_inspection
        return super(GovernmentMelonOrder, self).__init__(species, qty, order_date)

    def mark_inspection(self, passed):
        """ Check if the melon has passed govenment inspection """

        self.passed_inspection = passed
