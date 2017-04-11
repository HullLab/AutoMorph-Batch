import os
import sys
import argparse
import shutil

# location of original stacks to be segmented
raw_images_root = "/gpfs/scratch60/geo/hull/data/porosity"
# location of output from segment
output_root = "/home/fas/hull/jeb247/project/porosity_segmented/round2/"


def list_dirs_originals(raw_images_root):

    f = open('dirs_stacks.txt', 'w')
    for root, dirs, files in os.walk(raw_images_root):
        if len(dirs) == 0:
            f.write(root+'\n')
    f.close()


def list_dirs_segmented(output_root):

    f = open('dirs_segmented.txt', 'w')
    for root, dirs, files in os.walk(output_root):
        if len(dirs) == 0 or 'final' in dirs or 'sample' in dirs:
            if 'final' not in root and 'sample' not in root:
                f.write(root+'\n')

    f.close()

    shutil.copy('dirs_stacks.txt', 'dirs_stacks.csv')


def list_dirs_focused(output_root):

    f = open('dirs_focused.txt', 'w')
    for root, dirs, files in os.walk(output_root):
        if os.path.basename(root) == 'final':
            if 'focused_unlabeled' in dirs:
                f.write(os.path.dirname(root)+'\n')
            dirs[:] = []

    f.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('phase', help='specify: presegment, segmented or focused')
    args = parser.parse_args()

    if args.phase == 'presegment':
        list_dirs_originals(raw_images_root)
        list_dirs_segmented(output_root)

    elif args.phase == 'segmented':
        list_dirs_segment(output_root)
    elif args.phase == 'focused':
        list_dirs_focused(output_root)
    else:
        sys.exit('Unknown phase. Specify presegment, segmented or focused')

