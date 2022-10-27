import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import hydralit_components as hc
import plotly.graph_objects as go
from streamlit_option_menu import option_menu


### Page layout

st.set_page_config(
    page_title="Instagram Prediction",
    layout="wide",
)

### Import Dataset

df = pd.read_csv('https://raw.githubusercontent.com/sarakaddoura/Projects/main/healthcare-dataset-stroke-data.csv')


### Navigation

selected = option_menu(None, ["Home", "Patient Background","Patient Records", "Analysis"],
    icons=['house',"list-task","list-task", 'gear'],
    menu_icon="cast", default_index=0, orientation="horizontal")

### Page 1

if selected == "Home":
    #if st.checkbox('Show Dataset'):
    #    data = data
    #    data

    st.markdown(f'<h1 style="color:red;font-size:35px;">{"Stroke"}</h1>', unsafe_allow_html=True)

    col1,col2 = st.columns(2)

    col1.text_area('Intoduction','''
A stroke is a serious life-threatening medical condition that happens when the blood supply to part of the brain is cut off. Strokes are a medical emergency and urgent treatment is essential. The sooner a person receives treatment for a stroke, the less damage is likely to happen.
''', height = 170)

    image = 'https://img.freepik.com/free-vector/brain-stroke-ishemic_206049-256.jpg?w=2000'
    col2.image(image, use_column_width= True)

### Page 2

if selected == "Patient Background":

    ### Replacing Null Values

    df['bmi'].fillna(value=df['bmi'].mean(), inplace=True)

    ### Dropping a value in column

    df.drop(df[df['gender'] == 'Other'].index, inplace = True)

    ### Renaming Columns

    df.rename(columns = {'hypertension':'hypertension1','heart_disease':'heart_disease1','stroke':'stroke1'}, inplace = True)

    ### 0/1 to yes/no

    df["hypertension2"] = df["hypertension1"].map({1: "Yes",0: "No"})
    df["heart_disease2"] = df["heart_disease1"].map({1: "Yes",0: "No"})
    df["stroke2"] = df["stroke1"].map({1:"Yes",0: "No"})

    ### Calculating Values

    value1=sum(df['gender'] == 'Female')
    value2=sum(df['gender'] == 'Male')
    value3 = value1/(value1+value2) *100
    value4= "{:.1f}%".format(value3)
    value5 = value2/(value1+value2) *100
    value6 = "{:.1f}%".format(value5)
    value7 = df['id'].nunique()
    value8 = value="{:,}".format(value7)


    ### Columns

    info = st.columns(4)

    theme_bad = {'bgcolor': '#f9f9f9','title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-user-friends'}
    theme_neutral = {'bgcolor': '#f9f9f9','title_color': 'pink','content_color': 'pink','icon_color': 'pink', 'icon': 'fa fa-female'}
    theme_good = {'bgcolor': '#EFF8F7','title_color': 'lightskyblue','content_color': 'lightskyblue','icon_color': 'lightskyblue', 'icon': 'fa fa-male'}


    with info[0]:
        hc.info_card(title= '# of Patients', content = value8, theme_override = theme_bad)

    with info[1]:
        hc.info_card(title = 'Females',content= value4 , sentiment='good', theme_override = theme_neutral)

    with info[2]:
        hc.info_card(title = 'Males',content= value6 , sentiment='good', theme_override = theme_good)


    ### Columns

    col1,col2,col3 = st.columns((1,1,1))


    with col1:

        ## Fig 1

        def age_group(age):
            if   age >= 0 and age <= 20:
                return "0-20"
            elif age > 20 and age <= 40:
                return "20-40"
            elif age > 40 and age <= 50:
                return "40-50"
            elif age > 50 and age <= 60:
                return "50-60"
            elif age > 60:
                return "60+"

        df['age_group'] = df['age'].apply(age_group)
        df.sort_values('age', inplace = True)

        labels = df['age_group'].value_counts().index
        values = df['age_group'].value_counts()
        colors = ['','','lightgrey','#EFEFEF','#F7F7F7']

        fig1 = go.Figure(data = [
            go.Pie(
            labels = labels,
            values = values,
            hole = .5)
            ])

        fig1.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))


        fig1.update_layout(title='Patients age groups')
        col1.plotly_chart(fig1,use_container_width = True)

        ###Fig 2

        fig2 = px.histogram(df, x="work_type",text_auto=True).update_xaxes(categoryorder = 'total descending')
        fig2.update_yaxes(title='y', visible=False, showticklabels=False)
        fig2.update_layout(title='Work Status')
        fig2.update_layout(xaxis_title=None)
        col2.plotly_chart(fig2,use_container_width = True)

        ### Fig 3

        fig3 = px.histogram(df, x="stroke2",color="gender", pattern_shape="stroke2").update_xaxes(categoryorder = 'total descending')
        fig3.update_yaxes(title='y', visible=False, showticklabels=False)
        fig3.update_layout(title='Stroke Status')
        fig3.update_layout(xaxis_title=None)
        col3.plotly_chart(fig3,use_container_width = True)

        ### Fig 4

    override_theme_2 = {'bgcolor': '#636EFA','content_color': 'white','progress_color': 'red'}

    hc.progress_bar(65,'65% are Married','35% are not',override_theme=override_theme_2)


### Page 3

if selected == "Patient Records":

    ### columns
    col1,col2 = st.columns(2)

    ### Fig 1

    def bmi_range(bmi):
        if   bmi <= 18.5 :
            return "Underweight"
        elif bmi > 18.5 and bmi < 24.9:
            return "Healthy Weight"
        elif bmi > 25 and bmi < 29.9:
            return "Overweight"
        elif bmi > 30 and bmi < 39.9:
            return "Obese"

    df['bmi_range'] = df['bmi'].apply(bmi_range)
    df.sort_values('bmi', inplace = True)

    labels = df['bmi_range'].value_counts().index
    values = df['bmi_range'].value_counts()
    colors = ['red','#ff5050','lightgrey','#EFEFEF']

    fig1 = go.Figure(data = [
            go.Pie(
            labels = labels,
            values = values,
            hole = .5)
        ])

    fig1.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))


    fig1.update_layout(title='Patients Weight Status')
    col1.plotly_chart(fig1,use_container_width = True)


    ### Fig 2

    def glucose_level(avg_glucose_level):
        if  avg_glucose_level  <= 140 :
            return "Normal"
        elif avg_glucose_level >= 140 and avg_glucose_level <= 199:
            return "Prediabetes"
        elif avg_glucose_level >= 200 :
            return "Diabetes"

    df['glucose_level'] = df['avg_glucose_level'].apply(glucose_level)
    df.sort_values('avg_glucose_level', inplace = True)

    labels = df['glucose_level'].value_counts().index
    values = df['glucose_level'].value_counts()
    colors = ['#636EFA','red','lightgrey']

    fig2 = go.Figure(data = [
        go.Pie(
        labels = labels,
        values = values,
        hole = .5)
    ])

    fig2.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))

    fig2.update_layout(title='Patients Glucose Level')
    col2.plotly_chart(fig2,use_container_width = True)

    override_theme_2 = {'bgcolor': '#636EFA','content_color': 'white','progress_color': 'red'}

    st.write("Hypertension")
    hc.progress_bar(10,'10% Have ',override_theme=override_theme_2)
    st.write("Heart Diseases")
    hc.progress_bar(6,'6% Have',override_theme=override_theme_2)


if selected == "Analysis":

    ###Renaming Columns

    df.rename(columns = {'hypertension':'hypertension1','heart_disease':'heart_disease1','stroke':'stroke1'}, inplace = True)

    ### 0/1 to yes/no

    df["hypertension2"] = df["hypertension1"].map({1: "Yes",0: "No"})
    df["heart_disease2"] = df["heart_disease1"].map({1: "Yes",0: "No"})
    df["stroke2"] = df["stroke1"].map({1:"Yes",0: "No"})

    ###columns

    col1,col2,col3 = st.columns(3)

    ### Fig1

    plt.figure(figsize=(1,1))
    fig1 = sns.lmplot(x='age', y='avg_glucose_level', hue='stroke2', data=df, markers=["o", "x"], palette="Set1")
    fig1.set(xticklabels=[])
    fig1.set(yticklabels=[])
    col1.pyplot(fig1)

    ### fig2

    plt.figure(figsize=(1,1))
    fig2 = sns.lmplot(x='bmi', y='avg_glucose_level', hue='stroke2', data=df,
               markers=["o", "x"], palette="Set1")
    fig2.set(xticklabels=[])
    fig2.set(yticklabels=[])
    col2.pyplot(fig2)

    ### fig3

    plt.figure(figsize=(1,1))
    fig2 = sns.lmplot(x='age', y='bmi', hue='stroke2', data=df,
               markers=["o", "x"], palette="Set1")
    fig2.set(xticklabels=[])
    fig2.set(yticklabels=[])
    col3.pyplot(fig2)

    expander = st.expander("Analysis")
    expander.write("""
- In general, the top 3 main causes of stroke are high blood pressure, smoking and heart diseases. However, after analyzing and visualizing this dataset i realized that its an imbalanced data with most of the cases labeled as No Stroke.
- As shown in the above plots, the higher the age, bmi and blood pressure, the more the chances of getting a stroke is present.
    """)
