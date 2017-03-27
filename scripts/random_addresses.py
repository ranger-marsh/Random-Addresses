#!/usr/bin/env python3

"""
This script takes in a text file. The file has one address per line. The script
returns a text file that contains a random sampling of the original file. This
script is used to help administer surveys for a local police station. The
surveys are administered in specific neighborhoods concerning police relations.
"""
import random
import sys

# Terminal text colors.
OKBLUE = '\033[94m'
FAIL = '\033[91m'


def usage():
    print('''
             This script takes in a text file of addresses and writes a text
             file containing a random sample of the in-file. sample-rate is
             inputed as a floating point number. (e.g. 0.5 == %50) The rate
             should be less than 1.0.

             Basic usage:
             random_addresses.py <in-file> <out-file> <sample-rate>

             On a second or subsequent runs a text file containing used
             addresses can be passed. These addresses will not be sampled.

             Subsequent usage:
             random_addresses.py <in-file> <out-file> <sample-rate> <used-file>
             ''')


def validate_args():
    if len(sys.argv) != 4 and len(sys.argv) != 5:
        usage()
        sys.exit(f'{FAIL}Incorrect number of arguments passed.\n')

    try:
        if not float(sys.argv[3]) < 1:
            usage()
            sys.exit(
                'f{FAIL}sample-rate should be a floating point number less than 1.0.\n')
    except ValueError:
        usage()
        sys.exit(
            'f{FAIL}sample-rate should be a floating point number less than 1.0.\n')


def open_text_file(path):
    with open(path, 'r') as file:
        addresses = file.read().splitlines()
        # Remove leading/trailing white space and blank lines.
        addresses = [address.strip()
                     for address in addresses if address.strip() != '']
    return addresses


def write_text_file(random_list, path):
    with open(path, 'w') as file:
        for address in random_list:  # write out-file line by line from list
            file.write('{}\n'.format(address))


def determine_sample_size(address_list, sample_rate):
    # Returns an int because a fraction of an address is not very useful.
    sample_size = int(len(address_list) * float(sample_rate))
    return sample_size


def remove_used(address_list, used_list):
    # Remove used lines if a second sample is needed.
    used = set(used_list)  # set saves time  when checking membership
    unused_list = [address for address in address_list if address not in used]
    return unused_list


def random_sample(address_list, sample_size):
    # Return a list containing a random sample.
    random_list = random.sample(address_list, sample_size)
    return random_list


def sort_key(list_item):
    # Sort key specific to my data.
    try:
        parts = list_item.split()
        if len(parts) > 3:
            return parts[1], int(parts[0]), parts[-1]
        return parts[1], int(parts[0])
    except IndexError:
        sys.exit(f'{FAIL} "{list_item}" not sortable by sort_key() check format.\n')


def sort_addresses(random_list):
    # Sort the data after randomization.
    random_list.sort(key=sort_key)
    return random_list


def main():
    validate_args()

    address_list = open_text_file(sys.argv[1])
    out_path = sys.argv[2]
    sample_size = determine_sample_size(address_list, sys.argv[3])

    if len(sys.argv) == 5:
        used_list = open_text_file(sys.argv[4])
        address_list = remove_used(address_list, used_list)

    random_list = random_sample(address_list, sample_size)
    random_list = sort_addresses(random_list)

    write_text_file(random_list, out_path)
    sys.exit(f'{OKBLUE}Random address file created at {out_path}')

if __name__ == '__main__':
    main()
