from file_work import open_file, costomize_csv, write_file, get_countries_summary
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings
import sys, os

def main():
    save_file = False
    sec_arg = ["-medals", "-total", "-overall", "-interactive"]
    if sys.argv[1] not in  sec_arg:
        print("Error: The '-medals/overall/total/interactive' argument must be the second argument.")
        sys.exit(1)

    if len(sys.argv) == 6 and sys.argv[4] == '-output':
        save_file = True
        save_path = sys.argv[5]

    if sys.argv[1] == sec_arg[0]:
        country_name = sys.argv[2]
        year_name = int(sys.argv[3])
        medals =["Gold", "Silver", "Bronze"] 

        file = open_file()

        df_medalists = costomize_csv(file, country_name, year_name, medals)
        print(df_medalists.head(10))

        list_med = [df_medalists["Name"].tolist()] + [df_medalists["Sport"].tolist()] + [df_medalists["Medal"].tolist()]
        print(list_med[0][0], list_med[1][0], list_med[2][0])


        if save_file:
            write_file(save_path, list_med)

    if sys.argv[1] == sec_arg[2]:
        medals =["Gold", "Silver", "Bronze"] 
        file = open_file()
        countries = []
        for i in range(2, len(sys.argv)):
            countries.append(sys.argv[i])

        summary = get_countries_summary(file, countries, medals)
        for i in countries:
            print(i, summary[i])


if __name__ == "__main__":
    main()
