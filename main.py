import pandas as pd
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings
import sys

if 5 < len(sys.argv) < 7:
    print("Error: Incorrect input argument.")
    sys.exit(1)
if sys.argv[2] != "-medals":
    print("Error: The '-medals' argument must be the second argument.")
    sys.exit(1)

country_name = sys.argv[3]
year_name = sys.argv[4]


file_path = "assignment-3-sloniari_group\side\athlete_events.csv"

file = pd.read_csv(file_path)

df = file[file["NOC"] == country_name]
print(df)
df_year = df[df["Year"] == year_name]
print(df_year)
arg = file["Team"].unique()

# with open('text.txt', 'w') as file:
#     for country in arg:
#         file.write(country +"\n" )

# parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
# parser.add_argument("-c", "--country", default="SE", help="Two-letter country code")
# parser.add_argument("-l", "--length", default=40, type=int, help="Length of time series to fit the ARIMA model")
# parser.add_argument("-s", "--start", default=0, type=int, help="Starting offset to fit the ARIMA model")
# args = vars(parser.parse_args())