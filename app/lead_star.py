import pandas as pd

df = pd.read_csv("/home/shoarya/Desktop/leadomator/app/lead_comb_test.csv")

def get_value():
    unused = df[df["Is_use"] == False]

    if not unused.empty:
        print(unused.iloc[0])
    else:
        print("All the lead are completely in excel no new data")

if __name__ == "__main__":
    get_value()