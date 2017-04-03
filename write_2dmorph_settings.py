import os

output_directory = ''
twodmorph_run_name = ''

output_directory += os.sep+twodmorph_run_name

install_dir = '/home/geo/hull/ph269/software/AutoMorph'

l = open('dirs_focused.txt','r')

out_dir_list = []

for line in l:

    directory = line.strip()
    sampleID = os.path.basename(directory)

    sample_out_directory = output_directory+os.sep+sampleID
    focused_directory = directory+'/final/focused_unlabeled'

    print "in: "+focused_directory
    print "out: "+sample_out_directory

    if os.path.exists(focused_directory):

        out_dir_list.append(sample_out_directory)

        if not os.path.exists(sample_out_directory):
                os.makedirs(sample_out_directory)

        settings_text = []
        settings_text.append("directory = "+focused_directory)
        settings_text.append("output_dir = "+sample_out_directory)
        settings_text.append("install_dir = "+install_dir)
        settings_text.append("image_extension = .tif")

        settings_text.append("sampleID = "+sampleID)

        settings_text.append("microns_per_pixel_Y = 0.485")
        settings_text.append("microns_per_pixel_X = 0.485")
        settings_text.append("get_coordinates = []")
        settings_text.append("save_intermediates = []")
        settings_text.append("intensity_range_in = [0 0.8]")
        settings_text.append("intensity_range_out = []")
        settings_text.append("gamma = []")
        settings_text.append("threshold_adjustment = []")
        settings_text.append("smoothing_sigma = []")
        settings_text.append("noise_limit = []")
        settings_text.append("downsample = []")
        settings_text.append("num_points = []")
        settings_text.append("draw_ar = []")
        #print settings_text

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
