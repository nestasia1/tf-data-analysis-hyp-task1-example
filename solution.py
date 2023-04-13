import pandas as pd
import numpy as np
import scipy


chat_id = 1022895883 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.01

    hx = x_success / x_cnt
    hy = y_success / y_cnt
    h = (x_cnt * hx + y_cnt * hy) / (x_cnt + y_cnt)

    z_alpha = scipy.stats.norm.ppf(1- alpha)
    u = hy - hx - z_alpha * (hx*(1 - hx)/x_cnt + hy*(1 - hy)/y_cnt)**0.5
    return u > 0
