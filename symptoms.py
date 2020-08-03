import numpy as np
import pandas as pd 
import plotly.express as px
symptoms={'symptom':['Fever',
        'Dry cough',
        'Fatigue',
        'Sputum production',
        'Shortness of breath',
        'Muscle pain',
        'Sore throat',
        'Headache',
        'Chills',
        'Nausea or vomiting',
        'Nasal congestion',
        'Diarrhoea',
        'Haemoptysis',
        'Conjunctival congestion'],'percentage':[85.9,70.7,38.1,33.4,18.6,14.8,13.9,13.6,14.4,9.0,4.8,3.7,0.9,0.8]}#plotting the tree map

symptoms=pd.DataFrame(data=symptoms,index=range(14))
symptoms
fig = px.treemap(symptoms, path=['symptom'], values='percentage',
                  color='percentage', hover_data=['symptom'],
                  color_continuous_scale='Rainbow')
fig.show()
import plotly.io as pio
pio.write_html(fig, file='index.html', auto_open=True)#It'll save the plot as an html file.
