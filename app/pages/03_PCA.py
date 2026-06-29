"""Página PCA: variables, escalamiento, varianza y cargas (máx. 2 visualizaciones)."""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import utils as u

st.set_page_config(page_title="PCA", page_icon="🧭", layout="wide")
st.title("🧭 Reducción de dimensionalidad (PCA)")

df = u.load_data()
VARS = ["age", "monthly_watch_time_mins", "customer_support_tickets"]

st.subheader("Variables utilizadas")
st.write("Se aplica PCA sobre las tres variables numéricas de comportamiento: "
         "**age**, **monthly_watch_time_mins** y **customer_support_tickets**. "
         "Se excluye `user_id` por ser un identificador, no una característica del usuario.")

st.subheader("Escalamiento")
st.write("Antes del PCA, las variables se estandarizan con **StandardScaler** (media 0, desvío 1) "
         "para que ninguna domine por su magnitud.")

X = StandardScaler().fit_transform(df[VARS].dropna())
pca = PCA().fit(X)

var = pd.DataFrame({
    "Componente": [f"PC{i+1}" for i in range(3)],
    "Varianza explicada": (pca.explained_variance_ratio_ * 100).round(1),
    "Acumulada": (pca.explained_variance_ratio_.cumsum() * 100).round(1),
})

st.subheader("Varianza explicada")
c1, c2 = st.columns([1, 1.3])
c1.dataframe(var, width='stretch', hide_index=True)
fig, ax = u.new_fig(5.5, 3.4)
ax.bar(var["Componente"], pca.explained_variance_ratio_ * 100, color=u.PALETTE[:3])
for i, v in enumerate(pca.explained_variance_ratio_ * 100):
    ax.text(i, v + 0.6, f"{v:.0f}%", ha="center", color=u.TEXT, fontsize=9)
ax.set_ylabel("% de varianza"); ax.set_ylim(0, 42)
c2.pyplot(fig)

st.subheader("Cargas de las componentes (loadings)")
cargas = pd.DataFrame(pca.components_, columns=["edad", "tiempo", "tickets"],
                      index=["PC1", "PC2", "PC3"])
fig2, ax2 = u.new_fig(6, 3)
sns.heatmap(cargas, annot=True, fmt=".2f", cmap="magma", vmin=-1, vmax=1,
            linewidths=0.5, linecolor="#0E0B16",
            annot_kws={"color": "#EDEAF5", "size": 9}, cbar_kws={"shrink": 0.8}, ax=ax2)
ax2.tick_params(colors=u.MUTED)
st.pyplot(fig2)

st.subheader("Interpretación")
st.info("La varianza se reparte de forma **pareja** entre las tres componentes (≈ 34% · 33% · 33%). "
        "PC1 se asocia sobre todo a la **edad** y los **tickets**, PC2 al **tiempo de visualización** "
        "y PC3 combina las tres. Como las variables casi no se correlacionan, cada una aporta una "
        "dimensión propia: **no se logra una reducción de dimensionalidad efectiva**. El resultado "
        "es coherente con la matriz de correlación del EDA.")
