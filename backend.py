import sys, json, numpy as np
import krakenex
from pykrakenapi import KrakenAPI
import decimal
import time
import nltk
import numpy as np
import random
import string
from sklearn.linear_model import LinearRegression


#connection to the kraken api
api = krakenex.API()
k = KrakenAPI(api)

#user message treatement
greeting_input = ("hello", "hi", "greetings", "what's up","hey",)
greeting_responses = ["hi !", "hey !", "hi there !", "hello !"]
farewell_input=("bye","goodbye")
simple_question_input=("open","close","high","low","vwap","volume")
possible_pairs=("bcheur","bchusd","bchxbt","xxbtzeur","xbtzusd","xethxxbt","xethzusd","xethzeur")
predictions_input=("short","long","short-term","long-term")
sample_input=("yesterday","week", "weeks")


def sentence_analyse(sentence):
    sentence = sentence.lower()
    words = {'greet':'','bye':'', 'pair':'','simple_param':'','prediction_type':'', 'sample':''}
    for word in sentence.split():
        if word.lower() in greeting_input:
            words.update({'greet':word})
        elif word.lower() in farewell_input:
            words.update({'bye':word})
        elif word.lower() in possible_pairs:
            words.update({'pair':word.upper()})
        elif word.lower() in simple_question_input:
            words.update({'simple_param':word})
        elif word.lower() in predictions_input:
            words.update({'prediction_type':word})
        elif word.lower() in sample_input:
            words.update({'sample':word})
    return words


#all patterns
def greeting(): 
    return (random.choice(greeting_responses))

def farewell():
    return ('Bye! take care.')


def simple_question(pair,simple_param):
    olhc = k.get_ohlc_data(pair)
    if(simple_param=='close'):
        response = str(olhc[0].close[0])
    if(simple_param=='open'):
        response = str(olhc[0].open[0])
    if(simple_param=='high'):
        response = str(olhc[0].high[0])
    if(simple_param=='low'):
        response = str(olhc[0].low[0])
    if(simple_param=='vwap'):
        response = str(olhc[0].vwap[0])
    if(simple_param=='volume'):
        response = str(olhc[0].volume[0])
    return ("the price of the "+simple_param+" trade of "+pair+" is " + response)

def simple_question_sample(pair, sample):
    if (sample == "weeks"):
        inter_p = "2 weeks "
        inter = 21600
    if (sample == "week"):
        inter_p = "week "
        inter = 10080
    if (sample == "yesterday"):
        inter_p = "day "
        inter = 1440
    
    olhc = k.get_ohlc_data(pair, inter)
    response = str(olhc[0].vwap[0])

    return ("The vwap of the pair "+pair +" the last " +inter_p+" is " +response)


def prediction(pair, prediction_type):
    if (prediction_type == "short" or prediction_type == "short-term"):
        sample_min=1440
        horizon="tomorrow"
    else :
        horizon="next week"
        sample_min = 10080
    olhc = k.get_ohlc_data(pair,sample_min)
    data = olhc[0].vwap.to_numpy()

    X=np.column_stack((data[1:101], data[2:102]))
    Y=data[0:100]
    prediction=[]
    #print(X)
    #print(Y)
    #print(X.shape)
    #print(Y.shape)
    reg = LinearRegression()
    reg.fit(X,Y)
    prediction = reg.predict(np.array([[Y[0],Y[1]]]))
    print(prediction)
    changement = (1-(olhc[0].vwap[0]/prediction[0]))*100
    print (changement)
    return ("with my great calculation I can say that "+horizon+" the price of "+ pair+" will be " +"{:.2f}".format(prediction[0])+" and change by "+ "{:.2f}".format(changement) +'%')

    




#all patterns reunited to create the chatbot
def bot_reflexion(sentence):
    response=''
    key_words=sentence_analyse(sentence)

    if(key_words["greet"] != ''):
        return greeting()
    elif(key_words["bye"] != '' ):
        return farewell()
    elif(key_words["pair"] != '' and key_words["simple_param"] != '' and key_words["sample"] == ''):
        return simple_question(key_words["pair"],key_words["simple_param"])
    elif(key_words["pair"] != '' and key_words["simple_param"] != '' and key_words["simple_param"]=="vwap" and key_words["sample"] != ''):
        return simple_question_sample(key_words["pair"],key_words["sample"])
    elif(key_words["pair"] != '' and key_words["prediction_type"] != '' ):
        return prediction(key_words["pair"],key_words["prediction_type"])
    else:
        return ("I don't understand what you ask")






def read_in():
    lines=sys.stdin.readlines()
    return json.loads(lines[0])

def main():
    lines  = read_in()
    outputString=bot_reflexion(lines)
    outputString = "Crypto-currency Master: " + outputString
    print (outputString)


if  __name__=='__main__':
    main()