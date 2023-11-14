CODE_DIRS_TO_MOUNT = [
    ## location of SMiRL code
]
NON_CODE_DIRS_TO_MOUNT = [
    ## Maybe some simulation you are importing to run.
]
LOCAL_LOG_DIR = '/tmp/doodad-output/'
OUTPUT_DIR_FOR_DOODAD_TARGET = '/tmp/doodad-output/'
DIR_AND_MOUNT_POINT_MAPPINGS = [
#     dict(
#         local_dir='/home/gberseth/.mujoco/',
#         mount_point='/root/.mujoco',
#     ),
#     dict(
#         local_dir='/home/gberseth/playground/CoMPS',
#         mount_point='/root/playground/CoMPS',
#     ),
#     dict(
#         local_dir='/home/gberseth/playground/doodad_vitchry',
#         mount_point='/root/playground/doodad',
#     ),
]


"""
AWS Settings
"""
AWS_S3_PATH = 'TODO'

# The docker image is looked up on dockerhub.com.
DOODAD_DOCKER_IMAGE = 'gberseth/doodad-test:latest'
INSTANCE_TYPE = 'c4.2xlarge'
SPOT_PRICE = 0.3

GPU_DOODAD_DOCKER_IMAGE = 'gberseth/doodad-test:latest'
GPU_INSTANCE_TYPE = 'g3.4xlarge'
GPU_SPOT_PRICE = 0.5
REGION_TO_GPU_AWS_IMAGE_ID = {
    'us-west-1': "ami-874378e7",
    'us-east-1': "ami-ce73adb1",
}
AWS_FILE_TYPES_TO_SAVE = (
    '*.txt', '*.csv', '*.json', '*.gz', '*.tar',
    '*.log', '*.pkl', '*.mp4', '*.png', '*.jpg',
    '*.jpeg', '*.patch', '*.html'
)

"""
SSH Settings
"""
SSH_HOSTS = dict(
    default=dict(
        username='TODO',
        hostname='TODO.domain.edu',
    ),
    beluga=dict(
        username='gberseth',
        hostname='beluga.computecanada.ca',
        use_singularity=True,
        use_slurm=True,
    ),
)
SSH_DEFAULT_HOST = 'user'
SSH_PRIVATE_KEY = '~/.ssh/id_rsa'
SSH_LOG_DIR = '~/shared/res'
SSH_TMP_DIR = '~/shared/tmp'

"""
Local Singularity Settings
"""
SINGULARITY_IMAGE = 'TODO'
SINGULARITY_PRE_CMDS = [
]


"""
Slurm Script Settings (or HTP).

The comments assume you're running on BRC.
"""
SLURM_CONFIGS = dict(
    cpu=dict(
        account_name='rrg-gberseth',
        partition='',
        n_gpus=0,
        max_num_cores_per_node=4,
        time_in_mins="1:00:00", ### 1 hour(s)
        mem="8Gb",
    ),
    gpu=dict(
        account_name='rrg-gberseth',
        partition='',
        n_gpus=1,
        max_num_cores_per_node=4,
        n_cpus_per_task=2,
        time_in_mins="1:00:00", ### 1 hour(s)
        mem="8Gb",
    ),
)
# This is necessary for the GPU machines on BRC.
BRC_EXTRA_SINGULARITY_ARGS = '--writable-tmpfs '
# Point to some directory on slurm where tasks will be copied to
TASKFILE_DIR_ON_BRC = 'TODO'


# This is the same as `CODE_DIRS_TO_MOUNT` but the paths should be relative to
# wherever you're running the slurm jobs (e.g. on BRC).
SSS_CODE_DIRS_TO_MOUNT = [
]
SSS_NON_CODE_DIRS_TO_MOUNT = [
]
# where do you want doodad to output to when using SSS (or HTP) mode?
SSS_LOG_DIR = '/global/scratch/user/doodad-log'


# point to your singularity image with an absolute path on BRC.
SSS_GPU_IMAGE = 'TODO'
SSS_CPU_IMAGE = 'TODO'
# point to `doodad/easy_launch/run_experimenty.py`
SSS_RUN_DOODAD_EXPERIMENT_SCRIPT_PATH = 'TODO'
# add any extra pre-commands to your script
SSS_PRE_CMDS = [
    'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH'
]


"""
GCP Settings

To see what zones support GPU, go to https://cloud.google.com/compute/docs/gpus/
"""
GCP_IMAGE_NAME = 'TODO'
GCP_GPU_IMAGE_NAME = 'TODO'
GCP_BUCKET_NAME = 'TODO'

GCP_DEFAULT_KWARGS = dict(
    zone='us-west1-a',
    instance_type='n1-standard-4',
    image_project='TODO',
    terminate=True,
    preemptible=False,  # is much more expensive!
    gpu_kwargs=dict(
        gpu_model='nvidia-tesla-k80',
        num_gpu=1,
    )
)
GCP_FILE_TYPES_TO_SAVE = (
    '*.txt', '*.csv', '*.json', '*.gz', '*.tar',
    '*.log', '*.pkl', '*.mp4', '*.png', '*.jpg',
    '*.jpeg', '*.patch', '*.html'
)

# Overwrite with private configurations

try:
    from launchers.config_private import *
except ImportError as e:
    from doodad.utils import REPO_DIR
    import os.path as osp
    command_to_run = "cp {} {}".format(
        __file__,
        __file__[:-3] + '_private.py',
        )
    print("You should set up the private config files. Run:\n\n  {}\n".format(
        command_to_run
    ))
