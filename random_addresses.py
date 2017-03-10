import random


def open_file(path):
    with open(path, 'r') as file:
        addresses = file.read().splitlines()
        addresses = map(str.strip, addresses)  # Remove white space
        addresses = list(filter(None, addresses))  # Remove empty lines
    return addresses


def write_file(random_list, path):
    with open(path, 'w') as file:
        for address in random_list:
            file.write('{}\n'.format(address))  # write list line by line


def determine_sample_size(address_list, sample_rate):
    sample_size = int(len(address_list) * sample_rate)
    return sample_size


def random_sample(address_list, sample_size):
    random_list = random.sample(address_list, sample_size)
    return random_list


def sort_key(list_item):
    # Sort key specific to my data.
    parts = list_item.split()
    if len(parts) > 3:
        return parts[1], int(parts[0]), parts[-1]
    return parts[1], int(parts[0])


def sort_addresses(address_list):
    # Sort the data after randomization.
    address_list.sort(key=sort_key)
    return address_list


def main():
   pass

if __name__ == '__main__':
    main()
