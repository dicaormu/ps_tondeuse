# Main constructors: field and MowerClass
from src.utils import LOGGER, PositionError


class FieldClass:
    """Field delimitations"""
    min_x = 0
    min_y = 0

    # Constructor FieldClass
    def __init__(self, limits):
        """
        Initializes field parameters given limits
        :param limits: list composer of limits position [x,y]
        """
        FieldClass.max_x = int(limits[0])
        FieldClass.max_y = int(limits[1])
        LOGGER.info("Successfully initialized field params: O(%s; %s), L(%s; %s).",
                    self.min_x, self.min_y, limits[0], limits[1])


class MowerClass(FieldClass):
    """Mower constructor"""

    # Constructor MowerClass
    def __init__(self, mower_id, limits, pos, dir_):
        """
        Initializes mowers class and movements
        :param mower_id: Id of the mower
        :param pos: Position of the mower as a list [x, y]
        :param dir_: orientation among following list: N,E,W,S
        """
        # id of the MowerClass
        super().__init__(limits)
        self.mower_id = mower_id
        self.pos = pos
        self.dir = dir_
        LOGGER.info("Successfully initialized mower: Id %s.", mower_id)

    def is_valid(self, pos):
        """
        Checks if position is valid according to field limits
        :param pos: actual position [x, y, 0]
        :return: raise error or pass
        """
        # Position within field
        if pos[0] in range(self.min_x, self.max_x + 1) and pos[1] in range(self.min_y, self.max_y + 1):
            pass
        else:
            raise PositionError

    def next_pos(self, occupied=None):
        """
        Sets mower to next position
        :param: occupied: list of occupied positions
        :return: position as a list [x, y]
        """
        new_pos = self.pos
        if self.dir == "N":
            try:
                new_pos = [self.pos[0], self.pos[1] + 1]
                self.is_valid(new_pos)
                is_occupied(new_pos, occupied)
            except PositionError:
                LOGGER.info("Position not valid or occupied ... Skipping command.")
                new_pos = self.pos
        if self.dir == "E":
            try:
                new_pos = [self.pos[0] + 1, self.pos[1]]
                self.is_valid(new_pos)
                is_occupied(new_pos, occupied)
            except PositionError:
                LOGGER.info("Position not valid or occupied ... Skipping command.")
                new_pos = self.pos
        if self.dir == "W":
            try:
                new_pos = [self.pos[0] - 1, self.pos[1]]
                self.is_valid(new_pos)
                is_occupied(new_pos, occupied)
            except PositionError:
                LOGGER.info("Position not valid or occupied ... Skipping command.")
                new_pos = self.pos
        if self.dir == "S":
            try:
                new_pos = [self.pos[0], self.pos[1] - 1]
                self.is_valid(new_pos)
                is_occupied(new_pos, occupied)
            except PositionError:
                LOGGER.info("Position not valid or occupied ... Skipping command.")
                new_pos = self.pos
        self.pos = new_pos
        LOGGER.info("Mower position is set to: (%s; %s).", self.pos[0], self.pos[1])

    def next_dir_g(self):
        """
        Switches mower to next direction if command is g
        :return: position as a letter amongst N,W,E,S
        """
        dir_ = self.dir
        if self.dir == "N":
            dir_ = "W"
        elif self.dir == "W":
            dir_ = "S"
        elif self.dir == "S":
            dir_ = "E"
        elif self.dir == "E":
            dir_ = "N"
        self.dir = dir_
        LOGGER.info('New position is %s.', self.dir)

    def next_dir_d(self):
        """
        Switches mower to next direction if command is d
        :return: position as a letter amongst N,W,E,S
        """
        dir_ = self.dir
        if self.dir == "N":
            dir_ = "E"
        elif self.dir == "E":
            dir_ = "S"
        elif self.dir == "S":
            dir_ = "W"
        elif self.dir == "W":
            dir_ = "N"
        self.dir = dir_
        LOGGER.info('New position is %s.', self.dir)


def is_occupied(pos, occupied=None):
    """
    Checks if position could be occupied
    :param pos: actual position [x, y, 0]
    :param occupied: list of occupied positions [[x, y, 0], [a, b, 0]]
    :return: raise PositionError or pass
    """
    # Position within field
    if not occupied:
        pass
    else:
        for pos_ in occupied:
            if pos[:2] == pos_[:2]:
                raise PositionError


if __name__ == "__main__":
    my_mower = MowerClass(1, [5, 5], [0, 1], "N")
    my_mower.next_pos(occupied=[[0, 2, "N"]])
    # print(my_mower.max_x)
