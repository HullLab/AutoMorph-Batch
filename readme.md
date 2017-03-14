# AutoMorph Batch Workflow at Yale

## Segment (sample)


1. Set up and run `write_segment_settings.py`
    - specify segment output root directory
    - set mode to `sample`
    - set sample threshold range
    - run `write_segment_settings.py`
1. Run `build_sq.py segment`
1. Run dSQ to create taskfile: `dSQ --taskfile taskfile_segment.txt > submit_segment.sh`
1. Submit: `sbatch submit_segment.sh`

## Segment (final)

You can skip steps with `*` if you performed the steps above for Segment in sample mode.

1. *Set up and run `list_dirs.py`
    - *specify raw images root directory
    - *specify segment output root directory
1. Edit `dirs_stacks.csv` to add final threshold values
1. Edit and run `write_segment_settings.py`
    - *specify segment output root directory
    - set mode to `final`
    - run `write_segment_settings.py`
1. *Run `build_sq.py segment`
1. *Run dSQ to create taskfile: `dSQ --taskfile taskfile_segment.txt > submit_segment.sh`
1. Submit: `sbatch submit_segment.sh`


