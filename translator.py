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
        self._classdict = self.init_classdict()


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


    def init_classdict(self):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        if not os.path.exists(self._classfile):
            print("Warning: path " + self._classfile + " does not exist!")
            print("Initializing classdict as None!")
            return None

        classdict = {}

        with open(self._classfile, 'r') as filedesc:
            for line in filedesc:
                linesplit = line.split(',')
                classdict[linesplit[1].rstrip('\n')] = linesplit[0]

        return classdict


    @property
    def classdict(self):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        return self._classdict


    @classdict.setter
    def classdict(self):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        self._classdict = self.init_classdict()


    def get_class_meta(self, label):
        """FUNCTION_DOCSTRING_PLACEHOLDER
        """

        if self._classdict is None:
            print("No valid classdict available. Returning None.")
            return None

        class_meta = []

        with open(self._manifestfile, 'r') as filedesc:
            for line in filedesc:
                linesplit = line.split(',')
                if linesplit[2] == label:
                    class_meta.append([linesplit[0] + '.jpg', linesplit[4],
                                       linesplit[5], linesplit[6],
                                       linesplit[7]])

        return class_meta


def write_metadata(class_meta, label, meta_filename=None):
    """FUNCTION_DOCSTRING_PLACEHOLDER
    """

    if meta_filename is None:
        meta_filename = label + ".txt"

    if os.path.exists(meta_filename):
        print("Warning: file " + meta_filename + " already exists.")
        print("Appending class metadata at the end of the file.")

    with open(meta_filename, 'a') as filedesc:
        filedesc.write('ImageId Xmin Xmax Ymin Ymax\n')
        for entry in class_meta:
            filedesc.write(entry[0] + ' ' + entry[1] + ' ' + entry[2]
                           + ' ' + entry[3] + ' ' + entry[4] + '\n')
