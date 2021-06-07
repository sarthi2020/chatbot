# -*- coding: utf-8 -*-
"""chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dii60cpzuSgwBxCFv6HKwWzmrFFrJJxX
"""


import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer 
import tensorflow as tf 
from tensorflow.keras import Sequential 
from tensorflow.keras.layers import Dense, Dropout
import streamlit as st
from tensorflow.keras.models import load_model
nltk.download("punkt")
nltk.download("wordnet")
class Chatbot:
	def __init__(self):
		self.data = {"indents":[{
		    "type":"greetings",
		    "questions":["Hi","Hello","How are you?","Hi there","Hey"],
		    "answers": ["Hi","Hello, nice to meet you","Hi, I am your friend Kim","Hi nice to meet you"]
		    },
		    {"type":"age",
		     "questions":["What is your age?","When were you born?","How old are you?","When is your birthday?"],
		     "answers":["I am 2 years old","I was born on 1st april 2019"]
		    },
		    {"type": "date",
		    "questions": ["what are you doing this weekend?",
		    "do you want to hang out some time?", "what are your plans for this week","What are your weekend plans"],
		    "answers": ["I am available all week", "I don't have any plans", "I am not busy"]
		    },
		    {"type": "name",
		      "questions": ["what's your name?", "what are you called?", "who are you?"],
		      "answers": ["My name is kim", "I'm Kim", "Kim"]
		    },
		    {"type": "goodbye",
		      "questions": [ "Bye", "Goodbye", "see ya", "it was nice talking to you","See you later"],
		      "answers": ["It was nice talking to you", "See you later", "Speak soon!"]
		    },
		    {
		    "type": "noanswer",
		    "questions": [],
		    "answers": ["Sorry not able to understand","Please give me more info", "Not sure I understand"]
		    },
		    {"type": "thanks",
         	"questions": ["Thanks", "Thank you", "That's helpful", "Awesome, thanks", "Thanks for helping me"],
         	"answers": ["Happy to help!", "Any time!", "My pleasure"],
        	},
        	{"type": "options",
         	"questions": ["How you could help me?", "What you can do?", "What help you provide?", "How you can be helpful?", "What support is offered"],
         	"answers": ["You can ask me anything"],
        },
		]}

		self.docX = []
		self.docY = []
		self.classes = []
		self.dictionary = []

		self.lemmatizer = WordNetLemmatizer()

		self.trainX = []
		self.trainY = []
		self.train = []
	
	def lemmatization(self,text):
	  tokens = nltk.word_tokenize(text)
	  output = ""
	  for word in tokens:
	    output += self.lemmatizer.lemmatize(word.lower())+" "
	  return output

	def preprocessing(self):
		for indent in self.data["indents"]:
		  self.classes.append(indent["type"])
		  for question in indent["questions"]:
		    question = self.lemmatization(question)
		    tokens = nltk.word_tokenize(question)
		    self.dictionary.extend(tokens)
		    self.docX.append(question)
		    self.docY.append(indent["type"])

		self.dictionary = [word for word in self.dictionary if word not in string.punctuation]

		#sorted to sort and set to remove duplicates
		self.dictionary = sorted(set(self.dictionary))
		self.classes = sorted(set(self.classes))

		# print(self.docX)
		# print(self.docY)
		# print(self.classes)
		# print(self.dictionary)

	def getdata(self):
		for index,question in enumerate(self.docX):
		  bow = [0]*len(self.dictionary)
		  output = [0]*len(self.classes)
		  for id,word in enumerate(self.dictionary):
		    if(word in question):
		      bow[id] = 1 
		  
		  output[self.classes.index(self.docY[index])] = 1
		  bow = list(bow)
		  # print(question)
		  # print(bow)
		  # print(sum(bow))
		  self.train.append([bow,output])

		random.shuffle(self.train)
		self.train = np.array(self.train, dtype=object)

		self.trainX = np.array(list(self.train[:, 0]))
		self.trainY = np.array(list(self.train[:, 1]))

	def training(self):
		input_shape = (self.trainX.shape[1],)
		output_shape = self.trainY.shape[1]
		epochs = 200
		# the deep learning model
		self.model = Sequential()
		self.model.add(Dense(128, input_shape=input_shape, activation="relu"))
		self.model.add(Dropout(0.5))
		self.model.add(Dense(64, activation="relu"))
		self.model.add(Dropout(0.3))
		self.model.add(Dense(output_shape, activation = "softmax"))
		adam = tf.keras.optimizers.Adam(learning_rate=0.01, decay=1e-6)
		self.model.compile(loss='categorical_crossentropy',
		              optimizer=adam,
		              metrics=["accuracy"])
		print(self.model.summary())
		self.model.fit(x = self.trainX, y = self.trainY, epochs=200, verbose=1)

	def save(self):
		self.model.save("chatbot.h5")

	def load(self):
		self.model = load_model('chatbot.h5')

	def get_prediction(self,text):
	    text = self.lemmatization(text)
	    bow = [0]*len(self.dictionary)
	    tokens = nltk.word_tokenize(text)
	    for token in tokens:
	      if token in self.dictionary:
	        bow[self.dictionary.index(token)] = 1
	    
	    # if(sum(bow)==0):
	    # 	for indent in self.data["indents"]:
	    # 		if(indent['type'] == 'noanswer'):
	    # 			finaloutput = random.choice(indent["answers"])
	    # else:
	    result = self.model.predict(np.array([bow]))[0]
	    y_pred = [[id,value] for id,value in enumerate(result)]
	    y_pred.sort(key=lambda x: x[1], reverse=True) 
	    print(y_pred)
	    output = self.classes[y_pred[0][0]]
	    print(output)
	    for indent in self.data["indents"]:
	      if(indent['type'] == output):
	        finaloutput = random.choice(indent["answers"])
	        print(finaloutput)
	    return finaloutput


if __name__ == "__main__":
	chatbot = Chatbot()
	chatbot.preprocessing()
	chatbot.getdata()
	chatbot.training()
	chatbot.save()
'''


st.title("Chatbot")
st.write("Hi, user!!!!")

input = st.text_input("Ask me anything")
print(input)
submit = st.button("Predict")
st.write("Input : Output")
print(submit)
dict = {}
if submit:
	print("heree")
	finaloutput = get_prediction(input,classes,dictionary,data)
	dict[input] = finaloutput
	for key in dict.keys():
		print(key+"   "+ dict[key])
		st.write(key+" : "+dict[key])
'''
