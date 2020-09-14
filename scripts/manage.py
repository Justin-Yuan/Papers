import os 
import sys 
import argparse 

#####################################################################################
### arguments 
#####################################################################################

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp", type=str, default="maddpg_eval",
                        help="name of the experiment")
    # parser.add_argument("--save_dir", type=str, default="./results",
    #                     help="top level path to save experiment/training results")
    # parser.add_argument("--sub_dir", type=str, nargs='+',
    #                     help="sub folders for experiment (hierarchical), e.g. sub=a b c --> local-dir/a/b/c")
    # parser.add_argument("--tag", type=str, nargs='+',
    #                     help="additional info for experiment, i.e. hyperparameters")
    # parser.add_argument("--seed", default=0, type=int,
    #                     help="Random seed, if negative do not set seed")
    # parser.add_argument("--cuda", default=False, action='store_true')
    return parser.parse_args()

#####################################################################################
### funcs 
#####################################################################################

def compile_index(args):
    pass 


def main(args):
    pass


#####################################################################################
### maain  
#####################################################################################

if __name__ == "__main__":
    args = parse_args()
    main(args)

