import sys
sys.path.append(".")

import argparse
from problem.load_data import load_data_bis
from problem.train_MINST import train_model
from logger import custom_logger
import argparse


def run(**kwargs):
    data = load_data_bis()
    _, acc = train_model(data, **kwargs)


if __name__ == "__main__":
    # create logger
    logger = custom_logger("problem.train_MINST", "hyperOpal/log/runnee.log")

    # gets arguments
    parser = argparse.ArgumentParser(description="Runs MNIST")
    parser.add_argument("--n_epoch", help="Number of epochs")
    parser.add_argument("--batch_size", help="Batch size")
    parser.add_argument("--noeuds", help="Nombre de noeuds", nargs="*")
    parser.add_argument("--activation", help="Activation: relu, sigmoid, tanh")
    parser.add_argument("--learning_rate", help="Learning rate")
    parser.add_argument("--reg_l1", help="L1 regularization coefficient")
    parser.add_argument("--reg_l2", help="L2 regularization coefficient")
    parser.add_argument("--moment", help="Momentum for the gradient descent")
    parser.add_argument("--decay", help="Decay for the learning_rate")
    parser.add_argument("--nesterov", help="Using nesterov for the momentum")

    args = vars(parser.parse_args())
    params = {}
    for key in args:
        val = args[key]
        if val is not None:
            if key in ["n_epoch", "batch_size"]:
                params[key] = int(val)
            if key in ["learning_rate", "reg_l1", "reg_l2", "moment", "decay"]:
                params[key] = float(val)
            if key in ["nesterov"]:
                params[key] = bool(val)
            if key in ["activation"]:
                params[key] = val
            if key == "noeuds":
                neurons = map(lambda x: int(x), val)
                neurons = filter(lambda x: x > 0, neurons)
                params[key] = neurons
                params["n_couches"] = len(neurons)

    run(**params)
