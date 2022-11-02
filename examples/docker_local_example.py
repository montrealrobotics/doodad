"""
Example script for using newton machines via docker + rllab
"""

def my_func(doodad_config, variant):
    ### Import everything here. Not on the top level.
    print (variant)
    print (doodad_config)
    
    return variant["data"] + 4
    
    


if __name__ == "__main__":
    from doodad.easy_launch.python_function import run_experiment
#     from launchers.config import *
    ### You need to import your own config file to speicify the environment settings you want to use.
    ### Usually make a folder in your project called launchers/config_private.py
    ### doodad is designed to check for a launchers folder. Here we explicitly import the config file.
    from examples.config_private_example import *


    ### Consider using some method to construct your variant from a condif file.
    variant = { "exp_name": "test",
           "doodad_run_mode": "local_docker",
           "ssh_host": "defualt",
           "training_processor_type": "cpu",
           "data": 45}

    print ("variant: ", variant)
    out = run_experiment(
        my_func,
        exp_name=variant["exp_name"],
        mode=variant["doodad_run_mode"],
        ssh_host=variant["ssh_host"],
        use_gpu=variant["training_processor_type"] == "gpu",
        variant=variant,
    )
    
    print ("Out: " + str(out))
