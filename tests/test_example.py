from hexlet_pytest.example import reverse
from pathlib import Path


def test_reverse():
    assert reverse('12345') == '54321'


def test_reverse_for_empty_string():
    assert reverse('') == ''


def get_test_data_path(filename):
    return Path(__file__).parent /'test_data'/filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverse_long():
    text = read_file('data_1.txt')
    print(text)
    result = reverse(text)
    print(result)
    correct_result = read_file('result_1.txt')
    assert result == correct_result
