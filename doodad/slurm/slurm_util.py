import math


class SlurmConfig(object):
    """
    Wrap a command around a call to sbatch

    Usage:
    ```
    generator = SBatchGenerator()
    cmd = "echo 'Hello, world!'"
    sbatch_cmd = generator.wrap(cmd)
    """
    def __init__(
            self,
            account_name,
            partition,
            time_in_mins,
            max_num_cores_per_node,
            n_gpus=0,
            n_cpus_per_task=1,
            mem="8Gb",
            n_nodes=None,
            extra_flags="",
    ):
        if n_gpus > 0 and n_cpus_per_task < 2:
            raise ValueError("Must have at least 2 cpus per GPU task")
        self.account_name = account_name
        self.partition = partition
        self.time_in_mins = time_in_mins
        self.n_nodes = n_nodes
        self.n_gpus = n_gpus
        self.n_cpus_per_task = n_cpus_per_task
        self.max_num_cores_per_node = max_num_cores_per_node
        self.extra_flags = extra_flags
        self.mem = mem


def wrap_command_with_sbatch(
        cmd,
        config,
        n_tasks,
):
    """
    Wrap a command around a call to sbatch

    Usage:
    ```
    config = SlurmConfig()
    cmd = "echo 'Hello, world!'"
    sbatch_cmd = wrap_command_with_sbatch(cmd, config)
    """
    cmd = cmd.replace("'", "\\'")
    num_cpus = n_tasks * config.n_cpus_per_task
    n_nodes = config.n_nodes or math.ceil(
        num_cpus / config.max_num_cores_per_node)
    if config.n_gpus > 0:
        full_cmd = (
            "sbatch --account={account_name} --time={time}"
            " -N {nodes} --ntasks={n_tasks} --cpus-per-task={cpus_per_task} --mem={mem}"
            " --gpus-per-node={n_gpus} {extra_flags} --wrap=$'{cmd}'".format(
                account_name=config.account_name,
                partition=config.partition,
                time=config.time_in_mins,
                nodes=n_nodes,
                n_tasks=n_tasks,
                cpus_per_task=config.n_cpus_per_task,
                mem=config.mem,
                cmd=cmd,
                n_gpus=config.n_gpus,
                extra_flags=config.extra_flags,
            )
        )
    else:
        full_cmd = (
            "sbatch --account={account_name} --time={time}"
            " -N {nodes} --ntasks={n_tasks} --cpus-per-task={cpus_per_task} --mem={mem}"
            " {extra_flags} --wrap=$'{cmd}'".format(
                account_name=config.account_name,
                partition=config.partition,
                time=config.time_in_mins,
                nodes=n_nodes,
                n_tasks=n_tasks,
                cpus_per_task=config.n_cpus_per_task,
                mem=config.mem,
                cmd=cmd,
                extra_flags=config.extra_flags,
            )
        )
    return full_cmd
