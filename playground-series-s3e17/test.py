def clean_data(df):
    for col in df:
        df = df.rename(
            columns={
                col: col.lower()
                .replace(" ", "_")
                .replace("[", "")
                .replace("]", "")
                .replace("(", "")
                .replace(")", "")
            }
        )
    return df


print("hell" )
