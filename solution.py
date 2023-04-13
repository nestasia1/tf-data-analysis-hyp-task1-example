import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 123456 # Ваш chat ID, не меняйте название переменной

# True if H0 is rejected
# Interval estimation
def solutionPropZTest(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.05

    p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')[1]
    return p_value < alpha
