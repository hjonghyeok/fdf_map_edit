import cv2
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path', help=' : img path')
parser.add_argument('-r', help='resolution: 0.1 ~ 1.0 (default: 0.5)', default='0.5')
parser.add_argument('-n', help='normalize_size: 1 ~ 255 (default: 100)', default='100')
args = parser.parse_args()

def get_unique_filename(output_file):
    if not os.path.exists(output_file):
        return output_file

    base, ext = os.path.splitext(output_file)
    counter = 1

    while True:
        new_output_file = f"{base}_{counter}{ext}"
        if not os.path.exists(new_output_file):
            return new_output_file
        counter += 1

def main(argv, args):
    img_path = args.path
    output_file = os.path.splitext(os.path.basename(img_path))[0] + '.fdf'
    output_file = get_unique_filename(output_file)
    size = float(args.resolution)
    normalize_size = int(args.normalize_size)

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape

    img = cv2.resize(img, dsize=(int(w  * size), int(h * size)))
    img = cv2.normalize(img, None, 0, normalize_size, cv2.NORM_MINMAX)

    with open(output_file, 'w') as file:
        for i in img:
            for j in i:
                file.write(str(j))
                file.write(' ')
            file.write('\n')
    print(output_file)


if __name__ == '__main__':
    argv = sys.argv
    main(argv, args)