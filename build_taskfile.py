import argparse

directory_list = 'dirs_segmented.txt'

function_list = ['segment', 'focus', '2dmorph', '3dmorph']


def build_taskfile(function):

    if function not in function_list:
        print 'Error: unknown function specified. Choose from: %s' % ', '.join(function_list)
        sys.exit(1)

    # output filename for tasklist
    f = open('taskfile_'+function+'.txt', 'w')
    # input list of directories
    l = open(directory_list, 'r')

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

    parser.add_argument('function', help='specify AutoMorph function: %s' % ', '.join(function_list))
    args = parser.parse_args()

    build_taskfile(args.function)
