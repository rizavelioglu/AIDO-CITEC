import argparse


def get_ddpg_args_train():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", default=123, type=int)  # Sets Gym, PyTorch and Numpy seeds
    parser.add_argument("--start_timesteps", default=1e4, type=int)  # How many time steps purely random policy is run for
    parser.add_argument("--eval_freq", default=5e3, type=float)  # How often (time steps) we evaluate
    parser.add_argument("--max_timesteps", default=2e5, type=float)  # Max time steps to run environment for
    parser.add_argument("--save_models", action="store_true", default=True)  # Whether or not models are saved
    parser.add_argument("--batch_size", default=32, type=int)  # Batch size for both actor and critic
    parser.add_argument("--discount", default=0.99, type=float)  # Discount factor
    parser.add_argument("--tau", default=0.005, type=float)  # Target network update rate
    parser.add_argument("--env_timesteps", default=50, type=int)  # How many timesteps each episode should run for
    parser.add_argument("--replay_buffer_max_size", default=10000, type=int)  # Maximum number of steps to keep in the replay buffer
    parser.add_argument("--train_on_colab", default=0, type=int)  # Flag whether training is on Colab

    return parser.parse_args()


def get_ddpg_args_test():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", default=123, type=int)  # Inform the test what seed was used in training
    parser.add_argument("--experiment", default=2, type=int)

    return parser.parse_args()
