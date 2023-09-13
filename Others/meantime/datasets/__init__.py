from .base import AbstractDataset
from meantime.utils import all_subclasses
from meantime.utils import import_all_subclasses
import_all_subclasses(__file__, __name__, AbstractDataset)

DATASETS = {c.code():c
            for c in all_subclasses(AbstractDataset)
            if c.code() is not None}

print("666")
print(DATASETS)

def dataset_factory(args):
    #print(args)
    #print(args.dataset_code)
    dataset = DATASETS[args.dataset_code]
    #print(dataset)
    return dataset(args)
