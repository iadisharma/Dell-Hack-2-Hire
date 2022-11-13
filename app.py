# Dell Hack-2-Hire
# Team 7
# Problem Statement: Image Annotation
# Team Members : Adi Sharma, Divyadrishti Chhetri, Rajsekhor Saikia, Piyush Singh, Abhishek Kumar Jha


from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
import cv2


# creating a binary vector for the input labels 

mlb = MultiLabelBinarizer()

app = Flask(__name__)

model = load_model('mlmodel.h5')

def predict_label(img_path):
	i = tf.keras.utils.load_img(img_path, target_size=(60,80))
	i = tf.keras.utils.img_to_array(i)/255.0
	image = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
	i = image.reshape(1, 60,80,3)
	p = model.predict(i)
	pred_binarized = []
	for pred in p:
		vals = []
		for val in pred:
			if val > 0.5:
				vals.append(1)
			else:
				vals.append(0)
			pred_binarized.append(vals) 

# print(pred_binarized)
	pred_binarized = np.array(pred_binarized)   
	pred_dic= dict(enumerate(pred_binarized.flatten(), 1))
	print(pred_dic)


# we convert the output vectors to the predicted labels
	types = { 1 : 'Bags',
               2 : 'Belts',
               3 : 'Black',
               4 : 'Blue',
               5 : 'Brown',
               6 : 'Eyewear',
               7 : 'Free Gifts',
               8 : 'Green',
               9 : 'Grey',
               10 : 'Navy Blue',
			   11 : 'Pink',
			   12 : 'Purple',
               13 : 'Red',
               14 : 'Shoes',
               15 : 'Silver',
               16 : 'Topwear',
               17 : 'Watches' ,
               18 : 'White',
	}
	output=[]
	for num in range(1,18):
		if pred_dic[num]==1:
			output.append(types[num])
	return output
	       
        
 

	print(pred_test_labels)
	return pred_test_labels


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Team 7"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)