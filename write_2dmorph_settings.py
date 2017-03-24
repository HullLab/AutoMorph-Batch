import os

output_directory = '/home/fas/hull/jeb247/project'
twodmorph_run_name = '2dmorph_test'

output_directory += os.sep+twodmorph_run_name

install_dir = '/home/geo/hull/ph269/software/AutoMorph'

l = open('dirs_focused.txt', 'r')

out_dir_list = []

for line in l:

    directory = line.strip()
    print directory
    sampleID = os.path.basename(directory)

    sample_out_directory = output_directory+os.sep+sampleID
    focused_directory = directory+'/final/focused_unlabeled'

    if os.path.exists(focused_directory):

        out_dir_list.append(sample_out_directory)

        if not os.path.exists(sample_out_directory):
                os.makedirs(sample_out_directory)

        settings_text = []
        settings_text.append("directory = " + directory)
        settings_text.append("output_dir = " + sample_out_directory)
        settings_text.append("image_extension = .tif")

        settings_text.append("sampleID = "+sampleID)

        settings_text.append("output_filename = []")
        settings_text.append("microns_per_pixel_Y = 1")
        settings_text.append("microns_per_pixel_X = 1")
        settings_text.append("get_coordinates = []")
        settings_text.append("save_intermediates = []")
        settings_text.append("intensity_range_in = []")
        settings_text.append("intensity_range_out = []")
        settings_text.append("gamma = []")
        settings_text.append("threshold_adjustment = []")
        settings_text.append("smoothing_sigma = []")
        settings_text.append("noise_limit = []")
        settings_text.append("write_csv = []")
        settings_text.append("downsample = []")
        settings_text.append("num_points = []")
        settings_text.append("draw_ar = []")
        # print settings_text

        f = open(sample_out_directory+os.sep+'2dmorph_settings.txt', 'w')

        for setting in settings_text:
            f.write(setting+'\n')

        f.close()
    else:
        print "no focused_unlabeled directory: "+directory

# Write directory list
f = open('dirs_'+twodmorph_run_name+'.txt', 'w')

for directory in out_dir_list:
    f.write(directory+'\n')

f.close()
