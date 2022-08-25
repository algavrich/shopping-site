"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email 
        self.password = password

    def __repr__(self):

        return (
            f"<Customer: {self.first_name} {self.last_name}, 
            {self.email}, 
            {self.password}>"
        )


def get_customers_from_file(filepath):

    customers = {}

    for line in open(filepath):

        line = line.split("|")
        first_name, last_name, email, password = line 
        customers[email] = Customer(first_name, last_name, email, password)

    return customers

