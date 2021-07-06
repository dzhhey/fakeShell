import argparse
import sys

parser = argparse.ArgumentParser(description='命令行中传入一个数字')
parser.add_argument('integers', type=str, help='传入的数字')

try:
    args = parser.parse_args("")
    print(args)
except Exception:
    cmd_res = {'out': sys.stdout.readlines(), 'err': sys.stderr.readlines()}
    print(1)
    print(cmd_res)

