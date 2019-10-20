import matplotlib.pyplot as plt
import cv2
import sys


if len(sys.argv) < 2:
    print('Please enter filename')
    sys.exit()

file_path = ''.join([x + ' ' for x in sys.argv[1:]])[:-1]
extension = file_path.split('.')[-1]
file_name = ''.join([x + '.' for x in file_path.split('.')[:-1]])[:-1]
# print(file_name, file_path, extension)
image = cv2.imread(file_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

name_res = {
    '_placehold.jpg': (129, 230),
    '_lg.jpg': (1125, 1999),
    file_name + '.jpg': (1080, 1920),
    '_thumb@2x.jpg': (602, 1070),
    '_md.jpg': (557, 991),
    '_xs.jpg': (323, 575),
    '_thumb.jpg': (301, 535),
    '_sm.jpg': (431, 767)
}

for key, value in name_res.items():
    img = cv2.resize(image, value[::-1])
    plt.imsave(file_name + key, img)




