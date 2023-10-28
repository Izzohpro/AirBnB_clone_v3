#!/usr/bin/python3
"""Testing the Amenity model"""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity


class TestAmenity(TestBasemodel):
    """Represents test for the Amenity model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Testing the type of name."""
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
