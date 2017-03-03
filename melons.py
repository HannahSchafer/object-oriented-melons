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
        return (super(DomesticMelonOrder, self)
                                    .__init__(species, qty,
                                              order_type="international",
                                              tax=0.17))

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
