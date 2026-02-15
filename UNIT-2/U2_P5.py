'''p 2.5:Write a program to create a data frame to maintain three students names
associated with their marks in three courses &
then add a new column named Mean to maintain the calculated
mean mark per course. Display the final data frame.'''


import pandas as pd
import numpy as np
exam_data  = {'name': ['vivek', 'vijay', 'Karan'],
				'maths': [12, 9, 16],
				'sci': [18, 10, 5], 
				'eng':[10,23,21]}
df=pd.DataFrame(exam_data)

print(df)
print(df['maths'])

