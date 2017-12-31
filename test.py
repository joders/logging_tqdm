from logging_tqdm import tqdm
import time


print("Testing tqdm-logging:")
for i in tqdm(range(100)):
    time.sleep(.02)
print("\n\n\n")


print("Testing tqdm-logging with exception:")
try:
    for i in tqdm(range(100)):
        if i == 75:
            raise Exception("Some Exception")
        time.sleep(.02)
except:
    pass
print("\n\n\n")






import pandas as pd
import numpy as np
tqdm.pandas()


print("Testing pandas tqdm-logging:")
print("Processing 10 groups (needs 11 pandas operations):")
df=pd.DataFrame({'classes':np.random.randint(0,10,size=1000), \
                 'data':np.random.randn(1000)})
df.groupby('classes').progress_apply(lambda x:(time.sleep(.2),x.mean)[1])
print("\n\n\n")


print("Testing pandas tqdm-logging with exception:")
c=0
def exceptionMean(groupData):
    global c
    c+=1
    if c==7:
        raise Exception("")
    return groupData.mean()
df.groupby('classes').progress_apply(exceptionMean)

