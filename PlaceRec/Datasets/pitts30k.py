import os
import zipfile
from glob import glob
from os.path import join

import numpy as np
import torch
import torchvision
import yaml
from PIL import Image
from scipy.signal import convolve2d
from sklearn.neighbors import NearestNeighbors
from torch.utils.data import DataLoader, Dataset

from PlaceRec.Datasets.base_dataset import BaseDataset
from PlaceRec.utils import ImageIdxDataset, get_config

config = get_config()
package_directory = os.path.dirname(os.path.abspath(__file__))


class Pitts30k_Val(BaseDataset):
    def __init__(self):
        if not os.path.isdir(join(config["datasets_directory"], "Pittsburgh-Query")):
            raise Exception("Pitts30k Not Downloaded")

        self.root = join(config["datasets_directory"], "Pittsburgh-Query")
        self.map_paths = np.array(
            [
                join(self.root, pth)
                for pth in np.load(
                    "PlaceRec/Datasets/image_paths/pitts30k_val_dbImages.npy"
                )
            ]
        )
        self.query_paths = np.array(
            [
                join(self.root, pth)
                for pth in np.load(
                    "PlaceRec/Datasets/image_paths/pitts30k_val_qImages.npy"
                )
            ]
        )
        self.gt = np.load(
            "PlaceRec/Datasets/image_paths/pitts30k_val_gt.npy", allow_pickle=True
        )

        self.name = "pitts30k_val"

    def query_images_loader(
        self,
        batch_size: int = 16,
        shuffle: bool = False,
        preprocess: torchvision.transforms.transforms.Compose = None,
        pin_memory: bool = False,
        num_workers: int = 0,
    ) -> torch.utils.data.DataLoader:
        # build the dataloader
        dataset = ImageIdxDataset(self.query_paths, preprocess=preprocess)
        dataloader = DataLoader(
            dataset,
            shuffle=shuffle,
            batch_size=batch_size,
            pin_memory=pin_memory,
            num_workers=num_workers,
        )
        return dataloader

    def map_images_loader(
        self,
        batch_size: int = 16,
        shuffle: bool = False,
        preprocess: torchvision.transforms.transforms.Compose = None,
        pin_memory: bool = False,
        num_workers: int = 0,
    ) -> torch.utils.data.DataLoader:
        dataset = ImageIdxDataset(self.map_paths, preprocess=preprocess)

        dataloader = DataLoader(
            dataset,
            shuffle=shuffle,
            batch_size=batch_size,
            pin_memory=pin_memory,
            num_workers=num_workers,
        )
        return dataloader

    def ground_truth(self) -> np.ndarray:
        return self.gt


class Pitts30k_Test(BaseDataset):
    def __init__(self):
        if not os.path.isdir(join(config["datasets_directory"], "Pittsburgh-Query")):
            raise Exception("Pitts30k Not Downloaded")

        self.root = join(config["datasets_directory"], "Pittsburgh-Query")
        self.map_paths = np.array(
            [
                join(self.root, pth)
                for pth in np.load(
                    "PlaceRec/Datasets/image_paths/pitts30k_test_dbImages.npy"
                )
            ]
        )

        self.query_paths = np.array(
            [
                join(self.root, pth)
                for pth in np.load(
                    "PlaceRec/Datasets/image_paths/pitts30k_test_qImages.npy"
                )
            ]
        )
        self.gt = np.load(
            "PlaceRec/Datasets/image_paths/pitts30k_test_gt.npy", allow_pickle=True
        )

        self.name = "pitts30k_test"

    def query_images_loader(
        self,
        batch_size: int = 16,
        shuffle: bool = False,
        preprocess: torchvision.transforms.transforms.Compose = None,
        pin_memory: bool = False,
        num_workers: int = 0,
    ) -> torch.utils.data.DataLoader:
        # build the dataloader
        dataset = ImageIdxDataset(self.query_paths, preprocess=preprocess)
        dataloader = DataLoader(
            dataset,
            shuffle=shuffle,
            batch_size=batch_size,
            pin_memory=pin_memory,
            num_workers=num_workers,
        )
        return dataloader

    def map_images_loader(
        self,
        batch_size: int = 16,
        shuffle: bool = False,
        preprocess: torchvision.transforms.transforms.Compose = None,
        pin_memory: bool = False,
        num_workers: int = 0,
    ) -> torch.utils.data.DataLoader:
        dataset = ImageIdxDataset(self.map_paths, preprocess=preprocess)

        dataloader = DataLoader(
            dataset,
            shuffle=shuffle,
            batch_size=batch_size,
            pin_memory=pin_memory,
            num_workers=num_workers,
        )
        return dataloader

    def ground_truth(self) -> np.ndarray:
        return self.gt


if __name__ == "__main__":
    ds = Pitts30k_Test()
    ds = Pitts30k_Val()
