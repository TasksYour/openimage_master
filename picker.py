"""
MODULE_DOCSTRING_PLACEHOLDER
"""


import os
import shutil
import zipfile


class Picker:
    """Class responsible for creating folders, identifying and extracting
    required labelled images to a specific folder.

    CLASS_DOCSTRING_PLACEHOLDER
    """


    def __init__(self, zipname=None, foldername=None):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        if not os.path.exists(zipname):
            print("Warning: path " + zipname + " does not exist!")

        self._zipname = zipname
        self._foldername = foldername


    @property
    def zipname(self):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        return self._zipname


    @zipname.setter
    def zipname(self, zipname):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        if not os.path.exists(zipname):
            print("Warning: path " + zipname + " does not exist!")

        self._zipname = zipname


    @property
    def foldername(self):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        return self._foldername


    @foldername.setter
    def foldername(self, foldername):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        self._foldername = foldername


    def create_destination_folder(self, path=None):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        if self._foldername:

            if not path:
                path = os.getcwd()

            target_dir = os.path.join(path, self._foldername)

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            else:
                raise OSError("Path " + target_dir + " already exists.")

            return target_dir

        raise NameError("Target foldername has not been defined.")


    def extract_image(self, image_name, target_dir):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        if self._zipname:

            print("Unzip " + self._zipname + " to temp folder...", end='')

            temp_extract = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                        "temp_extract/")

            zip_foldername = self._zipname.split("/")[-1].rstrip(".zip") + "/"

            temp_foldername = os.path.join(temp_extract, zip_foldername)

            if not os.path.exists(temp_extract):
                os.makedirs(temp_extract)

            with zipfile.ZipFile(self._zipname) as zip_file:
                zip_file.extractall(temp_extract)
            print("done")

            extracted_img = [x for x in os.listdir(temp_foldername) if x in image_name]

            image_count = 0

            print("Moving target images to " + target_dir + "...", end='')
            for target_image in extracted_img:
                shutil.move(os.path.join(temp_foldername, target_image),
                            os.path.join(target_dir, target_image))
                image_count += 1
            print("done")

            print(self._zipname + ": extraction completed. " +
                  str(image_count) + " images extracted.")

            shutil.rmtree(temp_extract)

        else:

            raise NameError("Target zipfile has not been defined.")
