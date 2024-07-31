# # data_preprocessing.py

# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# def preprocess_data(file_path):
#     df = pd.read_csv(file_path)
#     df.fillna(0, inplace=True)
#     scaler = StandardScaler()
#     df_scaled = scaler.fit_transform(df)
#     return pd.DataFrame(df_scaled)

# if __name__ == "__main__":
#     df_preprocessed = preprocess_data('cloudtrail_logs.csv')
#     df_preprocessed.to_csv('preprocessed_logs.csv', index=False)


# data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    
    # Fill missing values
    df.fillna(0, inplace=True)
    
    # Extract numeric columns for scaling
    numeric_cols = df.select_dtypes(include=['number']).columns
    
    # Apply standard scaling to numeric columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    
    return df

if __name__ == "__main__":
    df_preprocessed = preprocess_data('cloudtrail_logs.csv')
    df_preprocessed.to_csv('preprocessed_logs.csv', index=False)
