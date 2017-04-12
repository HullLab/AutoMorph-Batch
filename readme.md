# AutoMorph Batch Workflow at Yale

We run the AutoMorph batch workflow on Yale's grace-next cluster, using the Slurm scheduler and a batching utility called Dead Simple Queue (dSQ).

```bash
ssh -Y <netid>@grace-next.hpc.yale.edu
```

- [Slurm Documentation](http://research.computing.yale.edu/support/hpc/user-guide/slurm)
- [dSQ Documentation](http://research.computing.yale.edu/support/hpc/user-guide/dead-simple-queue) (including tips on how to monitor your tasks and identifying failed tasks)

## One Time Setup

- Add the following to your `.bashrc` file on Grace

```bash
. /home/geo/hull/ph269/software/etc/hull_bashrc
module load Tools/dSQ
```
- Copy the ZereneStacker license, etc into your home directory

```bash
cp -r /home/geo/hull/ph269/.ZereneStacker ~/
```

## New Project Setup

- Create a directory in Grace's scratch60. This will be `raw_images_root` below.

```bash
mkdir /gpfs/scratch60/geo/hull/data/<your_project>
```

- Copy your stacks to your directory, either with Globus or rsync on Omega's data transfer node (email Kaylea if you have questions about this step).

- Create directory in your project space for the segmented output files. This will be `output_root` below.

```bash
mkdir $HOME/project/<your_project>
```

- Clone this repository into a new directory in your home directory on Grace.

- Edit and run `list_dirs.py`
    - specify `raw_images_root`
    - specify `output_root`

## Segment (sample)

- Edit and run `write_segment_settings.py`
    - specify `output_root` (see above)
    - set `mode = 'sample'`
    - set `threshold_range` to the sample threshold range
    - run `write_segment_settings.py`

- Run `list_dirs.py`. This will create three directories:
    - `dirs_stacks.txt`: file listing all the input directories
    - `dirs_stacks.csv`: same contents as `dirs_stacks.txt`, but fields should be added for when segment is run in `final` mode.
    - `dirs_segmented.txt`: file listing the output directories that will contain the settings file and output images from segment.

```
python list_dirs.py presegment    
```

- Create taskfile for dSQ

```bash
python build_taskfile.py segment
```

- Run dSQ to create submission script

```bash
dSQ --taskfile taskfile_segment.txt > submit_segment.sh
```

- Optional: It may be necessary to increase the memory that the submission script requests per task since Segment can be very memory hungry with bigtiff files. If so, edit `submit_segment.sh` and increase `--mem-per-cpu`. For example:

```
#SBATCH --mem-per-cpu=40G
```

- Submit the submission script to Slurm

```
sbatch submit_segment.sh
```

- See [dSQ Documentation](http://research.computing.yale.edu/support/hpc/user-guide/dead-simple-queue) for instructions on checking task status.

## Segment (final)

- Edit `dirs_stacks.csv` to add final threshold values. For example:

```
/gpfs/scratch60/geo/hull/data/porosity/CH82_150-250um_1-102_sp,0.1
```

- Edit and run `write_segment_settings.py`
    - specify `output_root` (if not already set, see above)
    - set `mode = 'final'`
    - run `write_segment_settings.py`

- Create taskfile for dSQ

```bash
python build_taskfile.py segment
```

- Run dSQ to create submission script

```bash
dSQ --taskfile taskfile_segment.txt > submit_segment.sh
```

- Optional: It may be necessary to increase the memory that the submission script requests per task since Segment can be very memory hungry with bigtiff files. If so, edit `submit_segment.sh` and increase `--mem-per-cpu`. For example:

```
#SBATCH --mem-per-cpu=40G
```

- Submit the submission script to Slurm

```
sbatch submit_segment.sh
```

- See [dSQ Documentation](http://research.computing.yale.edu/support/hpc/user-guide/dead-simple-queue) for instructions on checking task status.

## Focus

- If this is your first step with the dataset. Run `list_dirs.py`. 
    - `dirs_segmented.txt`: file listing the output directories that contain the output images from segment.

```
python list_dirs.py segmented    
```

- Create taskfile for SimpleQueue.

```bash
python build_taskfile.py focus
```

- Run dSQ to create submission script

```bash
dSQ --taskfile taskfile_focus.txt > submit_focus.sh
```

- Edit `submit_focus.sh`. Add the additional directive to ensure one task per node. Put it with the similar looking lines, otherwise order doesn't matter.

```

```

- Submit the submission script to Slurm

```
sbatch submit_focus.sh
```

## 2dmorph

- Create list of successfully focused directories (this will create `dirs_focused.txt`)

```
python list_dirs.py focused
```



### If Running with Global Settings

- Open `write_2dmorph_settings.py` and configure the settings. There is also a variable at the top named `twodmorph_run_name`. You can change this variable for different 2dmorph settings. It will then create a directory list called `dirs_<twodmorph_run_name>.txt` and set the output to a directory with that name in `output_root` as configured above. 

- Run `write_2dmorph_settings.py`

```
python write_2dmorph_settings.py
```

- Create a task list for 2dmorph.

```
python build_taskfile.py 2dmorph -d dirs_<twodmorph_run_name>.txt
```

### If Running with a CSV of Settings

- Open `write_2dmorph_settings.py` and configure the  variable at the top named `twodmorph_run_name`.  You can change this variable for different 2dmorph settings so they output in unique locations. It will also create a directory list called `dirs_<twodmorph_run_name>.txt` and create output directories with that name in `output_root` as configured above. 

- Run `write_2dmorph_settings.py`

```
python write_2dmorph_settings.py
```

- copy or move `dirs_<twodmorph_run_name>.txt` to `dirs_<twodmorph_run_name>.csv` and add fields for the settings you need to edit.

- Open `write_2dmorph_settings.py` and configure the settings. Make sure to modify `write_2dmorph_settings.py` to read in these settings. It will create another directory list called `dirs_<twodmorph_run_name>.txt` but you can ignore this file.

- Run `write_2dmorph_settings.py`

```
python write_2dmorph_settings.py
```

- Create a task list for 2dmorph 

```
python build_taskfile.py 2dmorph -d dirs_<twodmorph_run_name>.csv
```

- Use dead simple queue to create submission script and submit.

```
dSQ --taskfile taskfile_2dmorph.txt > submit_2dmorph.sh
sbatch submit_2dmorph.sh
```

