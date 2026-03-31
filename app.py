import streamlit as st

st.title("Test con ramificación y secuencias (neutro)")

# --- Pregunta 1 (ramificación principal) ---
st.header("Pregunta 1")
op1 = st.radio(
    "¿Cuál es tu grupo?",
    ("A) Grupo A", "B) Grupo B")
)

# Guardamos la rama
rama = op1[0]  # "A" o "B"

# -------------------------------------------------------
# Preguntas 2, 3, 4
# -------------------------------------------------------

st.header("Pregunta 2")
op2 = st.radio(
    "Elige un tamaño:",
    ("A) Pequeño", "B) Grande")
)

st.header("Pregunta 3")
op3 = st.radio(
    "Elige un estilo de color:",
    ("A) Claro", "B) Oscuro")
)

st.header("Pregunta 4")
op4 = st.radio(
    "Elige una textura:",
    ("A) Suave", "B) Rugosa")
)

# -------------------------------------------------------
# Procesar respuestas
# -------------------------------------------------------

if st.button("Ver resultado"):
    # Generar secuencia de preguntas 2 a 4
    seq = op2[0] + op3[0] + op4[0]

    st.write("Secuencia generada:", seq)

    # --- LÓGICA CORREGIDA ---
    # Si la persona eligió grupo A → muestra finales del grupo A
    # Si la persona eligió grupo B → muestra finales del grupo B
    # Las otras preguntas NO cambian la rama principal

    if rama == "A":
        # Final principal del grupo A depende de secuencia AAA
        if seq == "AAA":
            st.success("✅ Resultado: Final 1 (grupo A)")
        else:
            # Si no coincide con AAA, igualmente se queda en grupo A,
            # solo que recibe un final alternativo del grupo A
            st.info("✅ Resultado: Final alternativo A")
    
    elif rama == "B":
        # Mismo concepto: secuencia BBB es el ideal,
        # pero si no sale BBB, aun así debe dar un final B.
        if seq == "BBB":
            st.success("✅ Resultado: Final 2 (grupo B)")
        else:
            st.info("✅ Resultado: Final alternativo B")
