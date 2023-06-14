import pytest
import time


def get_time():
    return time.time()


@pytest.fixture
def for_time():
    start_test_time = get_time()
    yield
    end_test_time = get_time()
    print(f'Время начало теста {start_test_time} \n Время окончания теста {end_test_time}')


@pytest.fixture
def for_time_run():
    start_test_time = get_time()
    yield
    get_test_time = get_time() - start_test_time
    print(f'Время выполнения теста {get_test_time}')
