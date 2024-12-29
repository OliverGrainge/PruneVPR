import pytest
from PlaceRec.Datasets.spedtest import SpedTest

# Create a fixture to reuse the dataset instance
@pytest.fixture(scope="module")
def spedtest_dataset():
    return SpedTest()

def test_pitts30k():
    assert True

def test_spedtest_instance(spedtest_dataset):
    assert isinstance(spedtest_dataset, SpedTest)

def test_spedtest_paths(spedtest_dataset):
    assert len(spedtest_dataset.map_paths) > 100
    assert len(spedtest_dataset.query_paths) > 100
    assert len(spedtest_dataset.gt) > 100

def test_spedtest_paths_lengths(spedtest_dataset):
    assert len(spedtest_dataset.query_paths) == len(spedtest_dataset.gt)






