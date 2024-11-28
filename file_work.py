import pandas as pd

def open_file():
    file_path = "./dataSet/data.csv"
    return pd.read_csv(file_path)

def check_in(df, variabls, colum):
    uniq = df[colum].unique()
    for i in variabls:
       if i not in uniq:
          print(f"Error {i} not in {colum} colum")
          return False
    return True
     
def costomize_csv(file, country_code, year_name, medals):
    if check_in(file, [country_code], "NOC"):
        df = file[file["NOC"] == country_code]
        if check_in(df, [year_name], "Year"):
            df_year = df[df["Year"] == year_name]   
            df_medals = df_year[df_year['Medal'].isin(medals)]
            return df_medals[["Name", "Sport", "Medal"]].reset_index(drop=True), True
    else:
        return file, False

def write_file(save_path, list_med):
    with open(save_path, "w") as file:
        for i in range(len(list_med[0])):
            for j in range(3):
                file.write(list_med[j][i])
                file.write(' ')
            file.write('\n')