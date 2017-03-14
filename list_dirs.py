from os import walk
import shutil

# location of original stacks to be segmented
raw_images_root = ""
# location of output from segment
output_root = ""


def list_dirs(raw_images_root, output_root):

    f = open('dirs_stacks.txt', 'w')
    for root, dirs, files in walk(raw_images_root):
        if len(dirs) == 0:
            f.write(root+'\n')
    f.close()

    f = open('dirs_segmented.txt', 'w')
    for root, dirs, files in walk(output_root):
        if len(dirs) == 0 or 'final' in dirs or 'sample' in dirs:
            if 'final' not in root and 'sample' not in root:
                f.write(root+'\n')

    f.close()

    shutil.copy('dirs_stacks.txt', 'dirs_stacks.csv')


if __name__ == "__main__":

    list_dirs(raw_images_root, output_root)
