import os
import sys
import yaml

from handyrl.train import train_main
from handyrl.train import train_server_main
from handyrl.worker import worker_main
from handyrl.evaluation import eval_main
from handyrl.evaluation import eval_server_main
from handyrl.evaluation import eval_client_main

def main():
    with open('config.yaml') as f:
        args = yaml.safe_load(f)
    print(args)

    train_main(args)

if __name__ == '__main__':
    main()