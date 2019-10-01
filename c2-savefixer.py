from lzstring import LZString
import json
import argparse
import sys

parser = argparse.ArgumentParser(description='Fix a Clickpocalypse 2 save if you get stuck off the side of the map.')
input_group = parser.add_mutually_exclusive_group(required=True)
input_group.add_argument('-f', '--file', type=str, help='Input file')
input_group.add_argument('-i', '--input', type=str, help='Input text')

move_group = parser.add_mutually_exclusive_group(required=True)
move_group.add_argument('-l', '--left', action='store_true', help='Move party to the left')
move_group.add_argument('-r', '--right', action='store_true', help='Move party to the right')

args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

if args.file:
	try:
		save = open(args.file).read().strip()
	except FileNotFoundError:
		print("No such file")
elif args.input:
	save = args.input


data = json.loads(LZString().decompresFromBase64(save))

# +worldX moves to the right
# -worldX moves to the left

if args.left:
	move_amount = -5000
elif args.right:
	move_amount = 5000

for adventurer in data['adventurers']:
	adventurer['positionComponent']['worldX'] += move_amount


print(LZString().compressToBase64(json.dumps(data)))

