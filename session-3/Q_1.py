"""
Create two NumPy arrays representing the daily step counts of two friends over a week and use element-wise addition, subtraction, multiplication, and division to compare their activity levels."""

import numpy as np
first_f_step_counts  = np.array([5000,7000,10000,4000,6000,8000,1000])
second_f_step_count = np.array([10000,9000,8000,7000,6000,5000,4000])


addition = first_f_step_counts + second_f_step_count
subtract = first_f_step_counts - second_f_step_count
multiplication = first_f_step_counts * second_f_step_count
division = first_f_step_counts / second_f_step_count

print(f"addition : {addition}")
print(f"subtraction : {subtract}")
print(f"multiplication : {multiplication}")
print(f"division : {division}")