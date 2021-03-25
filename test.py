import pandas as pd

# s = pd.Series(["a", "b", "c"])
# print(s)

# s.append(["d"], ignore_index=True)
# print(s)

s = [["hello", 1], ["world", 2]]
df = pd.DataFrame(s, columns=['measure', 'value'])
# print(df)

s1 = [["wow", 3], ["good", 4]]
df1 = pd.DataFrame(s1, columns=['measure', 'value'])
print(df1)

df1.append(df, ignore_index=)