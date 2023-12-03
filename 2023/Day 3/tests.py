import unittest

from board import Board, Field, FieldGroup, FieldGroupNum


class Test_Field_get_set_value(unittest.TestCase):
    def setUp(self):
        self.field = Field(20, 30, 3)


    def test_Field_get_value_not_changed(self):
        self.assertEqual(self.field.value, 3)


    def test_Field_get_value_changed(self):
        self.field.value = "r"
        self.assertEqual(self.field.value, "r")


    def test_Field_set_incorrect_value(self):
        with self.assertRaises(ValueError):
            self.field.value = ("1234")


class Test_Field_value_is_digit(unittest.TestCase):
    def test_Field_value_is_digit(self):
        self.field = Field(20, 30, "4")
        expected = True
        self.assertEqual(self.field.value_is_digit(), expected)


    def test_Field_value_is_not_digit(self):
        self.field = Field(20, 30, "r")
        expected = False
        self.assertEqual(self.field.value_is_digit(), expected)


class Test_Board_property_sizes(unittest.TestCase):

    def setUp(self):
        self.board = Board(20, 30)


    def test_Board_x_size(self):
        self.assertEqual(self.board.x_size, 20)


    def test_Board_y_size(self):
        self.assertEqual(self.board.y_size, 30)


    def test_Field_value_is_not_digit(self):
        self.field = Field(20, 30, "r")
        expected = False
        self.assertEqual(self.field.value_is_digit(), expected)


class Test_Board_validate_coordinates(unittest.TestCase):

    def setUp(self):
        self.board = Board(20, 30)

    def test_Board_validate_coordinates_positive(self):
        expected = True
        self.assertEqual(self.board.validate_coordinates(2, 3), expected)

    def test_Board_validate_coordinates_one_negative(self):
        expected = False
        self.assertEqual(self.board.validate_coordinates(20, 3), expected)


    def test_Board_validate_coordinates_both_negative(self):
        expected = False
        self.assertEqual(self.board.validate_coordinates(20, 30), expected)


class Test_Board_get_set_field_value(unittest.TestCase):

    def setUp(self):
        self.board = Board(20, 30)

    def test_Board_get_set_field_value(self):
        self.board.set_field_value(2, 3, "e")
        self.assertEqual(self.board.get_board_el(2, 3), "e")


class Test_Board_get_list_of_values(unittest.TestCase):

    def setUp(self):
        self.board = Board(20, 30)

    def test_Board_get_set_field_value(self):
        self.board.set_field_value(2, 3, "e")
        self.board.set_field_value(5, 8, "4")
        self.assertEqual(self.board.get_list_of_values([(2,3), (5,8)]), ["e", "4"])


class Test_Board_calculate_borders(unittest.TestCase):

    def setUp(self):
        self.board = Board(20, 30)

    def test_Board_calculate_possible_borders(self):
        input_x = 10
        input_y = 10
        expected = {(9,11), (10,11), (11,11),
                    (9,10),         (11,10),
                    (9,9), (10,9), (11,9)}
        self.assertEqual(self.board._calculate_possible_borders(input_x, input_y), expected)


class Test_FieldGroupNum_validate_cords(unittest.TestCase):

    def setUp(self):
        self.g = FieldGroup()

    def test_FieldGroup_validate_cords_xcords_positive(self):
        x_cords = [9, 10, 11]
        self.assertEqual(self.g._validate_x_cords(x_cords), True)


    def test_FieldGroup_validate_cords_xcords_negative(self):
        x_cords = [9, 10, 12]
        self.assertEqual(self.g._validate_x_cords(x_cords), False)


    def test_FieldGroupN_validate_cords_ycords_positive(self):
        y_cords = [9, 9, 9]
        self.assertEqual(self.g._validate_y_cords(y_cords), True)


    def test_FieldGroup_validate_cords_ycords_negative(self):
        y_cords = [9, 10, 15]
        self.assertEqual(self.g._validate_y_cords(y_cords), False)


class Test_FieldGroupNum_create_num(unittest.TestCase):

    def test_FieldGroupNum_create_num_sorted_in_input(self):
        gn = FieldGroupNum(Field(1, 2, "5"), Field(1, 3, "6"))
        self.assertEqual(gn.create_num(), 56)


    def test_FieldGroupNum_create_num_not_sorted_in_input(self):
        gn = FieldGroupNum(Field(1,3, "5"), Field(1, 2, "6"))
        self.assertEqual(gn.create_num(), 56)


class Test_FieldGroupNum_validate_values(unittest.TestCase):

    def setUp(self):
        self.gn = FieldGroupNum()

    def test_FieldGroupNum_validate_values_positive(self):
        values = ["9", "1", "5"]
        self.assertEqual(self.gn._validate_values(values), True)


    def test_FieldGroupNum_validate_values_negative(self):
        values = ["9", "g", "5"]
        self.assertEqual(self.gn._validate_values(values), False)