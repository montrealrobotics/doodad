from doodad.easy_launch.python_function import run_experiment


def example(doodad_config, variant):
    print(doodad_config)
    print(variant)


if __name__ == "__main__":
    for seed in range(20):
        variant = dict(
            seed=seed,
        )
        run_experiment(
            example,
            exp_name='test',
            mode='htp',
            variant=variant,
            use_gpu=False,
        )
