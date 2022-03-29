from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Bienvenue à Streamlit ! 

Editez `/streamlit_app.py` pour personnaliser cette application selon vos désirs :heart :

Si vous avez des questions, consultez notre [documentation](https://docs.streamlit.io) et nos [forums communautaires](https://docs.streamlit.io).
forums](https://discuss.streamlit.io).

En attendant, voici un exemple de ce que vous pouvez faire avec seulement quelques lignes de code :
"""


with st.echo(code_location='below'):
    total_points = st.slider("Nombre de points dans la spirale", 1, 5000, 2000)
    num_turns = st.slider("Nombre de tours de la spirale", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
