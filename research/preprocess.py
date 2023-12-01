import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder




def preprocess(path_to_data):
    df = pd.read_csv(path_to_data)
    X = df.drop(columns='outcome')
    y = df['outcome']

    # Select numerical columns
    numerical_columns = X.select_dtypes(include=['int64', 'float64']).columns

    # Scale numerical columns
    scaler = StandardScaler()
    df[numerical_columns] = scaler.fit_transform(X[numerical_columns])

    # Select categorical columns
    categorical_columns = X.select_dtypes(include=['object']).columns

    # One-hot encode categorical columns
    encoder = OneHotEncoder()
    encoded_df = encoder.fit_transform(X[categorical_columns])

    # # Convert one-hot encoded data to a DataFrame
    encoded_df = pd.DataFrame(encoded_df.toarray(), columns=encoder.get_feature_names_out())

    # # Join the scaled numerical columns and one-hot encoded categorical columns
    preprocessed_df = pd.concat([df[numerical_columns], encoded_df], axis=1)

    return preprocessed_df, y



def create_train_test_split(X, y, test_size, random_state):
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y, test_size=test_size, random_state=random_state)
    return {
        'x_train':Xtrain,
        'x_test':Xtest,
        'y_train': ytrain,
        'y_test': ytest
    }

