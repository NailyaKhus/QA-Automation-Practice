from utils import read_from_file

TEST_FILE = 'testfile.txt'

def creat_test_data(test_data):
    with open(TEST_FILE, "a") as f_o:
        f_o.writelines(test_data)

def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three\n']
    creat_test_data(test_data)
    assert test_data == read_from_file(TEST_FILE)

def test_read_from_file2():
    test_data = ['one\n', 'two\n', 'three\n', 'four\n']
    creat_test_data(test_data)
    assert test_data == read_from_file(TEST_FILE)