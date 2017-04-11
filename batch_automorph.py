import os
import list_dirs
import write_settings
import build_taskfile

function_list = ['segment_sample', 'segment_final', 'focus', '2dmorph', '3dmorph']


def load_settings(function):

    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'automorph.cfg')

    if not os.path.exists(filename):

        parser = ConfigParser.SafeConfigParser()
        parser.optionxform = str  # preserve case
        parser.read(filename)

    settings = {}

    for setting in parser.options('global'):
        settings[setting] = str(parser.get('global', setting))

    for setting in parser.options('metadata'):
        settings[setting] = str(parser.get('global', setting))

    if 'segment' in function:
        section = 'segment'
        settings['mode'] = function.strip('segment_')
    else:
        section = function

    for setting in parser.options(section):
        settings[setting] = str(parser.get(section, setting))

    return settings


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('function', help='specify AutoMorph function: %s' % ', '.join(function_list))
    args = parser.parse_args()

    if args.function not in function_list:
        print 'Error: unknown function specified. Choose from: %s' % ', '.join(function_list)
        sys.exit(1)

    settings = load_settings(function)

    if not os.path.exists('dirs_stacks.txt'):
        list_dirs.list_dirs(raw_images_root, output_root)

    if 'segment' in function:
        write_settings.segment_settings(settings)
        build_taskfile.build_taskfile('segment')

    elif '2dmorph' in function:
        write_settings.twodmorph_settings(settings)
        build_taskfile.build_taskfile('2dmorph')

    elif '3dmorph' in function:
        write_settings.threedmorph_settings(settings)
        build_taskfile.build_taskfile('3dmorph')

