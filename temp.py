#Save the model
import pickle
import numpy as np
import streamlit as st


#loading saved model
#rb means read binary
loaded_model=pickle.load(open('trained_rfmodel.sav','rb'))


def horse_prediction(input_data):
    #input_data=(1.0,0,534817,88.0,20.0,3.0,1.0,1.0,4.0,2.0,1.0,50.0,85.0,2,2208,0)
    #changing input data to numpy data
    input_data_as_numpy_array=np.asarray(input_data)

    #reshape array
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction==[0]):
        return('Horse will live')
    elif(prediction==[1]):
        return('Horse will die')
    else:
        return('Horse will be Euthanized')

def main():
    #give page title
    st.title('Horse Colic Survival Prediction')
    #get input from user
    #surgery,Age,Hospital ID,pulse,respiratory rate,temperature of extremities,peripheral pulse,capillary refill time,peristalsis,abdominal distension,nasogastric reflux,packed cell volume,total protein,surgical lesion?,1,2

    surgery=st.text_input('Surgery')
    Age=st.text_input('Age')
    Hospital_ID=st.text_input('Hospital ID')
    pulse=st.text_input('Pulse')
    respiratory_rate=st.text_input('respiratory rate')
    temperature_of_extremities=st.text_input('temperature of extremities')
    peripheral_pulse=st.text_input('peripheral pulse')
    capillary_refill_time=st.text_input('capillary refill time')
    peristalsis=st.text_input('peristalsis')
    abdominal_distension=st.text_input('abdominal distension')
    nasogastric_reflux=st.text_input('nasogastric reflux')
    packed_cell_volume=st.text_input('packed cell volume')
    total_protein=st.text_input('total protein')
    surgical_lesion=st.text_input('surgical lesion?')
    one=st.text_input('1')
    two=st.text_input('2')
    #code for prediction
    diagnosis=''
    #create predict button
    if st.button('Prediction Result'):
        diagnosis=horse_prediction([surgery,Age,Hospital_ID,pulse,respiratory_rate,temperature_of_extremities,peripheral_pulse,capillary_refill_time,peristalsis,abdominal_distension,nasogastric_reflux,packed_cell_volume,total_protein,surgical_lesion,one,two])
        st.success(diagnosis)

if __name__=='__main__':
    main()
