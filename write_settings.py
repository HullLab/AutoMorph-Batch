import os


def write_settings_file(settings_text, function):

        settings_output = output_root+os.sep+subdirectory
        print settings_output
        if not os.path.exists(settings_output):
            os.makedirs(settings_output)

        f = open(settings_output+os.sep+function+'_settings.txt', 'w')

        for setting in settings_text:
            f.write(setting+'\n')

        f.close()


def segment_settings(settings):

    if settings['mode'] == "final":
        l = open('dirs_stacks.csv', 'r')

    elif settings['mode'] == "sample":
        threshold = settings['threshold_range']
        l = open('dirs_stacks.txt', 'r')

    else:
        sys.exit("unknown mode")

    for line in l:

        line = line.strip('\n')

        if mode == "final":
            input_directory, threshold = line.split(',')

        elif mode == "sample":
            input_directory = line

        subdirectory = os.path.basename(input_directory)
        source = os.path.basename(input_directory).split('_')[0]

        settings_text = []
        settings_text.append("[settings]")
        settings_text.append("directory = "+settings['raw_stacks_root'])
        settings_text.append("output = "+settings['output_root'])
        settings_text.append("input_ext = "+settings['original_ext'])
        settings_text.append("output_ext = tif")

        settings_text.append("minimum_size = "+settings['minimum_size'])
        settings_text.append("maximum_size = "+settings['maximum_size'])

        settings_text.append("threshold = "+threshold.strip())

        settings_text.append("pixel_size_y = "+settings['pixel_size_y'])
        settings_text.append("pixel_size_x = "+settings['pixel_size_x'])
        settings_text.append("unit = "+settings['unit'])
        settings_text.append("mode = "+setttings['mode'])
        settings_text.append("skip_last_plane = "+settings['skip_last_plane'])
        settings_text.append("scale_bar_length = "+settings['scale_bar_length'])

        settings_text.append("age = "+settings['age'])
        settings_text.append("source = "+source)
        settings_text.append("author = "+settings['author'])
        settings_text.append("location = "+settings['location'])
        settings_text.append("catalog_prefix = "+settings['catalog_prefix'])

        write_settings_file(settings_text, 'segment')
