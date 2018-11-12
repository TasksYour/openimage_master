"""
MODULE_DOCSTRING_PLACEHOLDER
"""


import os
import argparse

import translator
import picker


def parser():
    """FUNCTION_DOCSTRING_PLACEHOLDER
    """

    parse = argparse.ArgumentParser(description="Open Images Master helper."
                                                " Automatically extracts a "
                                                "label from the Open Images "
                                                "dataset")
    parse.add_argument("-l", "--label", help="label string to extract",
                       required=True, type=str)
    parse.add_argument("-f", "--folder",
                       help="absolute path of the target folder",
                       required=True, type=str)
    args = vars(parse.parse_args())

    return (args['label'], args['folder'])


def main():
    """FUNCTION_DOCSTRING_PLACEHOLDER
    """

    label, target_directory = parser()

    current_path = os.path.dirname(os.path.realpath(__file__))

    trs = translator.Translator(os.path.join(current_path, "data/",
                                             "class-descriptions-boxable.csv"),
                                os.path.join(current_path, "data/",
                                             "train-annotations-bbox.csv"))

    pick = picker.Picker(os.path.join(current_path, "data/", "train_00.zip"),
                         target_directory)

    print("Gathering class metadata...")
    try:
        class_meta = trs.get_class_meta(trs.classdict[label])
    except KeyError as err:
        raise type(err)('label \'' + label + '\' not found')

    print("Creating folder: " + pick.create_destination_folder() + "\n")

    for zip_number in range(9):
        print("***** ZIP 0" + str(zip_number) + " *****")
        pick.zipname = os.path.join(current_path, "data/",
                                    "train_0" + str(zip_number) + ".zip")
        print("Starting extraction")
        pick.extract_image([x[0] for x in class_meta], target_directory)
        print("*****************\n")

    print("Extraction completed for label: " + label + ". Your files are in: " +
          target_directory)


if __name__ == '__main__':
    main()
