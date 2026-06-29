"""Página Conclusiones: hallazgos, limitaciones y próximos pasos."""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st

st.set_page_config(page_title="Conclusiones", page_icon="✅", layout="wide")
st.title("✅ Conclusiones")

st.subheader("Hallazgos")
st.markdown(
    "- El comportamiento de consumo se explica sobre todo por el **plan de suscripción**: a mayor "
    "nivel de plan, mayor tiempo de visualización (597 · 872 · 1.139 min).\n"
    "- La **edad no se relaciona** con el consumo (correlación 0,005) y el **género favorito tampoco** "
    "lo diferencia.\n"
    "- Las variables numéricas son **independientes** entre sí, lo que el **PCA confirma** "
    "(varianza repartida ≈ 34/33/33%, sin reducción efectiva)."
)

st.subheader("Limitaciones")
st.markdown(
    "- El análisis es **descriptivo y exploratorio**: no se aplicaron pruebas de significancia ni "
    "modelos, por lo que las asociaciones observadas no son causales.\n"
    "- El alcance está condicionado por la **calidad del dato** y por las decisiones de limpieza "
    "documentadas (imputaciones, fechas conservadas como ausentes).\n"
    "- **486 fechas** de último ingreso quedaron sin valor, lo que limita el análisis temporal.\n"
    "- El PCA, con solo tres variables no correlacionadas, tiene poco margen de reducción."
)

st.subheader("Próximos pasos")
st.markdown(
    "- Incorporar **nuevas variables** (tipo de contenido, dispositivo, antigüedad de la cuenta, "
    "sesiones) que enriquezcan el análisis.\n"
    "- **Validar** las diferencias observadas (plan–tiempo) con pruebas estadísticas.\n"
    "- Mejorar la completitud de la fecha de último ingreso para habilitar análisis temporales.\n"
    "- Avanzar hacia la **segmentación de usuarios** o el modelado (fuera del alcance actual)."
)

st.caption("Conclusiones coherentes con el informe final (reports/informe_final.pdf) y con los notebooks 03–05.")
