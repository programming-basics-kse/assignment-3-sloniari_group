import pandas as pd
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings
import sys

save_file = False

if 5 < len(sys.argv) < 7:
    print("Error: Incorrect input argument.")
    sys.exit(1)

if sys.argv[1] != "-medals":
    print("Error: The '-medals' argument must be the second argument.")
    sys.exit(1)

if len(sys.argv) == 6 and sys.argv[4] == '-output':
    save_file = True
    save_path = sys.argv[5]

country_name = sys.argv[2]
year_name = int(sys.argv[3])
medals =["Gold", "Silver", "Bronze"] 

file_path = "./dataSet/data.csv"
file = pd.read_csv(file_path)

df = file[file["NOC"] == country_name]
df_year = df[df["Year"] == year_name]   
df_medals = df_year[df_year['Medal'].isin(medals)]

print(df_medals['Medal'].value_counts())
df_medalists = df_medals[["Name", "Sport", "Medal"]].reset_index(drop=True)
print(df_medalists.head(10))

list_med = [df_medalists["Name"].tolist()] + [df_medalists["Sport"].tolist()] + [df_medalists["Medal"].tolist()]
<<<<<<< HEAD
print(list_med[0][0], list_med[1][0], list_med[2][0])
=======
print(list_med[0][0], list_med[1][0], list_med[2][0])
# with open('text.txt', 'w') as file:
#     for country in arg:
#         file.write(country +"\n" )

# parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
# parser.add_argument("-c", "--country", default="SE", help="Two-letter country code")
# parser.add_argument("-l", "--length", default=40, type=int, help="Length of time series to fit the ARIMA model")
# parser.add_argument("-s", "--start", default=0, type=int, help="Starting offset to fit the ARIMA model")
# args = vars(parser.parse_args())
>>>>>>> 0c815125770e14e735e7fafa6e635c67bd450c43
