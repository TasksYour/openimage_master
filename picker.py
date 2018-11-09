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

            with zipfile.ZipFile(self._zipname) as zip_file:

                for member in zip_file.namelist():
                    filename = os.path.basename(member)
                    # skip directories and random labels
                    if not filename or filename is not image_name:
                        continue

                    # copy file (taken from zipfile's extract)
                    source = zip_file.open(member)
                    target = open(os.path.join(target_dir, filename), "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)

        else:

            raise NameError("Target zipfile has not been defined.")
