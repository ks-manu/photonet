import face_recognition
import pandas as pd
#  app settings
# from settings.settings import d
database_path = r"./database/facial_data.csv"

faceEncoding_df = pd.read_csv(database_path)
faceEncoding_df['faceEncoding'].astype(object)

def fetchFaceEncoding(faceID):
    faceEncoding = faceEncoding_df["faceEncoding"].loc[faceEncoding_df['faceID'] == faceID][0]
    return faceEncoding