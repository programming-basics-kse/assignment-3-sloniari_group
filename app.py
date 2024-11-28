import pandas as pd
import sys

def totalProcess():
  
  if(sys.argv[1] == "-total" 
  and int(sys.argv[2]) >= 1896
  and int(sys.argv[2]) <= 2016):
    year = int(sys.argv[2])
    medals =["Gold", "Silver", "Bronze"]
    
    file_path = './dataSet/data.csv'
    file = pd.read_csv(file_path)
    
    df_year = file[file["Year"] == year]
    df_medals = df_year[df_year['Medal'].isin(medals)]
    
    medal_counts = (
      df_medals.groupby(['Team', 'Medal'])
      .size()
      .unstack(fill_value=0)
    )
    for team, counts in medal_counts.iterrows():
      print(f"{team} - золото: {counts['Gold']} - серебро: {counts['Silver']} - бронза: {counts['Bronze']}")
      
  elif(sys.argv[1]== '-interactive'):
    user_data = input("Enter ur country to get the data")
    file_path = './dataSet/data.csv'
    file = pd.read_csv(file_path)
    
    medals =["Gold", "Silver", "Bronze"]
    df_country = file[file['Team'].str.contains(user_data, case=False, na=False)]
    
    if df_country.empty:
        print(f"No data found for the country: {user_data}")
        return 
    
    medals = ["Gold", "Silver", "Bronze"]
    
    first_olympics = df_country.sort_values('Year').iloc[0]
    first_year = first_olympics['Year']
    the_place = first_olympics['City']
    print(f"Перша олімпіада: {first_year}, {the_place}")
    
    medal_counts = (
        df_country[df_country['Medal'].notna()]
        .groupby('Year')
        .size()
    )
    
    if medal_counts: 
        
        best_year = medal_counts.idxmax()
        best_count = medal_counts.max()
        print(f"Найкраща олімпіада: {best_year} (медалі: {best_count})")
        
        worst_year = medal_counts.idxmin()
        worst_count = medal_counts.min()
        print(f"Найгірша олімпіада: {worst_year} (медалі: {worst_count})")
        
        average_medals = medal_counts.mean()
        print(f"Average medals: {average_medals:.2f}")
    else:
        print(f"No medals data found for {user_data}.")

totalProcess()


