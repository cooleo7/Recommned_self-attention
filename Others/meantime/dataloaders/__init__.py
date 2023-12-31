from .base import AbstractDataloader
from meantime.datasets import dataset_factory
from meantime.utils import all_subclasses
from meantime.utils import import_all_subclasses
import_all_subclasses(__file__, __name__, AbstractDataloader)

DATALOADERS = {c.code():c
               for c in all_subclasses(AbstractDataloader)
               if c.code() is not None}

print("333")
print(DATALOADERS)

def dataloader_factory(args):
    dataset = dataset_factory(args)
    print(dataset)
    dataloader = DATALOADERS[args.dataloader_code]
    dataloader = dataloader(args, dataset)
    train, val, test = dataloader.get_pytorch_dataloaders()
    print("333!!!")
    print(len(train))
    print(len(val))
    print(len(test))
    return train, val, test


def get_dataloader(args):
    dataset = dataset_factory(args)
    dataloader = DATALOADERS[args.dataloader_code]
    dataloader = dataloader(args, dataset)
    return dataloader
