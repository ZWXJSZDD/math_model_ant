import argparse
from ACO import ACO
from utils import random_init,calculate_distance,load_example

def default_argument_parser():
    parser = argparse.ArgumentParser(description="Ant Colony Algorithm")
    parser.add_argument("--test",default=1,nargs="?")
    parser.add_argument('--ant', default=10,type=int)
    parser.add_argument('--points', default=200,type=int)
    parser.add_argument('--generation', default=100,type=int) #[]
    parser.add_argument('--alpha', default=2.0,type=float)     #[1,4]
    parser.add_argument('--beta', default=3.0,type=float)     #[0,5]
    parser.add_argument('--rho', default=0.5,type=float)       #[0.2,0.5]
    parser.add_argument('--q', default=100,type=float)
    parser.add_argument('--strategy', default=2,type=int) 
    parser.add_argument('--min_x', default=0,type=int) 
    parser.add_argument('--max_x', default=500,type=int) 
    parser.add_argument('--min_y', default=0,type=int) 
    parser.add_argument('--max_y', default=500,type=int)
    return parser

def main():
    args = default_argument_parser().parse_args()

    if args.test!=None:
        points,distance = load_example(args.test)

    else:
        points = random_init(args.points,args.min_x,args.max_x,args.min_y,args.max_y)
        distance = calculate_distance(points)
    aco = ACO(#args.ant,args.generation,args.alpha,args.beta,args.rho,args.q,args.strategy,points,distance,
        ant_count=args.ant,
        generations=args.generation,
        alpha=args.alpha,
        beta=args.beta,
        rho=args.rho,
        q=args.q,
        strategy=args.strategy,
        points=points,
        distance=distance,
    )
    aco.run()

if __name__ == '__main__':
    main()