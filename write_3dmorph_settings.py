import os

output_directory = ''
threemorph_run_name = ''

output_directory += os.sep+threedmorph_run_name

install_dir = '/home/geo/hull/ph269/software/AutoMorph'

l = open('dirs_focused.txt','r')

out_dir_list = []

for line in l:

    directory = line.strip()
    sampleID = os.path.basename(directory)

    sample_out_directory = output_directory+os.sep+sampleID
    segmented_directory = directory
    focused_directory = directory+'/final/focused_unlabeled'

    print "in: "+segmented_directory
    print "out: "+sample_out_directory

    if os.path.exists(focused_directory):

        out_dir_list.append(sample_out_directory)

        if not os.path.exists(sample_out_directory):
                os.makedirs(sample_out_directory)

        settings_text = []
        settings_text.append("directory = "+segmented_directory)

        settings_text.append("path_run3dmorph = /home/geo/hull/ph269/software/AutoMorph/run3dmorph")
        settings_text.append("path_run2dmorph = /home/geo/hull/ph269/software/AutoMorph/run2dmorph")
        settings_text.append("output_dir = " + sample_out_directory)
        settings_text.append("sampleID = " +sampleID)

        settings_text.append("macro_mode = False")
        settings_text.append("kernel_size_SF = []")
        settings_text.append("fiji_architecture = 64")
        settings_text.append("unit = micron")
        settings_text.append("calibration = 0.975")
        settings_text.append("num_slices = 25")
        settings_text.append("zstep = 31.1")
        settings_text.append("kernel_size_OF = 105")
        settings_text.append("downsample_grid_size  = 1")
        settings_text.append("savePDF = []")

        settings_text.append("intensity_range_in = []")
        settings_text.append("intensity_range_out = []")
        settings_text.append("gamma = []")
        settings_text.append("threshold_adjustment = []")
        settings_text.append("noise_limit = []")
        settings_text.append("geom3d_path = /home/geo/hull/ph269/software/AutoMorph/run3dmorph/src/geom3d-2014.10.13/geom3d/meshes3d")
        settings_text.append("mbb_path =  /home/geo/hull/ph269/software/AutoMorph/run3dmorph/src")
        settings_text.append("mesh2pdf_path = /home/geo/hull/ph269/software/AutoMorph/run3dmorph/src/mesh2pdf")
        settings_text.append("media9_path = /home/geo/hull/ph269/software/AutoMorph/run3dmorph/src")
        settings_text.append("run_latex = true")
        # print settings_text

        f = open(sample_out_directory+os.sep+'3dmorph_settings.txt', 'w')

        for setting in settings_text:
            f.write(setting+'\n')

        f.close()
    else:
        print "no focused_unlabeled directory: "+directory

# Write directory list
f = open('dirs_'+threedmorph_run_name+'.txt', 'w')

for directory in out_dir_list:
    f.write(directory+'\n')

f.close()
