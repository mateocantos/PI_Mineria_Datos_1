
# 📊 Proyecto Integrador – Minería de Datos I

## Análisis Exploratorio y Reducción de Dimensionalidad sobre Datos de Usuarios de una Plataforma de Streaming


Proyecto desarrollado  para la asignatura **Minería de Datos I** de la carrera **Técnico Superior en Ciencias de Datos e Inteligencia Artificial**.

---

# 📖 Descripción

Este proyecto desarrolla un flujo completo de **Minería de Datos**, partiendo de un conjunto de datos correspondiente a usuarios de una plataforma de streaming.

El trabajo comprende todas las etapas del proceso de análisis:

- Inspección inicial del dataset.
- Preparación y limpieza de los datos.
- Análisis Exploratorio de Datos (EDA).
- Reducción de dimensionalidad mediante PCA.
- Elaboración de conclusiones.
- Desarrollo de un dashboard interactivo con Streamlit.

Todas las decisiones metodológicas fueron justificadas mediante evidencia obtenida durante el análisis, priorizando la reproducibilidad y la trazabilidad del proceso.

---

# 🎯 Objetivos

- Analizar la calidad inicial del conjunto de datos.
- Detectar valores faltantes, duplicados e inconsistencias.
- Preparar un dataset limpio para el análisis.
- Identificar patrones de comportamiento mediante EDA.
- Aplicar Análisis de Componentes Principales (PCA).
- Comunicar los resultados mediante una aplicación desarrollada en Streamlit.

---

# 🔄 Flujo de trabajo

```text
Dataset Original
        │
        ▼
01 - Inspección Inicial
        │
        ▼
02 - Calidad y Preparación
        │
        ▼
03 - Análisis Exploratorio (EDA)
        │
        ▼
04 - PCA
        │
        ▼
05 - Conclusiones
        │
        ▼
Dashboard Streamlit
```

---

# 📁 Estructura del proyecto

```text
PI_Mineria_Datos_1/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_preparacion.ipynb
│   ├── 03_analisis_exploratorio.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
│
├── reports/
│   └── informe_final.pdf
│
├── requirements.txt
│
└── README.md
```

---

# 🧹 Preparación de los datos

Durante la etapa de calidad y preparación se realizaron las siguientes tareas:

- Eliminación de registros completamente duplicados.
- Normalización de variables categóricas.
- Tratamiento de valores numéricos inválidos.
- Imputación mediante mediana para variables numéricas.
- Imputación por tipo de plan para `monthly_watch_time_mins`.
- Conservación de fechas inválidas como `NaT`.
- Generación del dataset limpio utilizado en el resto del proyecto.

Todas las decisiones fueron tomadas a partir de la evidencia obtenida durante la inspección inicial del dataset.

---

# 📈 Principales resultados

El análisis permitió obtener los siguientes hallazgos:

- El tiempo mensual de visualización presenta una distribución asimétrica con una mayoría de usuarios de consumo moderado y un grupo reducido de usuarios altamente activos.

- Los usuarios con planes **Premium** muestran, en promedio, mayores tiempos de visualización que los usuarios de planes Standard y Basic.

- La edad no evidenció una relación lineal significativa con el tiempo de visualización.

- Las correlaciones entre las variables numéricas resultaron débiles, indicando que el comportamiento de los usuarios depende de múltiples factores.

- El Análisis de Componentes Principales confirmó que ninguna variable explica individualmente la mayor parte de la variabilidad del conjunto de datos.

---

# 🧠 Análisis de Componentes Principales (PCA)

Para aplicar PCA se seleccionaron únicamente las variables numéricas del dataset.

Antes del análisis se utilizó **StandardScaler**, permitiendo que todas las variables participaran en igualdad de condiciones independientemente de su escala.

El PCA permitió:

- Reducir la dimensionalidad del conjunto de datos.
- Analizar la varianza explicada.
- Interpretar el aporte de cada variable.
- Confirmar los resultados obtenidos durante el EDA.

---

# 🛠 Tecnologías utilizadas

| Tecnología | Uso |
|------------|-----------------------------|
| Python | Desarrollo del proyecto |
| Pandas | Manipulación de datos |
| NumPy | Operaciones numéricas |
| Matplotlib | Visualización |
| Seaborn | Visualización estadística |
| Scikit-learn | PCA y StandardScaler |
| Streamlit | Dashboard interactivo |
| Jupyter Notebook | Desarrollo del análisis |

---

# 🚀 Instalación

Clonar el repositorio

```bash
git clone https://github.com/mateocantos/PI_Mineria_Datos_1.git
```

Ingresar al proyecto

```bash
cd PI_Mineria_Datos_1
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecutar la aplicación

```bash
streamlit run app/streamlit_app.py
```

---

# 📄 Informe

El informe técnico completo del proyecto se encuentra en:

```text
reports/informe_final.pdf
```

---

# 🌐 Dashboard

**Aplicación Streamlit**

> *(Agregar la URL una vez publicada.)*

---

# 💻 Repositorio

GitHub:

**https://github.com/mateocantos/PI_Mineria_Datos_1**

---

# 👨‍💻 Autor

**Mateo Cantos Lucero**

Estudiante de la carrera **Técnico Superior en Ciencias de Datos e Inteligencia Artificial**.

Proyecto desarrollado de manera individual para la asignatura **Minería de Datos I**.

---

# 📌 Observaciones

Este proyecto fue desarrollado siguiendo un enfoque reproducible de Minería de Datos, documentando cada etapa del proceso y justificando todas las decisiones de preparación y análisis a partir de la evidencia obtenida sobre el conjunto de datos.