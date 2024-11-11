from unittest import TestCase, main
from project.student_report_card import StudentReportCard


class StudentReportCardTests(TestCase):
    def setUp(self):
        self.student_report_card = StudentReportCard('Ivan', 10)

    def test_init(self):
        new_student_report_card = StudentReportCard('Gosho', 12)
        # student_name, school_year, grades_by_subject
        expected_student_name = 'Gosho'
        expected_school_year = 12
        expected_grades_by_subject = {}
        self.assertEqual(expected_student_name, new_student_report_card.student_name)
        self.assertEqual(expected_school_year, new_student_report_card.school_year)
        self.assertEqual(expected_grades_by_subject, new_student_report_card.grades_by_subject)

    def test_get_student_name(self):
        expected_student_name = 'Ivan'
        self.assertEqual(expected_student_name, self.student_report_card.student_name)

    def test_set_student_name_valid(self):
        expected_student_name = 'Ivan'
        self.assertEqual(expected_student_name, self.student_report_card.student_name)

        self.student_report_card.student_name = 'Ivo'
        expected_student_name_post = 'Ivo'
        self.assertEqual(expected_student_name_post, self.student_report_card.student_name)

    def test_set_student_name_invalid_should_raise(self):
        with self.assertRaises(ValueError) as ex:
            self.student_report_card.student_name = ''

        expected_assert_raises_message = 'Student Name cannot be an empty string!'
        self.assertEqual(expected_assert_raises_message, str(ex.exception))

    def test_get_school_year_valid(self):
        expected_school_year = 10
        self.assertEqual(expected_school_year, self.student_report_card.school_year)

    def test_set_school_year_valid(self):
        expected_school_year = 10
        self.assertEqual(expected_school_year, self.student_report_card.school_year)

        self.student_report_card.school_year = 11
        expected_school_year_post = 11
        self.assertEqual(expected_school_year_post, self.student_report_card.school_year)

    def test_set_school_year_invalid_should_raise(self):
        expected_assert_raises_message = 'School Year must be between 1 and 12!'

        with self.assertRaises(ValueError) as ex_1:
            self.student_report_card.school_year = 13
        self.assertEqual(expected_assert_raises_message, str(ex_1.exception))

        with self.assertRaises(ValueError) as ex_2:
            self.student_report_card.school_year = 0
        self.assertEqual(expected_assert_raises_message, str(ex_2.exception))

        with self.assertRaises(ValueError) as ex_3:
            self.student_report_card.school_year = -11
        self.assertEqual(expected_assert_raises_message, str(ex_3.exception))

        def test_add_grade_non_exising(self):
            subject = 'Math'
            self.assertNotIn(subject, self.student_report_card.grades_by_subject)

            self.student_report_card.add_grade(subject, 6)
            self.assertIn(subject, self.student_report_card.grades_by_subject)
            self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

    def test_add_grade_existing(self):
        subject = 'Math'
        self.assertNotIn(subject, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject, 6)
        self.assertIn(subject, self.student_report_card.grades_by_subject)
        self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

        self.student_report_card.add_grade(subject, 5)
        self.assertEqual([6, 5], self.student_report_card.grades_by_subject[subject])

    def test_average_grade_by_subject(self):
        subject = 'Math'
        self.assertNotIn(subject, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject, 6)
        self.assertIn(subject, self.student_report_card.grades_by_subject)
        self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

        self.student_report_card.add_grade(subject, 5)
        self.assertEqual([6, 5], self.student_report_card.grades_by_subject[subject])

        expected_result = 'Math: 5.50'
        self.assertEqual(expected_result, self.student_report_card.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        subject = 'Math'
        self.assertNotIn(subject, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject, 6)
        self.assertIn(subject, self.student_report_card.grades_by_subject)
        self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

        self.student_report_card.add_grade(subject, 5)
        self.assertEqual([6, 5], self.student_report_card.grades_by_subject[subject])

        expected_result = 'Average Grade: 5.50'
        self.assertEqual(expected_result, self.student_report_card.average_grade_for_all_subjects())

    def test_repr(self):
        subject = 'Math'
        self.assertNotIn(subject, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade(subject, 6)
        self.assertIn(subject, self.student_report_card.grades_by_subject)
        self.assertEqual([6], self.student_report_card.grades_by_subject[subject])

        self.student_report_card.add_grade(subject, 5)
        self.assertEqual([6, 5], self.student_report_card.grades_by_subject[subject])

        expected_result = "Name: Ivan\nYear: 10\n----------\nMath: 5.50\n----------\nAverage Grade: 5.50"
        self.assertEqual(expected_result, self.student_report_card.__repr__())


if __name__ == '__main__':
    main()
