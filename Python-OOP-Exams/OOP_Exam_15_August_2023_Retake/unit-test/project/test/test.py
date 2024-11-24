from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):
    def setUp(self) -> None:
        self.alone = Trip(10000, 1, False)
        self.fam = Trip(30000, 2, True)

    def test_trip_init(self):
        self.assertEqual(self.alone.budget, 10000)
        self.assertEqual(self.alone.travelers, 1)
        self.assertEqual(self.alone.is_family, False)
        self.assertEqual(self.alone.booked_destinations_paid_amounts, {})
        self.assertEqual(self.alone.DESTINATION_PRICES_PER_PERSON, {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500})

        self.assertEqual(self.fam.budget, 30000)
        self.assertEqual(self.fam.travelers, 2)
        self.assertEqual(self.fam.is_family, True)
        self.assertEqual(self.fam.booked_destinations_paid_amounts, {})
        self.assertEqual(self.fam.DESTINATION_PRICES_PER_PERSON, {'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500})

    def test_travelers_setter_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.alone.travelers = 0
        self.assertEqual(str(ex.exception),"At least one traveler is required!")

    def test_family_setter(self):
        self.fam.travelers = 1
        self.assertTrue(self.fam.is_family, False)

    def test_book_destination_fail_destination(self):
        result = self.alone.book_a_trip("France")
        expected = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(result, expected)

    def test_book_destination_fail_budget(self):
        self.alone.budget = 1
        result = self.alone.book_a_trip("New Zealand")
        expected = 'Your budget is not enough!'
        self.assertEqual(result, expected)

    def test_book_destination_success(self):
        self.alone.budget = 10000
        result = self.alone.book_a_trip("New Zealand")
        expected = 'Successfully booked destination New Zealand! Your budget left is 2500.00'
        self.assertEqual(result, expected)
        self.assertEqual(self.alone.booked_destinations_paid_amounts, {'New Zealand': 7500})

    def test_book_destination_success_family(self):
        self.fam.budget = 30000
        result = self.fam.book_a_trip("New Zealand")
        expected = 'Successfully booked destination New Zealand! Your budget left is 16500.00'
        self.assertEqual(result, expected)
        self.assertEqual(self.fam.booked_destinations_paid_amounts, {'New Zealand': 13500})

    def test_booking_status_no_bookings(self):
        self.assertEqual(self.alone.booking_status(),
                         "No bookings yet. Budget: 10000.00")

    def test_booking_status_with_bookings(self):
        self.alone.book_a_trip("New Zealand")
        self.assertEqual(self.alone.booking_status(),
                         "Booked Destination: New Zealand\n"
                         "Paid Amount: 7500.00\n"
                         "Number of Travelers: 1\n"
                         "Budget Left: 2500.00")

if __name__ == '__main__':
    main()