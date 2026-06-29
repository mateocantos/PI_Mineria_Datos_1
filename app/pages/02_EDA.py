"""Página EDA: 5 visualizaciones (2 univariadas, 2 bivariadas, 1 multivariada) con interpretación."""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
import seaborn as sns
import utils as u

st.set_page_config(page_title="EDA", page_icon="📈", layout="wide")
st.title("📈 Análisis exploratorio (EDA)")
st.caption("Cinco visualizaciones — cada una responde a una pregunta y cierra con su interpretación.")

df = u.load_data()
ORDEN_PLAN = ["Básico", "Estándar", "Premium"]

# ============ UNIVARIADA 1 ============
st.header("1 · ¿Cómo se distribuye el tiempo de visualización?")
fig, ax = u.new_fig(8, 3.6)
sns.histplot(data=df, x="monthly_watch_time_mins", bins=30, kde=True,
             color=u.ACCENT, edgecolor="none", ax=ax)
if ax.lines: ax.lines[0].set_color(u.ACCENT2)
ax.set_xlabel("Minutos por mes"); ax.set_ylabel("Cantidad de usuarios")
st.pyplot(fig)
st.info("**Interpretación.** La distribución es asimétrica hacia la derecha: la mayoría consume "
        "entre ~500 y ~1.200 minutos al mes (media 801, mediana 772), con una minoría de usuarios "
        "de consumo muy alto que estira el promedio.")

# ============ UNIVARIADA 2 ============
st.header("2 · ¿Cómo se reparten los planes de suscripción?")
fig, ax = u.new_fig(7, 3.6)
sns.countplot(data=df, x="subscription_plan", hue="subscription_plan", order=ORDEN_PLAN, palette=u.PALETTE[:3], legend=False, ax=ax)
ax.set_xlabel("Plan"); ax.set_ylabel("Cantidad de usuarios")
st.pyplot(fig)
st.info("**Interpretación.** Predominan los planes de menor costo: Básico 44,9%, Estándar 35,3% y "
        "Premium 19,8%. Aun así, los tres grupos tienen usuarios suficientes para comparar.")

# ============ BIVARIADA 1 ============
st.header("3 · ¿El tiempo de visualización varía según el plan?")
fig, ax = u.new_fig(7, 3.8)
sns.boxplot(data=df, x="subscription_plan", y="monthly_watch_time_mins",
            hue="subscription_plan", order=ORDEN_PLAN, palette=u.PALETTE[:3], legend=False, ax=ax)
ax.set_xlabel("Plan"); ax.set_ylabel("Minutos por mes")
st.pyplot(fig)
st.info("**Interpretación.** Sí, y es la relación más clara del análisis: el consumo crece con el "
        "nivel del plan (medias 597 · 872 · 1.139 min). Hay superposición entre grupos, así que el "
        "plan no es el único factor, pero la tendencia es consistente.")

# ============ BIVARIADA 2 ============
st.header("4 · ¿El tiempo de visualización varía según el género favorito?")
fig, ax = u.new_fig(9, 3.8)
sns.boxplot(data=df, x="favorite_genre", y="monthly_watch_time_mins", hue="favorite_genre", palette=u.PALETTE, legend=False, ax=ax)
ax.set_xlabel("Género favorito"); ax.set_ylabel("Minutos por mes")
ax.tick_params(axis="x", rotation=30)
st.pyplot(fig)
st.info("**Interpretación.** No. Las distribuciones son muy similares entre géneros, con medianas "
        "comparables y amplia superposición: el género favorito no diferencia el nivel de consumo.")

# ============ MULTIVARIADA ============
st.header("5 · ¿Cómo se relacionan entre sí las variables numéricas?")
num = df.select_dtypes(include="number").drop(columns="user_id", errors="ignore")
fig, ax = u.new_fig(5.5, 4.2)
sns.heatmap(num.corr(), annot=True, fmt=".2f", cmap="magma", vmin=-1, vmax=1,
            linewidths=0.5, linecolor="#0E0B16",
            annot_kws={"color": "#EDEAF5", "size": 9},
            cbar_kws={"shrink": 0.8}, ax=ax)
ax.tick_params(colors=u.MUTED)
st.pyplot(fig)
st.info("**Interpretación.** Las correlaciones entre edad, tiempo de visualización y tickets son "
        "casi nulas: las variables numéricas son prácticamente independientes entre sí. El consumo "
        "depende de múltiples factores y no de una sola variable numérica.")
