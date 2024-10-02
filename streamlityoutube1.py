#import
import streamlit as st
import pandas as pd
import seaborn as sns

#1. title
st.title("Data Analysis")
st.subheader("Data Analysis using python and streamlit")

#2. upload dataset
upload = st.file_uploader("Upload your dataset (In CSV format)")
if upload is not None:
    data=pd.read_csv(upload)

#.3 show dataset
if upload is not None:
    if st.checkbox("Preview"):
        if st.button("Head"):
            st.write(data.head())
    if st.button("Tail"):
        st.write(data.tail())
        
#4. check for the datatype of each column
if upload is not None:
    if st.checkbox("Datatype of each column"):
        st.text("Datatype")
        st.write(data.dtypes)

#5. find the shape of the dataset(Number of rows and columns)
if upload is not None:
    data_shape= st.radio("What dimension do you want to check?",('Rows','Columns'))
    if data_shape== 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape== 'Columns':
            st.text("Number of Columns")
            st.write(data.shape[1])

#6. Find Null value of the datasets
if upload is not None:
    test=data.isnull().values.any()
    if test== True:
        if st.checkbox("Null values in the Dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
        else:
                st.success("Congratulation!!!, No Missing Values")
                
#7. Find duplicate values in the dataset
if upload is not None:
    dup=data.duplicated().any()
    if dup==True:
        st.warning("This Dataset contains some duplicate values")
        dup=st.selectbox("Do you want to remove duplicate values?",("Select one", "Yes", "No"))
    if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
    if dup=="No":
            st.text("Ok No Problem")

#7. Get overall statistics
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe())

#9. About Section
if st.button("About App"):
    st.text("Built With Streamlit")
    st.text("Thanks To Streamlit")

#10 By
if st.checkbox("By"):
    st.success('Eduwoh Eboseta')







