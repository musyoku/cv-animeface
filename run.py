# -*- coding: utf-8 -*-
import argparse, cv2, sys, os, re

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--source_dir", type=str)
parser.add_argument("-o", "--output_dir", type=str, default="out")
parser.add_argument("-s", "--size", type=int, default=64)
args = parser.parse_args()

def main():
	cascade_filename = "lbpcascade_animeface.xml"
	if not os.path.isfile(cascade_filename):
		raise RuntimeError("%s not found" % cascade_filename)
	cascade = cv2.CascadeClassifier(cascade_filename)

	try:
		os.mkdir(args.output_dir)
	except:
		pass

	print args.source_dir
	dirs = os.listdir(args.source_dir)
	index = 0
	pattern = r"\.(png|jpeg|jpg)$"
	pattern = re.compile(pattern)
	for dirname in dirs:
		dirpath = "{}/{}".format(args.source_dir, dirname)
		if os.path.isdir(dirpath):
			print dirname
			files = os.listdir(dirpath)
			for i, filename in enumerate(files):
				if pattern.search(filename) is not None:
					filepath = "{}/{}".format(dirpath, filename)
					sys.stdout.write("Processing ({}/{}) {}\r".format(i, len(files), filename))
					sys.stdout.flush()
					image = cv2.imread(filepath)
					gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
					gray = cv2.equalizeHist(gray)
					faces = cascade.detectMultiScale(gray,
						 scaleFactor = 1.1,
						 minNeighbors = 5,
						 minSize = (args.size, args.size))
					for i, (x, y, w, h) in enumerate(faces):
						# cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
						cropped_image = image[y:y + h, x:x + w,:]
						cv2.imwrite("{}/{}.png".format(args.output_dir, index), cv2.resize(cropped_image, (args.size, args.size)))
						index += 1
			print "Done."

if __name__ == '__main__':
	main()
