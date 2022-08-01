"""
Example script for using newton machines via docker + rllab
"""

def my_func(doodad_config, variant):
    
    print (variant)
    print (doodad_config)
    
    return variant["data"] + 4
    
    


if __name__ == "__main__":
    from doodad.easy_launch.python_function import run_experiment
#     from launchers.config import *


    ### Consider using some method to construct your variant from a condif file.
    variant = { "exp_name": "test",
           "doodad_run_mode": "local",
           "ssh_host": "defualt",
           "training_processor_type": "cpu",
           "data": 45}

    print ("variant: ", variant)
    out = run_experiment(
        my_func,
        exp_name=variant["exp_name"],
#         mode='local_docker',
        mode=variant["doodad_run_mode"],
#         mode='local',
#         mode='ec2',
        ssh_host=variant["ssh_host"],
        use_gpu=variant["training_processor_type"] == "gpu",
        variant=variant,
    )
    
    print ("Out: " + str(out))
