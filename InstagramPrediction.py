###Importing Libraries
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
from PIL import Image
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
import streamlit.components.v1 as components
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor


### Page Layout

st.set_page_config(
    page_title="Instagram Prediction",
    layout="wide",
)


### Uploading Data

uploaded_data = st.sidebar.file_uploader('Upload dataset', type='csv')
if uploaded_data is not None:
  data = pd.read_csv(uploaded_data, encoding = 'ISO-8859-1')
  st.sidebar.write("Press me ⬇️")
  if st.sidebar.checkbox('Show Dataset'):
     data = data
     data

### SelectBox

add_selectbox1 = st.selectbox(
    "What would you like to see?",
    ["Overview","Google Trends","Analyzing Reach of Instagram Posts","Sources of Impressions","Analyzing Relationships","Reach Prediction"]
)
# ## Background of Streamlit

def get_base64_of_bin_file(bin_file):
    """
    function to read png file
    ----------
    bin_file: png -> the background image in local folder
    """
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

st.markdown(
    f"""
    <style>
    .stApp {{
    background: url("https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/v960-ning-30.jpg?w=800&dpr=1&fit=default&crop=default&q=65&vib=3&con=3&usm=15&bg=F4F4F3&ixlib=js-2.2.1&s=63dd5f402645ef52fb7dfb592aec765a");
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)

set_bg_hack_url()

#ECE4F5 --> hex for background

# create three columns
st.text("")
st.text("")

###Overview

if add_selectbox1 == "Overview":

    st.markdown(f'<h1 style="color:#8e97fa;font-size:35px;">{"Instagram Reach"}</h1>', unsafe_allow_html=True)


    st.text("")
    st.text("")
    txt1 = st.text_area('Intoduction','''
Instagram is one of the most popular social media applications today. People using Instagram professionally are using it to promote their business, build a portfolio, to blog, and to create various kinds of content. As Instagram is a popular application used by millions of people with different niches, it keeps on changing to make itself better for the content creators and the users. But as it keeps changing, it affects the reach of our posts that affects us in the long run. So if a content creator wants to do well on Instagram on the long run, they have to look at the data of their Instagram reach. That is where the use of Data Science in social media comes in.
''', height = 150)

    image = 'https://sm.pcmag.com/pcmag_me/news/i/instagram-/instagram-reportedly-encourages-users-to-make-second-account_h241.jpg'
    st.image(image, use_column_width= True)


if add_selectbox1 == "Google Trends":

    def main():

        html_temp = """

        <div class='tableauPlaceholder' id='viz1652904137187' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ma&#47;map3_16529035819780&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='map3_16529035819780&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ma&#47;map3_16529035819780&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1652904137187');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='1500px';vizElement.style.width='100%';vizElement.style.minHeight='1000px';vizElement.style.maxHeight='2000px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='1500px';vizElement.style.width='100%';vizElement.style.minHeight='1000px';vizElement.style.maxHeight='2000px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1000px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>  """

        st.components.v1.html(html_temp, width=1300, height=550, scrolling=False)

    if __name__ == "__main__":
        main()

    expander = st.expander("Analysis")
    expander.write("""
    Today Instagram boasts a membership numbers over 150 million. In fact, research show that Instagram offers brand engagement that is 25% higher than all other social networks. According to google trends, Instagram is undeniably one of the most important social channels around the world. It's mostly used for marketing, social life and for personal use.
 """)



### Analyzing Reach of Instagram Posts

if add_selectbox1 == "Analyzing Reach of Instagram Posts":

    ### Title
    st.markdown(f'<h1 style="color:#8e97fa;font-size:35px;">{"Distribution of Impressions From Home, Hashtags & Explore"}</h1>', unsafe_allow_html=True)

    ### KPI's for Distribution of Impressions

    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

    ### Calculating Values

    value1=sum(data['From Home'])
    value2=sum(data['From Hashtags'])
    value3=sum(data['From Explore'])

    #kpi1.write("")

    kpi2.metric(
        label="From 🏠",
        value="{:,}".format(value1),
    )


    kpi3.metric(
        label="From #️⃣'s ",
        value="{:,}".format(value2),
    )

    kpi4.metric(
        label="From 🔎",
        value="{:,}".format(value3)
    )

    kpi5.write("")

    ### Seperating Columns

    col1, col2, col3 = st.columns((1,1,1))

    ### Distribution of Impressions From Home (First Figure)

    fig1 = plt.figure(figsize=(5, 5))
    sns.distplot(data['From Home'])
    col1.plotly_chart(fig1,use_container_width = True)

    ### Distribution of Impressions From Hashtags (Second Figure)

    fig2 = plt.figure(figsize=(5, 5))
    sns.distplot(data['From Hashtags'])
    col2.plotly_chart(fig2,use_container_width = True)

    ### Distribution of Impressions From Explore (Third Figure)

    fig3 = plt.figure(figsize=(5, 5))
    sns.distplot(data['From Explore'])
    col3.plotly_chart(fig3,use_container_width = True)

    expander = st.expander("Analysis")
    expander.write("""
▪️ The majority of posts from home section have around 2k impressions scored. However, its clear by looking at the impressions from home, that its hard to reach all the followers daily, there are outliers.

▪️ As for impressions scored from hashtags, the mojority of posts have around 2k-5k impressions.

▪️ Finally for the explore section, its considered as the recommendation system of Instagram. It recommends posts to the users based on their preferences and interests just as netflix does with movies. We can observe that the majority of posts have little number of impressions in comparison to the other sources.
 """)



### Sources of Impressions

if add_selectbox1 == "Sources of Impressions":
    st.markdown(f'<h1 style="color:#8e97fa;font-size:35px;">{"Where are the sources of Impressions? "}</h1>', unsafe_allow_html=True)

    #Impressions on Instagram Posts From Various Source (Forth Figure)

    col1,col2,col3 = st.columns((2,1,1))

    home = data["From Home"].sum()
    hashtags = data["From Hashtags"].sum()
    explore = data["From Explore"].sum()
    other = data["From Other"].sum()

    labels = ['From Home','From Hashtags','From Explore','Other']
    values = [home, hashtags, explore, other]

    colors = ['#8e97fa', '#C3B1E1','#CCCCFF','#E6E6FA']

    fig4 = px.pie(data, values=values, names=labels,
                 hole=0.5)
    fig4.update_traces(marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    col1.plotly_chart(fig4, use_container_width = True)

    expander = col1.expander("Analysis")
    expander.write("""
There are many sources where Instagram impressions can be gained. When it comes to "Instagram impressions from home", this suggests the number of times a post has been seen on the main feed on Instagram. We can notice that people mostly interact and view content on the home page, followed by hashtags and explore section.
 """)

    col3.text("")
    col3.text("")
    col3.text("")

    ### Calculating Values

    value4=sum(data['From Home'])
    value5=sum(data['From Hashtags'])
    value6=sum(data['From Explore'])
    value7=sum(data['From Other'])


    col3.metric(
        label="From 🏠",
        value="{:,}".format(value4),
        delta="Highest"
    )

    col3.text("")
    col3.text("")
    col3.text("")


    col3.metric(
        label="From #️⃣'s",
        value="{:,}".format(value5),
    )

    col3.text("")
    col3.text("")
    col3.text("")

    col3.metric(
        label="From 🔎",
        value="{:,}".format(value6)
        )

    col3.text("")
    col3.text("")
    col3.text("")

    col3.metric(
        label="Other 📄",
        value="{:,}".format(value7),
        delta="-Lowest"
        )



### Analyzing Relationships

if add_selectbox1 == "Analyzing Relationships":
    st.markdown(f'<h1 style="color:#8e97fa;font-size:35px;">{"Visualizing the Correlation between Impressions and other Variables"}</h1>', unsafe_allow_html=True)

    st.text("")
    st.text("")
    st.text("")

    ###Calculating Values

    value8=sum(data['Impressions'])
    value9=sum(data['Follows'])
    value10=sum(data['Likes'])
    value11=sum(data['Saves'])


    # KPI's for Analyzing Relationships

    kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)

    kpi2.metric(
        label="Impressions 🎭",
        value="{:,}".format(value8)
    )

    kpi3.metric(
        label="Followers 👥",
        value="{:,}".format(value9),
    )


    kpi4.metric(
        label="Likes 👍",
        value="{:,}".format(value10),
    )

    kpi5.metric(
        label="Saves 📥 ",
        value="{:,}".format(value11)
    )

    st.text("")
    st.text("")
    col1, col2, col3 = st.columns((1,1,1))

    #Correlation of All Columns with Impressions Column


    #correlation = data.corr()
    #col11.text(correlation['Impressions'].sort_values(ascending=False))

    expander = st.expander("Analysis")
    expander.write("""
▪️ The correlation of Impressions is 1. The closer to 1, the more correlated
they are to impressions.

▪️ The following Columns have the highest correlation with impressions:

    👥 Follows with 0.88 correlation

    👍 Likes with 0.84 correlation

    📥 Saves with 0.77 correlation

▪️ As we can see, the more followers, likes and saves the higher
the reach on Instagram as they are strongly correlated to Impressions.

▪️ It is also reflected in the above scatter plots.
""")

    #Relationship Between Follows and Impressions (Fifth Figure)

    fig5 = px.scatter(data_frame = data, x="Impressions",
                        y="Follows", size="Follows", trendline="ols",
                        title = "Relationship Between Follows and Impressions")
    col1.plotly_chart(fig5,use_container_width = True)

    #Relationship Between Likes and Impressions (Sixth Figure)
    fig6 = px.scatter(data_frame = data, x="Impressions",
                        y="Likes", size="Likes", trendline="ols",
                        title = "Relationship Between Likes and Impressions")
    col2.plotly_chart(fig6,use_container_width = True)

    #Relationship Between Shares and Total Impressions (Seventh Figure)

    fig7 = px.scatter(data_frame = data, x="Impressions",
                        y="Saves", size="Saves", trendline="ols",
                        title = "Relationship Between Saves and Impressions")
    col3.plotly_chart(fig7,use_container_width = True)



### Reach Prediction

if add_selectbox1 == "Reach Prediction":
    st.markdown(f'<h1 style="color:#8e97fa;font-size:35px;">{"What is your Predicted Reach?"}</h1>', unsafe_allow_html=True)


### Machine learning

    #Splitting Data

    x = np.array(data[['Likes', 'Saves', 'Comments', 'Shares',
                       'Profile Visits', 'Follows']])
    y = np.array(data["Impressions"])
    xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                    test_size=0.2,
                                                    random_state=42)
    #Applying Passive Aggresive Regressor

    model = PassiveAggressiveRegressor()
    model.fit(xtrain, ytrain)
    accuracy = model.score(xtest, ytest)

    #Predict the reach of an Instagram post by giving inputs to the machine learning model

    ###Sliders
    col11,col22 = st.columns(2)

    Likes = col11.slider('Number of Likes', 0, 5000, 282)
    Saves = col11.slider('Number of Saves', 0,5000,280)
    Comments = col11.slider('Number of Comments', 0,5000,8)
    Shares = col22.slider('Number of Share', 0,5000,6)
    Profile_Visits = col22.slider('Number of Profile Visits', 0,5000,300)
    Follows = col22.slider('Number of Followers', 0,5000,6)

    features = np.array([[Likes,Saves, Comments, Shares, Profile_Visits, Follows]])
    reach = model.predict(features)


    st.balloons( )



    col1,col2 = st.columns((1,1))

    st.text("")
    st.text("")
    st.text("")

    ### Printing Results

    col1.markdown(f'<h1 style="color:#000000;font-size:35px;">{"Accuracy:"} {"{:.2f}".format(accuracy)}</h1>', unsafe_allow_html=True)
    col2.markdown(f'<h1 style="color:#000000;font-size:35px;">{"Reach Prediction:"} {"{:.2f}".format(reach[0])}</h1>', unsafe_allow_html=True)


    ### Thank you
