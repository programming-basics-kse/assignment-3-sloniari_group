import pandas as pd

def open_file():
    file_path = "./side/athlete_events.csv"
    return pd.read_csv(file_path)

def costomize_csv(file, country_code, year_name, medals):
    df = file[file["NOC"] == country_code]
    df_year = df[df["Year"] == year_name]   
    df_medals = df_year[df_year['Medal'].isin(medals)]
    return df_medals[["Name", "Sport", "Medal"]].reset_index(drop=True)

def write_file(save_path, list_med):
    with open(save_path, "w") as file:
        for i in range(len(list_med[0])):
            for j in range(3):
                file.write(list_med[j][i])
                file.write(' ')
            file.write('\n')

def get_countries_summary(df, countries, medals):
    answer = {}
    for country in countries:
        df_country = df[(df['Team'] == country) & (df['Medal'].isin(medals))]
        medal_count_by_year = df_country.groupby('Year').size()
        
        if not medal_count_by_year.empty:
            max_year = medal_count_by_year.idxmax()
            max_medals = medal_count_by_year[max_year]
            answer[country] = (int(max_year), int(max_medals))
        else:
            answer[country] = None 
    return answer