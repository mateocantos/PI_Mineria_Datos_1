"""App Streamlit - Página principal (Home)."""
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st

st.set_page_config(page_title="PI Minería de Datos · Streaming", page_icon="🎬", layout="wide")

# ---- Datos del proyecto ----
INTEGRANTE = "Cantos Lucero Mateo"
COMISION   = "Sede Nodo"
FECHA      = "29 de junio de 2026"
REPO       = "https://github.com/mateocantos/PI_Mineria_Datos_1"

st.markdown(
    "<div style='padding:6px 0 2px'>"
    "<span style='letter-spacing:3px;font-size:13px;color:#C084FC;font-weight:700'>"
    "PROYECTO INTEGRADOR · MINERÍA DE DATOS I</span></div>",
    unsafe_allow_html=True,
)
st.title("🎬 Análisis de usuarios de una plataforma de streaming")
st.markdown(
    "<p style='font-size:18px;color:#B8B2CC;margin-top:-6px'>"
    "Análisis exploratorio reproducible: inspección, calidad de datos, EDA y reducción de "
    "dimensionalidad (PCA).</p>",
    unsafe_allow_html=True,
)

st.divider()

c1, c2, c3 = st.columns(3)
c1.markdown(f"**👤 Integrante**\n\n{INTEGRANTE}")
c2.markdown(f"**🏷️ Comisión**\n\n{COMISION}")
c3.markdown(f"**📅 Fecha**\n\n{FECHA}")

st.divider()

st.subheader("Contexto")
st.write(
    "Este proyecto analiza un conjunto de **8.034 usuarios** de una plataforma de streaming "
    "(datos demográficos, hábitos de consumo y uso del servicio). El objetivo fue construir un "
    "análisis **reproducible y comunicable** —inspección, calidad y preparación de datos, "
    "análisis exploratorio y PCA— con decisiones **justificadas en evidencia**. No es un "
    "proyecto de modelado predictivo."
)

st.info("Usá el menú lateral para recorrer: **Dataset · EDA · PCA · Conclusiones**.")

st.markdown(f"🔗 **Repositorio en GitHub:** {REPO}")
st.caption("Esta aplicación comunica resultados para público general; la evidencia técnica completa está en el repositorio.")
