import json
import streamlit as st
import pydeck as pdk
from snowflake.snowpark.context import get_active_session

session = get_active_session()
# Configure database name here
sql = f"select * from dummy.public.dummy"
data = session.sql(sql).collect()

# Initiate empty polygon layers array to be displayed
polygons = []

# For each data, create a dataviz layer (GeoJsonLayer)
for i in range(len(data)):
    polygonjson = json.loads(data[i]["POLYGON"])
    # st.text(polygonjson)
    elevation = data[i]["SEVERITYLEVEL"]

    polygon_layer = pdk.Layer(
        "GeoJsonLayer",
        polygonjson,
        opacity=0.8,
        stroked=False,
        filled=True,
        extruded=True,
        wireframe=True,
        get_elevation=elevation * 1000,
        get_fill_color=[123, 255, 255],
        get_line_color=[123, 255, 255],
    )

    # st.text(polygon_layer)

    polygons.append((polygon_layer))

# Define initial map state, set it to UK
INITIAL_VIEW_STATE = pdk.ViewState(latitude=52.3781, longitude=-1.4360, zoom=6, max_zoom=16, pitch=45, bearing=0)

# Create deckgl
r = pdk.Deck(layers=polygons, map_style=None, initial_view_state=INITIAL_VIEW_STATE)

# Display
st.pydeck_chart(r)
