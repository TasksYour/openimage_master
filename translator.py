"""
MODULE_DOCSTRING_PLACEHOLDER
"""


import os


class Translator:
    """CLASS_DOCSTRING_PLACEHOLDER
    """


    def __init__(self, classfile, manifestfile):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        if not os.path.exists(classfile):
            print("Warning: path " + classfile + " does not exist!")

        if not os.path.exists(manifestfile):
            print("Warning: path " + manifestfile + " does not exist!")

        self._classfile = classfile
        self._manifestfile = manifestfile


    @property
    def classfile(self):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        return self._classfile


    @classfile.setter
    def classfile(self, classfile):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        if not os.path.exists(classfile):
            print("Warning: path " + classfile + " does not exist!")

        self._classfile = classfile


    @property
    def manifestfile(self):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        return self._manifestfile


    @manifestfile.setter
    def manifestfile(self, manifestfile):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        if not os.path.exists(manifestfile):
            print("Warning: path " + manifestfile + " does not exist!")

        self._manifestfile = manifestfile
