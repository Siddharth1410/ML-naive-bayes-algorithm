#Siddharth Vadgama
#1001397508
import os
import sys
import pandas as pd
import numpy as np
from numpy import genfromtxt
##Training##
training_file_path=sys.argv[1]
test_file_path=sys.argv[2]
training_file=os.path.basename(training_file_path)
test_file=os.path.basename(test_file_path)


def guassian(mean,std,x):
    prob=(1/np.sqrt(2*np.pi*std*std))*np.exp((-1)*(x-mean)*(x-mean)/(2*std*std))
    return prob
ins = open( training_file, "r" )
data = [[float(n) for n in line.split()] for line in ins]
rows,cols=np.shape(data)
col_vec=[i for i in range(1,cols+1)]
#row_vec=[i for i in range(1,rows+1)]
training_dataframe=pd.DataFrame(data,columns=col_vec)
#training_dataframe.iloc[0][cols]
counter_dict={}
counter=0
for i in range(rows):
    if training_dataframe.iloc[i][cols] in counter_dict.keys():
        counter_dict[training_dataframe.iloc[i][cols]]=counter_dict[training_dataframe.iloc[i][cols]]+1
    else:
        counter_dict[training_dataframe.iloc[i][cols]]=1
    counter=counter+1
for x in counter_dict:
    counter_dict[x]=float(counter_dict[x]/counter)
list_of_means = []
list_of_std = []

for x in sorted(counter_dict.keys()):
    df1=training_dataframe[training_dataframe[cols]==x]
    mean_series = df1.mean()
    std_series = df1.std()
    list_of_means.append(mean_series.values)
    list_of_std.append(std_series.values)
df_means=pd.DataFrame(list_of_means,columns=col_vec)
df_std=pd.DataFrame(list_of_std,columns=col_vec)
df_std=df_std.where(df_std>=0.01,0.01)
df_std[cols]=df_means[cols]
df_row,df_col=df_std.shape

for i in range(df_row):
    for j in range(1,df_col):
        pass
        print('Class =%d'%df_means.iloc[i][cols],'Attribute =%d'%j,"mean = %.2f" % df_means.iloc[i][j],"std = %0.2f"%df_std.iloc[i][j])
ins_test = open( test_file, "r" )
data_test = [[float(n) for n in line.split()] for line in ins_test]
rows_test,cols_test=np.shape(data_test)
col_vec_test=[i for i in range(1,cols_test+1)]
num_of_t=1
#row_vec_test=[i for i in range(1,rows_test+1)]
test_dataframe=pd.DataFrame(data_test,columns=col_vec_test)
#p_test=guassian(df_means.iloc[0][1],df_means.iloc[0][1],test_dataframe[1][1])
#p_test_norm= normpdf(df_means.iloc[0][1],df_means.iloc[0][1],test_dataframe[1][1])
#print(p_test)
#print(p_test_norm)
test_dataframe
correct=0
ties_classified=False
for i in range(rows_test):
    test_prob_class={}
    for k in sorted(counter_dict):
        pi_Ck_given_xj=1
        for j in range(1,cols_test):
            test_x=test_dataframe.iloc[i][j]
            test_class=k
            prob_Ck=counter_dict[k]
            mean=df_means[df_means[cols_test]==float(k)][j].tolist()
            #need the index because std df last is all 0
            #or change the last column of std df. copy mean
            mean=df_means[df_means[cols_test]==float(k)][j].tolist()
            std=df_std[df_std[cols_test]==float(k)][j].tolist()
            prob_Ck_given_xj=guassian(mean[0],std[0],test_x)
            pi_Ck_given_xj=pi_Ck_given_xj*prob_Ck_given_xj
        prob_final=pi_Ck_given_xj*counter_dict[k]
        test_prob_class[k]=prob_final
    accuracy=0.00
    classified_class=max(counter_dict.keys(), key=(lambda k: test_prob_class[k]))
    if classified_class == test_dataframe.iloc[i][cols_test]:
        correct=correct+1
        accuracy=1.00
    elif ties_classified:
        accuracy=1/num_of_t
    else:
        accuracy=0.00
    print('ID = %5d, '%(i+1),'predicted =%3d, '%classified_class,'true =%3d, '%test_dataframe.iloc[i][cols_test],'probability = %.4f, '%test_prob_class[classified_class],'accuracy = %4.2f '%accuracy)

classification_accuracy=correct/rows_test
print('\n\n')
print('classification_accuracy = %6.4f'%classification_accuracy)
