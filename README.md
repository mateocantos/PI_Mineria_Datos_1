
# 📊 Proyecto Integrador – Minería de Datos I

## Información general

Proyecto desarrollado para la asignatura **Minería de Datos I** de la carrera **Técnico Superior en Ciencias de Datos e Inteligencia Artificial**.

**Integrante**

* Mateo Cantos Lucero

El proyecto presenta un proceso completo de análisis de datos, desde la inspección inicial del dataset hasta la comunicación de resultados mediante una aplicación interactiva desarrollada con Streamlit.

---

# 🎯 Objetivo del proyecto

Desarrollar un análisis de datos reproducible y documentado sobre un conjunto de datos de usuarios de una plataforma de streaming, aplicando técnicas de inspección, preparación, análisis exploratorio y reducción de dimensionalidad mediante PCA, justificando cada decisión tomada y comunicando los resultados de forma clara e interactiva.

---

# 📂 Dataset

El conjunto de datos corresponde a usuarios de una plataforma de streaming e incluye variables demográficas, características del servicio contratado y métricas de uso de la plataforma.

Cada registro representa un usuario e incorpora información utilizada para analizar la calidad de los datos, identificar patrones de comportamiento y aplicar técnicas de reducción de dimensionalidad.

* **Dataset original:** `data/raw/`
* **Dataset procesado:** `data/processed/`

---

# 📁 Estructura del repositorio

```text
PI_Mineria_Datos_1/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
│
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 01_Dataset.py
│       ├── 02_EDA.py
│       ├── 03_PCA.py
│       └── 04_Conclusiones.py
│
├── reports/
│   └── informe_final.pdf
│
└── logs/
    └── pipeline_log.csv
```

---

# 🧹 Preparación y calidad de datos

Durante la etapa de preparación se realizó una inspección completa del conjunto de datos para identificar valores faltantes, registros duplicados, inconsistencias y formatos incorrectos.

Las principales acciones incluyeron:

* Eliminación de registros duplicados.
* Conversión de tipos de datos.
* Tratamiento de valores faltantes mediante criterios justificados.
* Normalización de variables categóricas.
* Generación del dataset limpio utilizado durante todo el análisis.

Cada transformación fue documentada en `logs/pipeline_log.csv`, permitiendo mantener la trazabilidad del proceso.

---

# 📈 Resumen del análisis exploratorio

El análisis exploratorio permitió comprender el comportamiento general de los usuarios de la plataforma.

Los principales hallazgos fueron:

* La distribución del tiempo de visualización presenta una marcada asimetría, con predominio de usuarios de consumo moderado.
* Los usuarios con planes Premium registran, en promedio, mayores tiempos de visualización que los usuarios de otros planes.
* No se observó una relación lineal significativa entre la edad y el tiempo de visualización.
* Las correlaciones entre variables numéricas fueron bajas, indicando que el comportamiento de los usuarios depende de múltiples factores.

---

# 🧠 Reducción de dimensionalidad (PCA)

El Análisis de Componentes Principales (PCA) se aplicó sobre las variables numéricas luego de realizar un escalamiento mediante **StandardScaler**.

El análisis permitió:

* Reducir la dimensionalidad del conjunto de datos.
* Analizar la varianza explicada por cada componente principal.
* Identificar el aporte relativo de las variables originales.
* Complementar los resultados obtenidos durante el análisis exploratorio.

---

# 🌐 Visualización interactiva

La aplicación fue desarrollada utilizando **Streamlit** y permite recorrer las principales etapas del proyecto mediante una interfaz interactiva.

Incluye:

* Presentación del proyecto.
* Descripción del dataset.
* Resultados del análisis exploratorio.
* Resultados del PCA.
* Conclusiones finales.

**Repositorio GitHub**

https://github.com/mateocantos/PI_Mineria_Datos_1

**Aplicación Streamlit**

https://mineriadatos1cantosluceromateo.streamlit.app

---

# ▶️ Cómo ejecutar localmente

Clonar el repositorio:

```bash
git clone https://github.com/mateocantos/PI_Mineria_Datos_1.git
```

Ingresar al proyecto:

```bash
cd PI_Mineria_Datos_1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
streamlit run app/Home.py
```

---

# 📄 Recursos del proyecto

* Notebooks: `notebooks/`
* Informe final: `reports/informe_final.pdf`
* Registro ETL: `logs/pipeline_log.csv`

---

# ✅ Conclusiones

El proyecto permitió desarrollar un proceso completo de análisis de datos siguiendo un enfoque reproducible y documentado.

Las decisiones tomadas durante las etapas de inspección, preparación, análisis exploratorio y reducción de dimensionalidad fueron justificadas mediante evidencia obtenida del conjunto de datos.

La aplicación desarrollada en Streamlit facilita la comunicación de los principales resultados de forma clara e interactiva, complementando la documentación técnica presentada en el repositorio y el informe final.
