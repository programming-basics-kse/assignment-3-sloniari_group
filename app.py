import pandas as pd
import sys
import os

def totalProcess():
  
  file_path = './dataSet/data.csv'
  file = pd.read_csv(file_path)
  medals =["Gold", "Silver", "Bronze"]
  
  if(sys.argv[1] == "-total" 
  and int(sys.argv[2]) >= 1896
  and int(sys.argv[2]) <= 2016):
    year = int(sys.argv[2])
    
    df_year = file[file["Year"] == year]
    df_medals = df_year[df_year['Medal'].isin(medals)]
    
    medal_counts = (
      df_medals.groupby(['Team', 'Medal'])
      .size()
      .unstack(fill_value=0)
    )
    for team, counts in medal_counts.iterrows():
      print(f"{team} - золото: {counts['Gold']} - серебро: {counts['Silver']} - бронза: {counts['Bronze']}")
      
  elif sys.argv[1] == "-interactive":
    user_data = input("Enter your country to get the data: ")
    
    df_country = file[file["Team"] == user_data]
    df_medals = df_country[df_country['Medal'].isin(medals)]

    if df_medals.empty:
      print(f"No data found for the country: {user_data}")
      pass
    
    first_olympics = df_medals.sort_values('Year').iloc[0]
    first_year = first_olympics['Year']
    the_place = first_olympics['City']
    print(f"Перша олімпіада: {first_year}, {the_place}")
    
    medal_counts = (
        df_medals[df_medals['Medal'].notna()]
        .groupby('Year')
        .size()
    )
    
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

totalProcess()


