import os

dir = os.listdir()
for f in dir:
    if f[:3].isnumeric():
        os.rename(f, f[:3])

print("Done!")