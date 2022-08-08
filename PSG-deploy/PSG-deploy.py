
import numpy as np
import pickle
import streamlit as st


# loading the saved model
#loaded_model = pickle.load(open('path_to_model', 'rb'))


# creating a function for Prediction

def BERTsentiment_prediction(input_data):
    
    #write code here if your input needs to be changed to another form before your model takes it in

    #call the function that can predict the sentiment of your input text 
    #prediction = loaded_model.prediction_function_name(input_data_reshaped)
    #print(prediction)
    print("Negative score")

  
def main():
    
    
    # giving a title
    st.title('Positive Synonym Generator - Sentiment Prediction Phase')
    
    
    # getting the input data from the user
   
    Comment = st.text_input('Enter the text or sentence:')
    
    
    # code for Prediction
    sentiment = ''
    
    # creating a button for Prediction
    
    if st.button('Get sentiment'):
        sentiment = BERTsentiment_prediction(Comment)       
        
    st.success(sentiment)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
  
    
  
