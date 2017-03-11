import random
import sys

# Terminal text colors.
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


def usage():
    print('''
             This script takes in a text file of addresses and writes a text
             file containing a random sample of the in-file. sample-rate is
             inputed as a floating point number. (e.g. 0.5 == %50) The rate
             should be less than 1.0.

             Basic usage:
             script.py <in-file> <out-file> <sample-rate>

             On a second or subsequent runs a text file containing used
             addresses. These addresses will not be sampled.

             Subsequent usage:
             script.py <in-file> <out-file> <sample-rate> <used-file>
             ''')


def validate_args():
    if len(sys.argv) != 4 and len(sys.argv) != 5:
        usage()
        sys.exit(FAIL + 'Incorrect number of arguments passed.\n')

    try:
        if not float(sys.argv[3]) < 1:
            usage()
            sys.exit(
                FAIL + 'sample-rate should be a floating point number less than 1.0.\n')

    except ValueError:
        usage()
        sys.exit(
            FAIL + 'sample-rate should be a floating point number less than 1.0.\n')


def open_file(path):
    with open(path, 'r') as file:
        addresses = file.read().splitlines()
        addresses = [address.strip() for address in addresses]
        addresses = list(filter(None, addresses))  # Remove empty lines
    return addresses


def write_file(random_list, path):
    with open(path, 'w') as file:
        for address in random_list:
            file.write('{}\n'.format(address))  # write list line by line


def determine_sample_size(address_list, sample_rate):
    sample_size = int(len(address_list) * sample_rate)
    return sample_size


def remove_used(orginal_list, used_list):
    # Remove used lines if a second sample is needed.
    used = set(used_list)  # set saves time  when checking checking membership
    unused_list = [address for address in orginal_list if address not in used]
    return unused_list


def random_sample(address_list, sample_size):
    random_list = random.sample(address_list, sample_size)
    return random_list


def sort_key(list_item):
    # Sort key specific to my data.
    parts = list_item.split()
    if len(parts) > 3:
        return parts[1], int(parts[0]), parts[-1]
    return parts[1], int(parts[0])


def sort_addresses(random_list):
    # Sort the data after randomization.
    random_list.sort(key=sort_key)
    return random_list


def main():
    pass

if __name__ == '__main__':
    main()
