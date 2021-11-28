#Save the model
import pickle
import numpy as np
import streamlit as st


#loading saved model
#rb means read binary

def choose_model():

    option = st.sidebar.selectbox('Select a model', ('Random Forest','Decision Tree','Support Vector Machine'))

    if option =='Random Forest':
        return(pickle.load(open('trained_rfmodel.sav','rb')))
    elif option =='Decision Tree':
        return(pickle.load(open('trained_dtmodel.sav','rb'))) 
    else:
        return(pickle.load(open('trained_svmmodel.sav','rb')))
    

loaded_model = choose_model()

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

    surgery=st.text_input('Surgery (1 = Yes, it had surgery, 2 = It was treated without surgery )')
    Age=st.text_input('Age (0 = Adult horse, 1 = Young (< 6 months) )')
    Hospital_ID=st.text_input('Hospital ID')
    pulse=st.text_input('Pulse (30-40 is normal for adults )')
    respiratory_rate=st.text_input('Respiratory rate (normal rate is 8 to 10)')
    temperature_of_extremities=st.text_input('temperature of extremities (1 = Normal, 2 = Warm, 3 = Cool, 4 = Cold )')
    peripheral_pulse=st.text_input('peripheral pulse (1 = normal, 2 = increased, 3 = reduced, 4 = absent )')
    capillary_refill_time=st.text_input('capillary refill time (1 = < 3 seconds, 2 = >= 3 seconds)')
    peristalsis=st.text_input('peristalsis (1 = hypermotile, 2 = normal, 3 = hypomotile, 4 = absent )' )
    abdominal_distension=st.text_input('abdominal distension (1 = none, 2 = slight, 3 = moderate, 4 = severe )')
    nasogastric_reflux=st.text_input('nasogastric reflux (1 = none, 2 = > 1 liter, 3 = < 1 liter )')
    packed_cell_volume=st.text_input('packed cell volume (normal range is 30 to 50)')
    total_protein=st.text_input('total protein (normal values lie in the 6-7.5 (gms/dL))')
    surgical_lesion=st.text_input('surgical lesion? (1 = Yes, 2 = No )')
    st.subheader('Type of lesion')
    st.text('First number is site of lesion: 1 = gastric, 2 = sm intestine, 3 = lg colon, 4 = lg colon and cecum, 5 = cecum, 6 = transverse colon, 7 = retum/descending colon, 8 = uterus, 9 = bladder, 11 = all intestinal sites, 00 = none')
    st.text('Second number is type: 1 = simple, 2 = strangulation, 3 = inflammation, 4 = other')
    st.text('Third number is subtype: 1 = mechanical, 2 = paralytic, 0 = n/a')
    st.text('Fourth number is specific code: 1 = obturation, 2 = intrinsic, 3 = extrinsic, 4 = adynamic, 5 = volvulus/torsion, 6 = intussuption, 7 = thromboembolic, 8 = hernia, 9 = lipoma/slenic incarceration, 10 = displacement, 0 = n/a')
    one=st.text_input('lesion 1')
    two=st.text_input('lesion 2')
    
    #code for prediction
    diagnosis=''
    #create predict button
    if st.button('Prediction Result'):
        diagnosis=horse_prediction([surgery,Age,Hospital_ID,pulse,respiratory_rate,temperature_of_extremities,peripheral_pulse,capillary_refill_time,peristalsis,abdominal_distension,nasogastric_reflux,packed_cell_volume,total_protein,surgical_lesion,one,two])
        st.success(diagnosis)

if __name__=='__main__':
    main()
