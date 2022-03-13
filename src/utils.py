import os
import logging


FORMAT = "%(asctime)-15s [%(filename)s:%(lineno)s - %(funcName)2s() ] %(message)s"
logging.basicConfig(
    format=FORMAT, level=logging.getLevelName('INFO'))
LOGGER = logging.getLogger(__name__)


def get_data_path():
    """
    Regardless of one's computer, return absolute path to data folder
    :return: str, absolute path to data folder
    """
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, "data")


def preprocess_file(file_name):
    """
    Preprocess raw files to create a mower config dictionary
    :param file_name: Name of the file (it should be within data folder
    :return: config dictionary of mower
    """
    try:
        with open(get_data_path() + "/" + file_name, "r") as file:
            input_ = file.readlines()
        LOGGER.info("Successfully read file {}.".format(file_name))
        mowers = {}
        # Get limits - being always first line
        limits = [int(val) for val in input_[0].split()]
        LOGGER.info("Successfully parsed field limits.".format(limits))

        # Initializing mower id
        mower_id = 1

        # Read other lines of the file - being position and commands for each mower
        for line_id in range(1, len(input_)):
            # position is always in odd lines
            if line_id % 2 != 0:
                raw_pos = input_[line_id].rstrip("\n").split()
                pos = [int(val) for val in raw_pos[:2]]
                dir_ = raw_pos[2]

                # Commands are always in following line
                commands = list(input_[line_id + 1].rstrip("\n"))
                mowers[mower_id] = {"pos": pos, "dir": dir_, "commands": commands, "limits": limits}
                LOGGER.info("Successfully parsed mower {} config {}.".format(mower_id, mowers[mower_id]))

                # Update next mower id
                mower_id += 1
        return mowers
    except FileNotFoundError:
        LOGGER.error("File doesn't exist in data folder.")


if __name__ == '__main__':
    preprocess_file("test.txt")
