import streamlit as st

# ------------------ BASE DE DATOS ------------------

preguntas = [
    {"texto": "¿Dónde se jugó la final del mundial de 2010?",
     "opciones": ["Rusia", "Francia", "Sudáfrica", "Uruguay"],
     "correcta": "Sudáfrica"},

    {"texto": "¿Quién ganó el mundial en el año 2010?",
     "opciones": ["España", "Países Bajos", "Francia", "Brasil"],
     "correcta": "España"},

    {"texto": "¿Quién ganó la Champions en el Año 2018?",
     "opciones": ["Liverpool", "Barcelona", "Atlético de Madrid", "Real Madrid"],
     "correcta": "Real Madrid"},

    {"texto": "¿Quién perdió la final de la Champions en el Año 2018?",
     "opciones": ["Liverpool", "Barcelona", "Atlético de Madrid", "Real Madrid"],
     "correcta": "Liverpool"},

    {"texto": "¿Quien marcó el gol en la final del mundial de 2010?",
     "opciones": ["Robben", "Zinedine Zidane", "Andrés Iniesta", "Robinho"],
     "correcta": "Andrés Iniesta"},

    {"texto": "¿Quién ganó el primer mundial de la historia?",
     "opciones": ["Brasil", "Alemania", "Uruguay", "Argentina"],
     "correcta": "Uruguay"},

    {"texto": "¿Cuál de estos equipos tiene más champions?",
     "opciones": ["Real Betis", "Atlético de Madrid", "Celtic", "Nottingham Forest"],
     "correcta": "Nottingham Forest"},

    {"texto": "¿Quién ganó la Champions en 1970?",
     "opciones": ["AC Milan", "FC Barcelona", "Real Madrid", "Feyenoord"],
     "correcta": "Feyenoord"},

    {"texto": "¿Dónde se jugó el primer mundial de la Historia?",
     "opciones": ["Brasil", "Alemania", "Italia", "Uruguay"],
     "correcta": "Uruguay"}
]

# ------------------ INTERFAZ ------------------

st.title("Examen de Furbito")
st.write("Buena suerte, que saques buena nota. (Cada fallo resta 0,25).")

tab_examen, tab_informe = st.tabs(["📝 Examen", "📊 Informe"])

# ------------------ TAB EXAMEN ------------------

with tab_examen:

    with st.form("quiz_form"):

        respuestas_usuario = []

        for pregunta in preguntas:
            st.subheader(pregunta["texto"])
            eleccion = st.radio(
                "Elige una opción:",
                pregunta["opciones"],
                key=pregunta["texto"]
            )
            respuestas_usuario.append(eleccion)
            st.write("---")

        boton_enviar = st.form_submit_button("Entregar Examen")

# ------------------ CORRECCIÓN ------------------

if boton_enviar:

    fallos = 0
    aciertos = 0
    total = len(preguntas)

    informe_md = "# 📊 Informe del Examen\n\n"

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1
            informe_md += f"✅ **{preguntas[i]['texto']}**\n"
            informe_md += f"- Tu respuesta: {respuestas_usuario[i]}\n\n"
        else:
            fallos += 1
            informe_md += f"❌ **{preguntas[i]['texto']}**\n"
            informe_md += f"- Tu respuesta: {respuestas_usuario[i]}\n"
            informe_md += f"- Respuesta correcta: {preguntas[i]['correcta']}\n\n"

    nota_base = (aciertos / total) * 10
    penalizacion = fallos * 0.25
    notafinal = round(nota_base - penalizacion, 2)

    if notafinal < 0:
        notafinal = 0

    informe_md += "---\n"
    informe_md += f"## 🎯 Nota final: {notafinal} / 10\n"
    informe_md += f"- Aciertos: {aciertos}\n"
    informe_md += f"- Fallos: {fallos}\n"

    # Mostrar nota en tab examen
    with tab_examen:
        st.divider()
        st.header(f"Resultado final: {notafinal} / 10")

    # Mostrar informe en tab informe
    with tab_informe:
        st.markdown(informe_md)

    if notafinal >= 8:
        st.success("felicidades, has sacado muy buena nota")
        st.balloons()
    
    elif 8> notafinal >= 5:
        st.warning("Hay que estudir un poco más")

    elif notafinal < 5:
        st.success("Has suspendido")
        st.snow()
