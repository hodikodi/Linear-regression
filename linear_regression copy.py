import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading data from remote link
url = "student_scores - student_scores.csv"
s_data = pd.read_csv(url)

print("Data imported successfully")
