import matplotlib.pyplot as plt
import matplotlib.image as img
import imageio
import pydicom
from pydicom.data import get_testdata_file

#img = img.imread("/home/felipe/Escritorio/Python-OPencv/IMG/IMG10.dcm")

img = get_testdata_file("/home/felipe/Escritorio/Python-OPencv/IMG/IMG10.dcm")
lecimg = pydicom.dcmread(img)
print(lecimgz)