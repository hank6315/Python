import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Please specify either single IP or list from csv'
    )
    parser.add_argument("-s", metavar='192.168.0.1', dest='host' , help="IP Address" ,type=str)
    parser.add_argument("-u", metavar='user', dest='username', help="Username", type=str)
    parser.add_argument("-p", metavar='password', dest='password', help="assword", type=str)
    parser.add_argument("-f", metavar='template.csv',dest='csvfile', help="CSV format file to defined template information",  type=str)
    
    args = parser.parse_args()

    if (args.host is None) and (args.csvfile is None):
        parser.print_help()
        sys.exit(1)