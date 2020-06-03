import face_recognition
import pandas as pd
import numpy as np

import pickle
database_path = "encodings.pickle"
# f = open("encodings.pickle", "wb")
data = [
[-0.99934063,  0.88795481, -0.08936332, -0.07643753,  0.0080383,
0.01902981, -0.07184699, -0.09383309,  0.18518871, -0.09588896,
0.23951106,  0.0986533 , -0.22114635, -0.1363683 ,  0.04405268,
0.11574756, -0.19899382, -0.09597053, -0.11969153, -0.12277931,
0.03416885, -0.00267565,  0.09203379,  0.04713435, -0.12731361,
-0.35371891, -0.0503444 , -0.17841317, -0.00310897, -0.09844551,
-0.06910533, -0.00503746, -0.18466514, -0.09851682,  0.02903969,
-0.02174894,  0.02261871,  0.0032102 ,  0.20312519,  0.02999607,
-0.11646006,  0.09432904,  0.02774341,  0.22102901,  0.26725179,
0.06896867, -0.00490024, -0.09441824,  0.11115381, -0.22592428,
0.06230862,  -0.16559327,  0.06232892,  0.03458837,  0.09459756,
-0.18777156,  0.00654241,  0.08582542, -0.13578284,  0.0150229 ,
0.00670836, -0.08195844, -0.04346499,  0.03347827,  0.20310158,
0.09987706, -1.12370517, -0.06683611,  0.12704916, -0.02160804,
0.00984683,  0.00766284, -0.18980607, -0.19641446, -0.22800779,
0.09010898,  0.39178532,  0.18818057, -0.20875394,  0.03097027,
-0.21300618,  0.02532415,  0.07938635,  0.01000703, -0.07719778,
-0.12651891, -0.04318593,  0.06219772,  0.09163868,  0.05039065,
-0.04922386,  0.21839413, -0.02394437,  0.06173781,  0.0292527 ,
0.06160797, -0.15553983, -0.02440624, -0.17509389, -0.0630486 ,
0.01428208, -0.03637431,  0.03971229,  0.13983178, -0.23006812,
0.04999552,  0.0108454 , -1.03970895,  0.02501768,  0.08157793,
-0.03224047, -0.04502571,  0.0599995 , -0.24374914,  0.25514284,
0.24795187,  0.04060191,  0.17599922,  0.07966681,  0.01920104,
-0.01194376, -0.02300822, -0.17000897, -0.0596558 ,  0.05307484,
0.07417042,  0.07126575,  0.00200004],
[-0.20579949, 0.1225121, 0.1465642, 0.00871459, -0.03472548, -0.07330739, 0.06718618, -0.08239582, 0.10335007, -0.04267024, 0.30626237, -0.03054919
, -0.20136127, -0.1213872, 0.03250232, 0.12970835, -0.18022729, -0.11236667
, -0.02549328, -0.14668767, -0.01048119, 0.02390467, -0.0909071, 0.07733081
, -0.06603181, -0.31484622, -0.08547423, -0.10978441, 0.11437848, -0.04348643
, 0.01864032, 0.06153565, -0.15219322, -0.01366495, -0.02496105, 0.05178246
, 0.02680699, 0.0218174, 0.09333172, 0.06417929, -0.06602814, -0.03845844
, -0.01606457, 0.35882655, 0.1413478, 0.03655425, 0.03845783, 0.03694479
, -0.00083928, -0.19335663, 0.00590931, 0.14089912, 0.18356115, 0.0398422
, -0.05119799, -0.19680525, -0.10735123, 0.00073427, -0.20569351, 0.12235784
, 0.05585408, -0.13607755, -0.11977167, -0.06370632, 0.2440313, 0.11606602
, -0.14556387, -0.12269916, 0.22551814, -0.1585592, -0.01412485, 0.05020423
, -0.14079605, -0.11441281, -0.20502403, 0.14947748, 0.3768523, 0.10395876
, -0.16470982, -0.05949218, -0.20394932, 0.03618684, -0.04506093, 0.03508112
, -0.07362074, -0.01407861, -0.11153565, 0.01975995, 0.1079779, -0.01068831
, -0.01609765, 0.2009951, -0.01449224, -0.01917212, -0.03184753, -0.04247052
, -0.03480794, -0.03399953, -0.0511428, -0.08129586, -0.02545251, -0.1504539
, 0.03442406, 0.07090696, -0.20174249, 0.18321459, 0.05608436, 0.01095912
, 0.00130186, 0.09370902, -0.09851031, -0.06765404, 0.1958074, -0.20979616
, 0.20940474, 0.23967175, 0.08441924, 0.15853702, 0.00846457, 0.105646
, -0.04669958, -0.07088128, -0.0455882, -0.05248417, -0.01384374, -0.08368793
, -0.00859017, 0.03304813]]
# dta = {'data': data}
# f.write(pickle.dumps(dta))
# dat = pickle.loads(open("encodings.pickle", "rb").read())

# database_path = r"../database/facial_data.pickle"

# faceEncoding_df = pd.read_csv(database_path)
# faceEncoding_df['faceEncoding'].apply(np.array)
# # faceEncoding_df['faceID'].apply(str)

def fetchFaceID(faceEncoding):
    name = "Unknown"
    with open(database_path, 'rb') as fp:
        records = pickle.load(fp)
    # print(faceEncoding_df.head())
    # known_faces_encoding = faceEncoding_df['faceEncoding'] #.to_list()
    known_faces_encoding = records['faceEncoding']
    known_faces_ID = records['faceID']
    face_distances =[]
    for i in known_faces_encoding:
        #     face_distances.append(np.linalg.norm([i] - faceEncoding, axis=1))
        # best_match_index = np.argmin(face_distances)
        # print (best_match_index)

        matches = face_recognition.compare_faces(known_faces_encoding, faceEncoding)
        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_faces_encoding, faceEncoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_faces_ID[best_match_index]
    # print(name)
    return name


    # try:
    #     # faceID = faceEncoding_df["faceID"].loc[faceEncoding_df['faceEncoding'] == faceEncoding][0]
    #     faceID = faceEncoding_df.at[best_match_index_, "faceID"]
    #     return faceID
    # except IndexError or KeyError:
    #     return "Not found"

# array = [np.array([-0.09634063, 0.12095481, -0.00436332, -0.07643753, 0.0080383, 0.01902981, -0.07184699, -0.09383309, 0.18518871, -0.09588896, 0.23951106, 0.0986533, -0.22114635, -0.1363683, 0.04405268, 0.11574756, -0.19899382, -0.09597053, -0.11969153, -0.12277931, 0.03416885, -0.00267565, 0.09203379, 0.04713435, -0.12731361, -0.35371891, -0.0503444, -0.17841317, -0.00310897, -0.09844551, -0.06910533, -0.00503746, -0.18466514, -0.09851682, 0.02903969, -0.02174894, 0.02261871, 0.0032102, 0.20312519, 0.02999607, -0.11646006, 0.09432904, 0.02774341, 0.22102901, 0.26725179, 0.06896867, -0.00490024, -0.09441824, 0.11115381, -0.22592428, 0.06230862, 0.16559327, 0.06232892, 0.03458837, 0.09459756, -0.18777156, 0.00654241, 0.08582542, -0.13578284, 0.0150229, 0.00670836, -0.08195844, -0.04346499, 0.03347827, 0.20310158, 0.09987706, -0.12370517, -0.06683611, 0.12704916, -0.02160804, 0.00984683, 0.00766284, -0.18980607, -0.19641446, -0.22800779, 0.09010898, 0.39178532, 0.18818057, -0.20875394, 0.03097027, -0.21300618, 0.02532415, 0.07938635, 0.01000703, -0.07719778, -0.12651891, -0.04318593, 0.06219772, 0.09163868, 0.05039065, -0.04922386, 0.21839413, -0.02394437, 0.06173781, 0.0292527, 0.06160797, -0.15553983, -0.02440624, -0.17509389, -0.0630486, 0.01428208, -0.03637431, 0.03971229, 0.13983178, -0.23006812, 0.04999552, 0.0108454, -0.03970895, 0.02501768, 0.08157793, -0.03224047, -0.04502571, 0.0556995, -0.24374914, 0.25514284, 0.24795187, 0.04060191, 0.17597422, 0.07966681, 0.01920104, -0.01194376, -0.02300822, -0.17204897, -0.0596558, 0.05307484, 0.07417042, 0.07126575, 0.00209804])]
# print(array[0])
# id = fetchFaceID(np.array(data[0]))
# print(id)
# id = faceEncoding_df['faceEncoding']#.to_list() #.to_numpy()
# idd = fetchFaceID(id)
# id = faceEncoding_df['faceEncoding'].loc[faceEncoding_df['faceID'] == "obama"] #.to_numpy()
# print(i for i in np.ndenumerate(id))
# for i in id:
#     print(i)

# np.linalg.norm(faceList - searchFace, axis=1)