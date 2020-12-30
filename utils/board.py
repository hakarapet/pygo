class Board:
    def __init__(self, size=19):
        """
            Creates the board.
            Returns an empty list of lists as a nxn matrix.

            Attributes:
                n - as the nxn size board. Possible
                variants are: 9x9, 13x13, 19x19

            Returns:
                an nxn sized list of None-s
        """
        self.size = size
        self.board = []
        self.board_type = f"{self.size}x{self.size}"

        if not (self.size == 9 or self.size == 13 or self.size == 19):
            raise AttributeError("Attribute can be only: 9, 13, 19")

        for i in range(0, self.size):
            for j in range(0, self.size):
                self.board.append({"x": i, "y": j, "val": None})

    def val_check(self, val):
        """
            Private function to test the setting values

            Attributes:
            val - value can be B or W
        """
        if val not in ["B", "W", None]:
            raise AttributeError("Wrong value. Values can be either 'B', 'W' or None")
        return True

    def get_position(self, x, y):
        """
            Gets value of the givven position

            Attributes:
                x and y coordinates
            Returns:
                A dict data with coordinates and the value
        """
        if x * y > self.size ** 2:
            raise AttributeError(f"Givven coordinates {x} and {y} are off the board")

        for element in self.board:
            if element["x"] == x and element["y"] == y:
                return element

    def set_position(self, x, y, val):
        """
            Sets the value of the givven position if it is not empty

            Attributes:
                x,y - coordinates
                val - "B" - black, "W" - white
            Returns:
                Boolean
        """
        if self.val_check(val):
            position = self.get_position(x, y)
            if position["val"] == None:
                position["val"] = val
                return True
            else:
                raise Exception(f"The spot is already taken by {position['val']}")

    def is_adjacent(self, x1, y1, x2, y2):
        """
            Checks if two spots are adjacent
            Attributes:
                x1,y1,x2,y2: coordinates of 2 points
            Returns:
                Boolean
        """
        el1 = self.get_position(x1, y1)
        el2 = self.get_position(x2, y2)

        if x1 == x2 and y1 == y2:
            raise AttributeError(
                f"Adjacent cannot be same stones. el1: {el1}, el2: {el2}"
            )
        if el1["val"] == None or el2["val"] == None:
            return False
        if el1["val"] != el2["val"]:
            raise AttributeError(
                f"Adjacent cannot be two stones different color. el1: {el1}, el2: {el2}"
            )
        if el1 != el2:
            is_diagonal = abs(x1 - x2) == 1 and abs(y1 - y2) == 1
            same_spot = (x1 == x2) and (y1 == y2)
            one_step_away_ver = abs(x1 - x2) == 1 and not (abs(y1 - y2) == 1)
            one_step_away_hor = abs(y1 - y2) == 1 and not (abs(x1 - x2) == 1)

            if same_spot:
                return False
            elif is_diagonal:
                return False
            elif one_step_away_ver:
                return True
            elif one_step_away_hor:
                return True
            else:
                return False

    def find_next_siblings(self, curr, previous=None, previous_siblings=[]):
        """
            Returns a list of next siblings EXCLUDED previous
            or returns empty list
        """

        curr_x = curr[0]
        curr_y = curr[1]
        siblings = []

        # TODO Refactor
        if (
            self.is_adjacent(curr_x, curr_y, curr_x + 1, curr_y)
            and curr_x + 1 < self.size
        ):
            siblings.append((curr_x + 1, curr_y))

        if self.is_adjacent(curr_x, curr_y, curr_x - 1, curr_y) and curr_x - 1 >= 0:
            siblings.append((curr_x - 1, curr_y))

        if (
            self.is_adjacent(curr_x, curr_y, curr_x, curr_y + 1)
            and curr_y + 1 < self.size
        ):
            siblings.append((curr_x, curr_y + 1))

        if self.is_adjacent(curr_x, curr_y, curr_x, curr_y - 1) and curr_y - 1 >= 0:
            siblings.append((curr_x, curr_y - 1))

        # Excluding the previous
        temp_siblings = list(set([sib for sib in siblings if sib != previous]))

        # Checking if we are in a closed loop of siblings
        result_siblings = list(
            set([s for s in temp_siblings if s not in previous_siblings])
        )

        return result_siblings

    def __search(
        self, curr_spot, goal_spot, previous, previous_siblings=[], saved_siblings=[]
    ):
        """
            Search algorithm of connected group
        """
        next_siblings = self.find_next_siblings(curr_spot, previous, previous_siblings)

        previous = curr_spot

        search_in_siblings = [
            spot
            for spot in next_siblings
            if spot[0] == goal_spot[0] and spot[1] == goal_spot[1]
        ]
        if len(search_in_siblings):
            return True
        elif len(next_siblings) == 1:
            previous_siblings.append(next_siblings[0])
            return self.__search(
                next_siblings[0], goal_spot, previous, previous_siblings, saved_siblings
            )
        elif len(next_siblings) > 1:

            saved_siblings = list(set(saved_siblings + next_siblings[:-1]))
            if next_siblings[-1] not in previous_siblings:
                previous_siblings.append(next_siblings[-1])

            return self.__search(
                next_siblings[-1],
                goal_spot,
                previous,
                previous_siblings,
                saved_siblings,
            )
        elif len(saved_siblings):
            previous_siblings.append(saved_siblings[-1])
            previous_siblings = list(set(previous_siblings))
            return self.__search(
                saved_siblings[-1],
                goal_spot,
                previous,
                previous_siblings,
                saved_siblings[:-1],
            )
        else:
            return False

    def is_connected_group(self, x1, y1, x2, y2):
        """
            Checks if two spots are in a adjacent adjacent
            Attributes:
                x1,y1,x2,y2: coordinates of 2 distinct points
            Returns:
                Boolean
        """
        if self.is_adjacent(x1, y1, x2, y2):
            return True

        # Pickes closest to zero point
        start_spot = (x1, y1) if x1 + y1 < x2 + y2 else (x2, y2)

        # TODO change the way goal spot is selected
        goal_spot = (x1, y1) if x1 + y1 > x2 + y2 else (x2, y2)

        # defining previous with initial starter/closest to zero
        previous = start_spot

        result = self.__search(start_spot, goal_spot, previous, [], [])

        return result

    # ##### LIBERTIES #####

    def has_liberties(self, x, y, val, previous=None):
        liberties = []

        for xi in range(x - 1, x + 2, 2):
            if xi > self.size or previous == (xi, y):
                continue
            pos_x_val = self.get_position(xi, y)["val"]
            if pos_x_val == None:
                liberties.append((xi, y))
            elif pos_x_val == val:
                liberties += self.has_liberties(xi, y, val, (x, y))[1]

        for yi in range(y - 1, y + 2, 2):
            if yi > self.size or previous == (x, yi):
                continue
            pos_y_val = self.get_position(x, yi)["val"]
            if pos_y_val == None:
                liberties.append((x, yi))
            elif pos_y_val == val:
                liberties += self.has_liberties(x, yi, val, (x, y))[1]

        return (True, list(set(liberties))) if len(liberties) else (False, liberties)
