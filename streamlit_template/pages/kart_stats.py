import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")


df_kart = pd.read_csv('streamlit_template/data/kart_stats.csv')

#st.write(df_racer) Body,Weight,Acceleration,
#Standard Kart,2,4,3,3,4,3,3,3,3,3,2,3,3
#On-Road traction,Off-Road Traction,Mini-Turbo,Ground Speed,
#Water Speed,Anti-Gravity Speed,Air Speed,
#Ground Handling,Water Handling,Anti-Gravity Handling,Air Handling

df_kart_limited = df_kart[['Body','Weight', 'Acceleration','Water Speed', 'Air Handling', 'Mini-Turbo']]

st.dataframe(df_kart.style
             .highlight_max(color='green', axis=0,subset=['Acceleration','Water Speed', 'Air Handling', 'Mini-Turbo'])
             .highlight_min(color='red', axis=0,subset=['Acceleration','Water Speed', 'Air Handling', 'Mini-Turbo'])
             .highlight_max(color='red', axis=0,subset=['Weight'])
             .highlight_min(color='green', axis=0,subset=['Weight'])
             )


st.line_chart(df_kart_limited, x='Weight', y=['Acceleration', 'Water Speed', 'Air Handling', 'Mini-Turbo'])

st.scatter_chart(df_kart_limited, x='Acceleration', y=['Weight', 'Water Speed', 'Air Handling', 'Mini-Turbo'])

st.area_chart(df_kart_limited, x='Water Speed', y=['Weight', 'Acceleration', 'Air Handling'])


df_kart_fastest = df_kart[['Body', 'Air Speed','Anti-Gravity Speed', 'Ground Speed', 'Water Speed']]

st.line_chart(df_kart_fastest, x='Ground Speed', y=['Air Speed','Anti-Gravity Speed', 'Water Speed'])



st.write("Carts by Top Average Speed")
df_fastest = df_kart_fastest[['Body', 'Air Speed','Anti-Gravity Speed', 'Ground Speed', 'Water Speed']]
df_fastest['Top Average Speed'] = df_kart_fastest['Ground Speed'] + df_kart_fastest['Air Speed'] + df_kart_fastest['Anti-Gravity Speed'] + df_kart_fastest['Water Speed'] /4
df_fastest = df_fastest[['Body', 'Top Average Speed' ]].sort_values('Top Average Speed', ascending=False)
st.dataframe(df_fastest.style
                 .highlight_max(color='green'))

    


chosen_kart = st.selectbox('Select a Cart', df_kart['Body'])
df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])
df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
st.bar_chart(df_unp_kart, x='category', y='strength')



