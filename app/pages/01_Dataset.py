"""Página Dataset: descripción, calidad, vista previa y transformaciones."""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
import utils as u

st.set_page_config(page_title="Dataset", page_icon="🗂️", layout="wide")
st.title("🗂️ Dataset")

df = u.load_data()

st.subheader("Descripción general")
st.write(
    "Cada registro representa a un **usuario** de la plataforma. El conjunto final reúne "
    f"**{df.shape[0]:,} usuarios** descritos por **{df.shape[1]} variables**: identificador, edad, "
    "plan de suscripción, minutos vistos por mes, país, género favorito, fecha de último ingreso "
    "y cantidad de tickets de soporte."
)

st.subheader("Resumen de calidad")
col1, col2, col3 = st.columns(3)
col1.metric("Filas", f"{df.shape[0]:,}")
col2.metric("Columnas", df.shape[1])
col3.metric("Valores faltantes", f"{int(df.isna().sum().sum()):,}")
st.caption(
    "El dataset original tenía 8.160 filas y 753 faltantes. Tras la limpieza quedó en 8.034 filas "
    "y 486 faltantes, todos en la fecha de último ingreso (conservados como dato ausente)."
)

st.subheader("Vista previa")
st.dataframe(df.head(15), width='stretch')

st.subheader("Transformaciones principales")
st.markdown(
    "- **Duplicados:** se eliminaron 126 registros completamente repetidos.\n"
    "- **Categorías** (plan, país, género): se unificaron las variantes de escritura "
    "(p. ej. *Básico / basico / BASICO / Basic*).\n"
    "- **Fechas:** se convirtió `last_login_date` a tipo fecha; 486 valores ambiguos o inválidos "
    "se conservaron como ausentes.\n"
    "- **Valores imposibles** (edad, tiempo de visualización y tickets): se trataron como datos "
    "inválidos y se imputaron con la mediana, siempre con evidencia.\n\n"
    "El detalle paso a paso está en los notebooks y en `logs/pipeline_log.csv`."
)
