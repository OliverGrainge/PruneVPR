import pytest
from PlaceRec.Datasets.pitts30k import Pitts30k_Val, Pitts30k_Test

# Create a fixture to reuse the dataset instance
@pytest.fixture(scope="module")
def pitts_dataset_val():
    return Pitts30k_Val()


@pytest.fixture(scope="module")
def pitts_dataset_test():
    return Pitts30k_Test()


def test_pitts30k():
    assert True


def test_pitts30k_val_instance(pitts_dataset_val):
    assert isinstance(pitts_dataset_val, Pitts30k_Val)

def test_pitts30k_val_paths(pitts_dataset_val):
    assert len(pitts_dataset_val.map_paths) > 100
    assert len(pitts_dataset_val.query_paths) > 100
    assert len(pitts_dataset_val.gt) > 100

def test_pitts30k_val_paths_lengths(pitts_dataset_val):
    assert len(pitts_dataset_val.query_paths) == len(pitts_dataset_val.gt)

def test_pitts30k_val_query_loader(pitts_dataset_val):
    dataloader = pitts_dataset_val.query_images_loader(batch_size=3, shuffle=False, pin_memory=False, num_workers=0)
    for batch in dataloader:
        break 
    assert len(batch[0]) == 3

def test_pitts30k_val_map_loader(pitts_dataset_val):
    dataloader = pitts_dataset_val.map_images_loader(batch_size=3, shuffle=False, pin_memory=False, num_workers=0)
    for batch in dataloader:
        break 
    assert len(batch[0]) == 3



def test_pitts30k_test_instance(pitts_dataset_test):
    assert isinstance(pitts_dataset_test, Pitts30k_Test)

def test_pitts30k_test_paths(pitts_dataset_test):
    assert len(pitts_dataset_test.map_paths) > 100
    assert len(pitts_dataset_test.query_paths) > 100
    assert len(pitts_dataset_test.gt) > 100

def test_pitts30k_test_paths_lengths(pitts_dataset_test):
    assert len(pitts_dataset_test.query_paths) == len(pitts_dataset_test.gt)


def test_pitts30k_test_query_loader(pitts_dataset_test):
    dataloader = pitts_dataset_test.query_images_loader(batch_size=3, shuffle=False, pin_memory=False, num_workers=0)
    for batch in dataloader:
        break 
    assert len(batch[0]) == 3

def test_pitts30k_test_map_loader(pitts_dataset_test):
    dataloader = pitts_dataset_test.map_images_loader(batch_size=3, shuffle=False, pin_memory=False, num_workers=0)
    for batch in dataloader:
        break 
    assert len(batch[0]) == 3
