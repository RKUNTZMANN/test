import pandas as pd
import frail as fr

print('Hello World')

d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
f = fr(15)