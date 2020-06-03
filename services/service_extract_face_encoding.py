import face_recognition

# [[image_bytes], [image_bytes], [image_bytes]]
def extractFaceMultiple(imageFileStreamList):
    imageEncoding = []
    for imageStream in imageFileStreamList:
        imageFile = face_recognition.load_image_file(imageStream)
        imageEncoding.append((face_recognition.face_encodings(imageFile))[0])
    
    return imageEncoding

def extractFaceEncoding(imageFileStream):
    imageFile = face_recognition.load_image_file(imageFileStream)
    imageEncoding = face_recognition.face_encodings(imageFile)[0]
    
    return imageEncoding

# encoding_for_file.resize((2, 128)) # Resize using your command