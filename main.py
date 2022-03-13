from src.tondeuse import MowerClass
from src.utils import LOGGER, preprocess_file
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description='Controls a list of mower using a config file.')
    parser.add_argument('--file', required=True, help='Name of the file. File has to be located in data folder.')
    return parser


def main(filename):
    # Read source file
    mowers = preprocess_file(filename)
    result = {}
    occupied = []
    for mower_id, mower_config in mowers.items():
        LOGGER.info("Mower {} - process started.".format(mower_id))
        my_mower = MowerClass(mower_id, mower_config["limits"], mower_config["pos"], mower_config["dir"])
        for command in mower_config["commands"]:
            LOGGER.info("Running command {}.".format(command))
            if command == "A":
                my_mower.next_pos(occupied)
            elif command == "D":
                my_mower.next_dir_d()
            elif command == "G":
                my_mower.next_dir_g()
            else:
                LOGGER.warn("Invalid command {}.".format(command))
                pass
        result[mower_id] = {"pos": my_mower.pos, "dir": my_mower.dir}
        occupied.append(my_mower.pos)
    print(result)


if __name__ == '__main__':
    file_name = get_arguments().parse_args().file
    main(file_name)
