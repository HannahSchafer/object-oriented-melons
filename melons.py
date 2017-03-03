"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """Parent class for melon orders.
    """

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price."""

        base_price = 5

        if self.species == "Christmas melons":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        return super(DomesticMelonOrder, self).__init__(species, qty,
                                                        order_type="domestic",
                                                        tax=0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.country_code = country_code
        return (super(InternationalMelonOrder, self)
                                    .__init__(species, qty,
                                              order_type="international",
                                              tax=0.17))

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

    def __init__(self, species, qty, passed_inspection=False):
        self.passed_inspection = passed_inspection
        return super(GovernmentMelonOrder, self).__init__(species, qty,
                                                          order_type="government",
                                                          tax=0)

    def mark_inspection(self, passed):
        """ Check if the melon has passed govenment inspection """

        if passed is True:
            self.passed_inspection = True
