#####################################
from deepface import DeepFace

obj = DeepFace.analyze(img_path = "fernando3.jpg", actions = ['age', 'gender', 'race', 'emotion'])

print (obj)

#####################################

