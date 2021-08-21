import random 
import statistics
import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
MathList = df["reading score"].to_list()

mean = sum(MathList)/len(MathList)
median = statistics.median(MathList)
mode = statistics.mode(MathList)


sd = statistics.stdev(MathList)
print(sd)

first_sd_start,first_sd_end=mean-sd,mean+sd
list_of_data_within_1_std_deviation = [] 
for result in MathList:
     if result > first_sd_start and result < first_sd_end:
        list_of_data_within_1_std_deviation.append(result)

print("{}% of data lies within first standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(MathList)))

second_sd_start,second_sd_end=mean-(2*sd),mean+(2*sd)
list_of_data_within_2_std_deviation = [] 
for result in MathList:
     if result > second_sd_start and result < second_sd_end:
        list_of_data_within_2_std_deviation.append(result)

print("{}% of data lies within second standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(MathList)))


third_sd_start,third_sd_end=mean-(3*sd),mean+(3*sd)
list_of_data_within_3_std_deviation = [] 
for result in MathList:
     if result > third_sd_start and result < third_sd_end:
        list_of_data_within_3_std_deviation.append(result)

print("{}% of data lies within third standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(MathList)))

print(mean)
print(median)
print(mode)