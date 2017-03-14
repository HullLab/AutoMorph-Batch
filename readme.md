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
    - run `list_dirs.py`


## Segment (sample)

- Edit and run `write_segment_settings.py`
    - specify `output_root` (see above)
    - set `mode = 'sample'`
    - set `threshold_range` to the sample threshold range
    - run `write_segment_settings.py`

- Create taskfile for dSQ

```bash
build_sq.py segment
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
build_sq.py segment
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

Focus still requires the old SimpleQueue due to the restrictions on ZereneStacker.

- Create taskfile for SimpleQueue.

```bash
build_sq.py focus
```

- Run sqCreateScript to create submission script. Set `num_workers` equal to a whole number that is about 10-25% of the number of tasks in your taskfile.

```bash
sqCreateScript -n <num_workers> taskfile_focus.txt > submit_focus.sh
```

- Edit `submit_focus.sh`. Add the additional directive to ensure one task per node. Put it with the similar looking lines, otherwise order doesn't matter.

```bash
#SBATCH --ntasks-per-node=1
```


- Submit the submission script to Slurm

```
sbatch submit_focus.sh
```

