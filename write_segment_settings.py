import os

output_root = "/home/fas/hull/jeb247/project/porosity_segmented"
mode = "final"

if mode == "final":
    l = open('dirs_stacks.csv', 'r')
elif mode == "sample":
    threshold_range = "0.15-0.25 by 0.01"
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
    settings_text.append("directory = "+input_directory)
    settings_text.append("output = "+output_root)
    settings_text.append("input_ext = tif")
    settings_text.append("output_ext = tif")

    settings_text.append("minimum_size = 100.0")
    settings_text.append("maximum_size = 2000.0")

    if mode == "final":
        settings_text.append("threshold = "+threshold.strip())
    elif mode == "sample":
        settings_text.append("threshold = "+threshold_range)

    settings_text.append("pixel_size_y = 0.48")
    settings_text.append("pixel_size_x = 0.48")
    settings_text.append("unit = um")
    settings_text.append("mode = "+mode)
    settings_text.append("skip_last_plane = True")
    settings_text.append("scale_bar_length = 100")

    settings_text.append("age = Recent")
    settings_text.append("source = "+source)
    settings_text.append("author = The Hull Lab")
    settings_text.append("location = Yale Peabody Museum")
    settings_text.append("catalog_prefix = UCMP")

    settings_output = output_root+os.sep+subdirectory
    print settings_output
    if not os.path.exists(settings_output):
        os.makedirs(settings_output)

    f = open(settings_output+os.sep+'segment_settings.txt', 'w')

    for setting in settings_text:
        f.write(setting+'\n')

    f.close()
