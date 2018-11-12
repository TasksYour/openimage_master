# Open Images Master

Simple Python script designed to extract labels and associated metadata on the [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html).

With this simple command line tool, you can specify one label you wish to use for your machine learning application. The script will automatically create a folder with all relevant images extracted from the dataset. It will also extract the metadata associated with it, including the bounding boxes of the associated label.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Implementation obviously requires the 9 parts of the [dataset](https://storage.googleapis.com/openimages/web/index.html) zip files to be downloaded in a data directory created at the root of the git folder. Metadata files (class-descriptions-boxable.csv and train-annotations-bbox.csv) are also required.

### Prerequisites

What things you need to install the software and how to install them. Python3 libraries are in requirements.txt for easy installation with pip.

- Linux >= 4.17.11
- Python >= 3.7.0
- [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)

Earlier program/package versions might work too but haven't been tested.

### Installing

A step by step series of examples that tell you how to get a development env running.

Simply clone the repository.

```bash
git clone https://github.com/julienstark/openimages_master.git
```

Create a data/ folder at the root of the git project and move the dataset zip files there as well as the metadata files.

```bash
mkdir openimages_master/data
mv train_0*.zip openimages_master/data
```

And that's it !

### Running

```bash
python3 main.py --label 'label' --folder 'folder'
```

Replace "label" by the label you wish to extract. Available labels are in the data folder > class-description-boxable.csv.

Replace "folder" by the absolute path of the folder you wish to have the images and metadata extracted to.

#### IMPORTANT

Please make sure that you have enough space on the extracted destination since some labels contain several thousand of images.

During the extraction process, the implementation temporarily extracts the content of each zip files, one at a time, to a temporary folder. This temporary folder is located in the directory where the main.py file is executed. Please make sure that you have enough disk space at this location to avoid program crash during extraction. All temporary files are deleted at the end of the program.
