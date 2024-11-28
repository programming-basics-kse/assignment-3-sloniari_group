import pandas as pd
import sys
import os
from file_work import open_file, costomize_csv, write_file, check_in

def cout_medals(medal_counts, user_data):
  if medal_counts.empty:
    print(f"No medal data available for {user_data}.")
    return 
  best_year = medal_counts.idxmax()
  best_count = medal_counts.max()
  print(f"Найкраща олімпіада: {best_year} (медалі: {best_count})")
    
  worst_year = medal_counts.idxmin()
  worst_count = medal_counts.min()
  print(f"Найгірша олімпіада: {worst_year} (медалі: {worst_count})")
    
  average_medals = medal_counts.mean()
  print(f"Середня кількість медалей: {average_medals:.2f}")

def get_countries_summary(df, countries, medals):
    answer = {}
    for country in countries:
        df_country = df[(df['NOC'] == country) & (df['Medal'].isin(medals))]
        medal_count_by_year = df_country.groupby('Year').size()
        
        if not medal_count_by_year.empty:
            max_year = medal_count_by_year.idxmax()
            max_medals = medal_count_by_year[max_year]
            answer[country] = (int(max_year), int(max_medals))
        else:
            answer[country] = None 
    return answer

def task_1(save_file, save_path):
  country_name = sys.argv[2]
  year_name = int(sys.argv[3])
  medals =["Gold", "Silver", "Bronze"] 
  file = open_file()
  df_medalists, bool_answer = costomize_csv(file, country_name, year_name, medals)

  if bool_answer:
    print(df_medalists.head(10))

    list_med = [df_medalists["Name"].tolist()] + [df_medalists["Sport"].tolist()] + [df_medalists["Medal"].tolist()]
    print(list_med[0][0], list_med[1][0], list_med[2][0])

    if save_file:
      write_file(save_path, list_med)
  else:
     print("incorrect input")


def task_2(medals):
  file = open_file()
  year = int(sys.argv[2])
    
  df_year = file[file["Year"] == year]
  df_medals = df_year[df_year['Medal'].isin(medals)]
    
  medal_counts = (
    df_medals.groupby(['NOC', 'Medal'])
    .size()
    .unstack(fill_value=0)
    )
  # print(medal_counts)
  for team, counts in medal_counts.iterrows():
    print(f"{team} - золото: {counts['Gold']} - серебро: {counts['Silver']} - бронза: {counts['Bronze']}")

def task_3(medals):
        file = open_file()
        countries = []
        for i in range(2, len(sys.argv)):
            countries.append(sys.argv[i])
        if check_in(file, countries, "NOC"):
          summary = get_countries_summary(file, countries, medals)
          for i in countries:
              print(i, summary[i])

def task_4(medals):
  file = open_file()
  user_data = input("Enter your NOC to get the data: ")
  if check_in(file, [user_data], "NOC"):
    df_country = file[file["NOC"] == user_data]
    df_medals = df_country[df_country['Medal'].isin(medals)]

    if df_medals.empty:
      print(f"No data found for the NOC: {user_data}")
      pass
      
    first_olympics = df_medals.sort_values('Year').iloc[0]
    first_year = first_olympics['Year']
    the_place = first_olympics['City']
    print(f"First Olympics: {first_year}, {the_place}")
      
    medal_counts = (
          df_medals[df_medals['Medal'].notna()]
          .groupby('Year')
          .size()
      )
    
    cout_medals(medal_counts, user_data)