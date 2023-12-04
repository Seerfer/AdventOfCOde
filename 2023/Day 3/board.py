from dataclasses import dataclass
from typing import Optional, List, Tuple, Set


@dataclass
class Field:
    _x: int
    _y: int
    _value: Optional[str] = None

    @property
    def value(self) -> str:
        return self._value

    @property
    def x(self) -> int:
        return self._x


    @property
    def y(self) -> int:
        return self._y


    @value.setter
    def value(self, v: str) -> None:
        if len(str(v)) != 1:
            raise ValueError("Value must be a char")
        self._value = v

    def value_is_digit(self):
        return self._value.isdigit()


class FieldGroup:
    def __init__(self, *args: Field):
        self._fields = [a for a in args]
        if self._validate_fields() is False:
            raise ValueError("Validation of fields did not pass")


    def _validate_fields(self):
        x_cords = [a.x for a in self.fields]
        y_cords = [a.y for a in self.fields]
        return self._validate_x_cords(x_cords) and self._validate_y_cords(y_cords)

    @staticmethod
    def _validate_x_cords(x_cords: List[int]) -> bool:
        return sorted(x_cords) == list(range(min(x_cords), max(x_cords) + 1))

    @staticmethod
    def _validate_y_cords(y_cords: List[int]) -> bool:
        return len(set(y_cords)) == 1


    @property
    def fields(self):
        return self._fields

    @property
    def cords(self):
        return [(f.x, f.x) for f in self.fields]

    @property
    def values(self):
        return [f.value for f in self.fields]



class FieldGroupNum(FieldGroup):
    def __init__(self, *args: Field):
        super().__init__(*args)
        self._num = self.create_num()



    def create_num(self):
        sorted_by_x = sorted(self.fields, key=lambda f: f.x)
        values = [f.value for f in sorted_by_x]
        return int("".join(values))

    def validate(self):
        return self._validate_fields() and self._validate_values()

    @staticmethod
    def _validate_values(values: List[str]) -> bool:
        return all([v.isdigit() for v in values])


    @property
    def num(self):
        return self._num




class Board:
    def __init__(self, x_size, y_size):
        self.fields = [[Field(i, j) for j in range(y_size)] for i in range(x_size)]

    def get_board_el(self, x: int, y: int) -> str:
        if self.validate_coordinates(x,y):
            return self.fields[x][y].value
        raise ValueError("Index out of range")

    def set_field_value(self, x: int, y: int, value: str) -> None:
        self.fields[x][y].value = value

    @property
    def x_size(self):
        return len(self.fields)

    @property
    def y_size(self):
        return len(self.fields[0])

    def validate_coordinates(self, x, y):
        return (x in range(0, self.x_size) and y in range(0, self.y_size))

    def get_list_of_values(self, values=List[Tuple[int, int]]) -> List[str]:
        return [self.get_board_el(x, y) for x,y in values]

    @staticmethod
    def _calculate_possible_borders(x:int, y:int) -> Set[Tuple[int, int]]:
        return {(x-1,y+1), (x,y+1), (x+1,y+1),
                (x-1, y),           (x+1,y),
                (x-1,y-1),(x,y-1),(x+1,y-1)}

    def get_field_borders(self, x, y) -> List[str]:
        possible_borders_coordinates = self._calculate_possible_borders(x,y)
        valid_borders = [(x,y) for x,y in possible_borders_coordinates if self.validate_coordinates(x,y)]
        return self.get_list_of_values(valid_borders)


    def get_group_borders(self, group: FieldGroup):
        return list({self.get_field_borders(f.x, f.y) for f in group.fields})


    def get_group_border(self, group: FieldGroup):
        return {self.get_field_borders(cord[0], cord[1]) for cord in FieldGroup.cords}
