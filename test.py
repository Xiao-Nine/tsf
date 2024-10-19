import pandas as pd
import numpy as np
from data_provider.data_loader import Dataset_Custom


ds = Dataset_Custom(
    root_path='dataset',
    flag='train',
    size=[]
)