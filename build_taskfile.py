import argparse
import sys
import os

function_list = ['segment', 'focus', '2dmorph', '3dmorph']

def build_taskfile(function, directory_list = None):

    if directory_list == None:
        directory_list = 'dirs_segmented.txt'

    if function not in function_list:
        print 'Error: unknown function specified. Choose from: %s' % ', '.join(function_list)
        sys.exit(1)

    #output filename for tasklist
    f = open('taskfile_'+function+'.txt', 'w')
    #input list of directories
    l = open(directory_list,'r')

    for line in l:
        directory = line.strip('\n')
        task = []
        task.append('source ~/.bashrc')
        task.append('cd '+directory)

        if function == 'segment':
            task.append('segment segment_settings.txt')
        elif function == 'focus':
            task.append('focus final')
        elif function == '2dmorph':
            task.append('run2dmorph 2dmorph_settings.txt')
        elif function == '3dmorph':
            task.append('run3dmorph 3dmorph_settings.txt')
        else:
            sys.exit(1)

        task_string = "; ".join(task)
        f.write(task_string+'\n')

    f.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('function', help='specify AutoMorph function', choices = function_list)
    parser.add_argument('-d', '--dirs', help="directory list file (required for 2d and 3d morph)")
    args = parser.parse_args()

    if args.function in ['2dmorph', '3dmorph']:
        if args.dirs == None :
            sys.exit('directory list is required for 2d and 3dmorph. Specify with -d <dir_list>.')
        else:
            if os.path.exists(args.dirs):
                build_taskfile(args.function, args.dirs)
            else:
                sys.exit('File %s not found' % args.dirs)

    build_taskfile(args.function)
