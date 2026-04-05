import time

from faker import Faker
from faker.providers.python import TEnum


class Fake:
    """
    A class for generating random test data using the Faker library.
    """

    def __init__(self, faker: Faker):
        """
        :param faker: An instance of the Faker class used for data generation.
        """
        self.faker = faker

    def enum(self, value: type[TEnum]) -> TEnum:
        """
        Selects a random value from an enum type.

        :param value: Enum class to generate a value from.
        :return: A random value from the enumeration.
        """
        return self.faker.enum(value)

    def email(self) -> str:
        """
        Generates a random email.

        If not specified, a random domain will be used.
        :return: A random email.
        """
        return f"{time.time()}.{self.faker.email()}"

    def category(self) -> str:
        """
        Generates a random purchase category from a predefined list.

        Used to simulate expense types in systems that model
        user transactions or payment behavior for goods and services.

        :return: A random category (e.g., 'gas', 'taxi', 'supermarkets', etc.).
        """
        return self.faker.random_element([
            "gas",
            "taxi",
            "tolls",
            "water",
            "beauty",
            "mobile",
            "travel",
            "parking",
            "catalog",
            "internet",
            "satellite",
            "education",
            "government",
            "healthcare",
            "restaurants",
            "electricity",
            "supermarkets",
        ])

    def last_name(self) -> str:
        """
        Generates a random last name.

        :return: A random last name.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Generates a random first name.

        :return: A random first name.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Generates a random middle name/patronymic.

        :return: A random middle name.
        """
        return self.faker.first_name()

    def phone_number(self) -> str:
        """
        Generates a random phone number.

        :return: A random phone number.
        """
        return self.faker.phone_number()

    def float(self, start: int = 1, end: int = 100) -> float:
        """
        Generates a random floating-point number within the specified range.

        :param start: Start of the range (inclusive).
        :param end: End of the range (inclusive).
        :return: A random floating-point number.
        """
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:
        """
        Generates a random monetary amount.

        :return: A value between 1 and 1000.
        """
        return self.float(1, 1000)


# Create an instance of the Fake class using Faker
fake = Fake(faker=Faker())