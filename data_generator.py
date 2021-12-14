from typing import List
from torch import LongTensor
from torch.utils.data import Dataset
from torch.utils.data import DataLoader, random_split
        
class DataGenerator(Dataset):
    def __init__(self, expr_list, res_list):
        self.x = list()
        self.y = list()
        for i, expr in enumerate(expr_list):
            self.x.append(expr)
            self.y.append(res_list[i])

    def __getitem__(self, index):
        return LongTensor(self.x[index]), LongTensor([0] + self.y[index])

    def __len__(self):
        return len(self.x)
