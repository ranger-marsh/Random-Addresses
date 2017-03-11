from pathlib import Path
import os
import random_addresses as RA


def setup_module(module):
    pass


def teardown_module(module):
    os.remove('test_write.txt')


def test_file_open():
    # Open file read to list.
    address_list = RA.open_file('testing_data/test_data.txt')
    # Does the file open
    assert address_list is not None
    # Is the file a list
    assert type(address_list) is list
    # Are the list items striped
    assert address_list[1] == '1001 N Summer LN UNIT E'
    # list length is expected after empty lines are removed
    assert len(address_list) == 24


def test_write_file():
    test_list = ['red', 'blue', 'green']
    RA.write_file(test_list, 'test_write.txt')
    my_file = Path('test_write.txt')
    assert my_file.is_file() is True


def test_determine_sample_size():
    # Open file read to list.
    address_list = RA.open_file('testing_data/test_data.txt')
    # sample half the list test_data is length 24.
    sample_rate = '0.5'
    results = RA.determine_sample_size(address_list, sample_rate)
    # half the list is 12
    assert results == 12


def test_remove_used():
    orginal_list = ['zero', 'one', 'two', 'three', 'four', 'five']
    used_list = ['zero', 'two',  'five']
    expected = ['one', 'three', 'four']
    RA.remove_used(orginal_list, used_list)
    assert RA.remove_used(orginal_list, used_list) == expected


def test_random_sample():
    # Open file read to list.
    address_list = RA.open_file('testing_data/test_data.txt')
    # create random list
    random_addresses = RA.random_sample(address_list, sample_size=12)
    # make sure list length is as expected.
    assert len(random_addresses) == 12


def test_sort_addresses():
    unsorted = ['515 Movie RD UNIT 204',
                '2517 Blue LN',
                '512 Movie RD UNIT 102',
                '2506 Blue LN',
                '507 Movie RD UNIT 204',
                '1003 N Summer LN UNIT E',
                '2702 Silver GATE WAY',
                '1003 N Summer LN UNIT H',
                '2610 Silver GATE WAY',
                '1003 N Summer LN UNIT A']

    expected = ['2506 Blue LN',
                '2517 Blue LN',
                '507 Movie RD UNIT 204',
                '512 Movie RD UNIT 102',
                '515 Movie RD UNIT 204',
                '1003 N Summer LN UNIT A',
                '1003 N Summer LN UNIT E',
                '1003 N Summer LN UNIT H',
                '2610 Silver GATE WAY',
                '2702 Silver GATE WAY']

    custom_sorted = RA.sort_addresses(unsorted)
    assert custom_sorted == expected
