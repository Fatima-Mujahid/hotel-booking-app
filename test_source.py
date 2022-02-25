import pytest
import mock
import source
from datetime import datetime


# Fixtures

@pytest.fixture
def hotel():
    return source.HotelBookingApp()



# Valid answers are parametrized
@pytest.mark.parametrize('valid_day', [str(day) for day in range(1, 8)])
def test_get_num_of_days(hotel, valid_day):

    # Invalid inputs can be added here with valid input at the end
    days = ["9999", "0", "", " ", "-2015", "12.65", "-30", "Seven", str(10 ^ 1000), valid_day]

    # side_effect, when given an iterable, iterates through
    # each time the patched function is called (in this case input())
    with mock.patch('builtins.input', side_effect=days):
        assert source.HotelBookingApp.get_num_of_days(hotel) == int(valid_day)



def test_get_amount(hotel):

    studio_amount = ["25001", "49999", "", " ", "-2015", "12.65", "-30", "Seven", str(10 ^ 1000), 0, 9999]
    executive_amount = ["25001", "49999", "", " ", "-2015", "12.65", "-30", "Seven", 10000, 25000]
    cabana_amount = ["25001", "49999", "", " ", "-2015", "12.65", "-30", "Seven", 50000, 100000,
                     9999999]

    # side_effect, when given an iterable, iterates through
    # each time the patched function is called (in this case input())
    with mock.patch('builtins.input', side_effect=studio_amount):
        assert source.HotelBookingApp.get_amount(hotel) == "Studio"
    with mock.patch('builtins.input', side_effect=executive_amount):
        assert source.HotelBookingApp.get_amount(hotel) == "Executive Suite"
    with mock.patch('builtins.input', side_effect=cabana_amount):
        assert source.HotelBookingApp.get_amount(hotel) == "Cabana"



# Valid answers are parametrized
@pytest.mark.parametrize('valid_name', ['Fatima Tuz Zehra', 'Maaz', 'Fatima Mujahid', 'Aaa', "Zzz", 'A A', 'Z Z'])
def test_get_user_name(hotel, valid_name):

    # Invalid inputs can be added here with valid input at the end
    names = ["ali", "kamran", "", " ", "-2015", "-30", "fatima zehra", 'AAA', 'ZZZ', str(10 ^ 1000), valid_name]

    # side_effect, when given an iterable, iterates through
    # each time the patched function is called (in this case input())
    with mock.patch('builtins.input', side_effect=names):
        assert source.HotelBookingApp.get_user_name(hotel) == valid_name



# Valid answers are parametrized
@pytest.mark.parametrize('valid_date', ['01-01-0001', '31-01-9999', '29-02-9996', '31-12-9999'])
def test_get_user_birthday(hotel, valid_date):

    # Invalid inputs can be added here with valid input at the end
    dates = ["ali", "kamran", "", " ", '99-99-9999', '00-00-0000', '30-02-2001', '29-02-9999', "-2015", "-30",
             "fatima zehra", str(10 ^ 1000), valid_date]

    # side_effect, when given an iterable, iterates through
    # each time the patched function is called (in this case input())
    with mock.patch('builtins.input', side_effect=dates):
        assert source.HotelBookingApp.get_user_birthday(hotel) == valid_date



# Valid answers are parametrized
@pytest.mark.parametrize('valid_cnic',
                         ['1111111111111', '9999999999999', '1000000000001', '0000000000000', '1000000000000'])
def test_get_user_cnic(hotel, valid_cnic):

    # Invalid inputs can be added here with valid input at the end
    cnics = ["9000000000000000", "00000000", "", " ", '99-99-9999', "-2015", "-30",
             "fatima zehra", str(10 ^ 1000), valid_cnic]

    # side_effect, when given an iterable, iterates through
    # each time the patched function is called (in this case input())
    with mock.patch('builtins.input', side_effect=cnics):
        assert source.HotelBookingApp.get_user_cnic(hotel) == valid_cnic


# Valid answers are parametrized
@pytest.mark.parametrize('valid_cnic_copy',
                         ['here.jpg', 'here.png', '0.jpg', '999999.png', 'a123a.jpg'])
def test_get_cnic_photocopy(hotel, valid_cnic_copy):

    # Invalid inputs can be added here with valid input at the end
    cnic_copys = ["hello.gif", "123.pdf", "", " ", ".png", '99-99-9999', "-2015", "-30",
                  "fatima zehra", str(10 ^ 1000), valid_cnic_copy]

    # side_effect, when given an iterable, iterates through
    # each time the patched function is called (in this case input())
    with mock.patch('builtins.input', side_effect=cnic_copys):
        assert source.HotelBookingApp.get_cnic_photocopy(hotel) == valid_cnic_copy



# Valid answers are parametrized
@pytest.mark.parametrize('valid_rating', [int(rating) for rating in range(0, 6)])
def test_get_rating(hotel, valid_rating):

    # Invalid inputs can be added here with valid input at the end
    ratings = ["9999", "", " ", "-2015", "12.65", "-30", "Seven", "6", str(10 ^ 1000), valid_rating]

    # side_effect, when given an iterable, iterates through
    # each time the patched function is called (in this case input())
    with mock.patch('builtins.input', side_effect=ratings):
        assert source.HotelBookingApp.get_rating(hotel) == int(valid_rating)
