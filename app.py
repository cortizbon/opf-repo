import streamlit as st
import pandas as pd 
from io import BytesIO

df = pd.read_csv('data/gastos_def_2024.csv')
st.title("Repositorio de datos")

st.divider()
dictio_pgn = {'Año': "año del decreto de liquidación",
              'Sector': "sector del presupuesto",
              'Código de sector': "código asociado al sector",
              'Entidad': "entidad perteneciente a cada sector del presupuesto",
              'Código de entidad': "código asociado a la entidad",
              'Tipo de gasto': "funcionamiento, inversión o deuda",
              'apropiacion_corrientes': "valor en precios corrientes",
              'apropiacion_cons_2024': "valor en precios constantes de 2024"}
with st.expander("PGN | Datos (2013 - 2024)"):
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.subheader("Datos históricos del PGN (2013-2024)")
        st.json(dictio_pgn, expanded=False)
    
        binary_output = BytesIO()
        df.to_excel(binary_output, index=False)
        st.download_button(label = 'Descargar datos completos',
                    data = binary_output.getvalue(),
                    file_name = 'datos.xlsx')
            
        
    with col2:
        st.image("imgs/favicon.jpeg")
        st.link_button("PePE", "https://ofiscal-pepe.streamlit.app")
    