import streamlit as st

def caja_resultado(texto):
    st.markdown(
        f"""
        <div style="
            background-color: #FFEB3B; 
            color: #FF00FF; 
            padding: 20px; 
            border-radius: 15px; 
            border: 4px solid #FF00FF; 
            font-weight: 900; 
            text-align: center; 
            font-size: 22px;
            margin: 20px 0px;
            box-shadow: 5px 5px 0px #FF00FF;
        ">
             {texto} 
        </div>
        """, 
        unsafe_allow_html=True
    )

def info_custom(text: str):
    st.success(
        f"""
        <div style='background-color: #FFEB3B; color: #FF00FF; padding: 14px; border-radius: 10px; border: 1px solid #FF00FF; font-weight: 600;'>
            {text}
        </div>
        """,
        unsafe_allow_html=True,
    )
# Estilos personalizados para la página
    st.markdown("""
        <style>
            body {
                background-color: #f023b0;
                color: white;
            }
            .stApp {
                background-color: #FF69B4;
            }
            h1, h2, h3, h4, h5, h6 {
                color: white;
            }
            .stRadio {
                color: white;
            }
            .stRadio > label {
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)
    # Reemplaza la sección de estilos (líneas 16-35) con esto:

st.markdown("""
    <style>
        body {
            background-color: #f023b0;
            color: white;
        }
        .stApp {
            background-color: #FF69B4;
        }
        h1, h2, h3, h4, h5, h6 {
            color: white;
        }
        .stRadio {
            color: white;
        }
        .stRadio > label {
            color: white;
        }
        /* Estilos para los radio buttons */
        .stRadio > div > label > div:first-child {
            background-color: #FFEB3B;  /* Rosa palo */
            border-color: #FFEB3B;
        }
        .stRadio > div > label > div:first-child input:checked ~ div {
            background-color: #FFEB3B;  /* Amarillo cuando se selecciona */
            border-color: #FDD835;
        }
        /* Para inputs checked */
        [data-testid="stRadio"] input:checked {
            accent-color: #FFEB3B;  /* Amarillo */
        }
    </style>
""", unsafe_allow_html=True)


st.title("¿Qué juguete sexual va contigo?")

# --- Pregunta 1 (ramificación principal) ---
st.header("¿Qué zona quiere ser la protagonista hoy?")
op1 = st.radio(
    "",
    ("A) El clítoris, que lleva años pidiendo un aumento de sueldo ", 
     "B) El punto G, que está más escondido que mi dignidad un domingo",
     "C) La vulva entera, que yo soy muy de repartir juego ",
     "D) El ano, que una es curiosa",
     "E) El pene, que ya no sabe dónde meterse")
)

# Guardamos la rama
rama = op1[0]  # "A" o "B"

# -------------------------------------------------------
# Preguntas 2, 3, 4
# -------------------------------------------------------

st.header("¿Qué estudiaste para intentar sobrevivir a la vida? ")
op2 = st.radio(
    "",
    ("A) Artes y Humanidades, porque me encanta sufrir por gusto ", 
     "B) Sociales y Jurídicas, discuto hasta con el panadero",
     "C) Ciencias, yo y las fórmulas, un romance tóxico",
     "D) Ciencias de la Salud, curo hasta los males inventados",
     "E) Ingeniería y Arquitectura, construyo cosas… y luego ya veremos ")
)

st.header("¿En qué etapa vital estás dando guerra? ")
op3 = st.radio(
    "",
    ("A) 18–29. Cuesta abajo y sin frenos", 
     "B) 30–44. Tengo amores repetidos",
     "C) 45–64. La cagué, burt lancaster",
     "D) +65. Elena Francis, mi psicóloga")
)

st.header("Cuando te pregunto por tu género, ¿qué me dices?")
op4 = st.radio(
    "",
    ("A) Mujer, hija, mujer ", 
     "B) Hombre, ¿qué pasa? ", 
     "C) ¿Por qué elegir? ")
)
st.header("¿Cómo te llevas con tu cuerpo?")
op5 = st.radio(
    "",
    ("A) Somos íntimos, casi mejores amigos", 
     "B) Bien, pero podríamos vernos más",
     "C) A veces no nos entendemos, como yo con Hacienda",
     "D) Mi cuerpo me habla y yo pensando en otra cosa ")
)
st.header("¿Qué tipo de estímulos te gustan?")
op6 = st.radio(
    "",
    ("A) Suaves, que yo soy delicada", 
     "B) Constantes, que no me mareen",
     "C) Sorprendentes, dame salseo",
     "D) Intensos, que se note que tengo callo")
)
st.header("¿Qué buscas cuando te dedicas un ratito íntimo?")
op7 = st.radio(
    "",
    ("A) Relajarme, que falta me hace", 
     "B) Conocerme, porque alguien tendrá que hacerlo",
     "C) Pasarlo bien, sin tesis doctoral",
     "D) Sentirlo todo, como en los Bridgerton")
)
st.header("¿Cómo te gusta el lubricante?")
op8 = st.radio(
    "",
    ("A) Sedoso, que me deje más fina que un jamón de bellota", 
     "B) Denso, que no se escape ni la vergüenza",
     "C) Ligerito, que fluya como mis ganas",
     "D) Que huela rico, pero sin parecer ambientador de taxi")
)
st.header("¿Te va el salseo con sabores?")
op9 = st.radio(
    "",
    ("A) Sí, hija, dame la frutería entera", 
     "B) Algo suave, que no quiero sentir que me estoy comiendo un flash",
     "C) Sin sabores, que bastante sabor tengo en mi vida",
     "D) Con olor rico, pero sin parecer vela del Tiger")
)
st.header("¿Qué sensaciones te llaman más?")
op10 = st.radio(
    "",
    ("A) Las relajantes, que si me acelero me tienen que bajar del techo", 
     "B) Las que me dejan pensando si llamo al fisio o al cura",
     "C) Un menú degustación, que luego no sé ni por dónde me ha venido",
     "D) Las envolventes, que me dejen blandita como un flan")
)
st.header("¿Cada cuánto visitas la cueva?")
op11 = st.radio(
    "",
    ("A) Varias veces por semana, porque me lo merezco", 
     "B) Una vez por semana, como quien riega una planta",
     "C) De vez en cuando",
     "D) Casi nunca… y luego me quejo")
)

st.header("¿Qué tal te llevas con las novedades?")
op12 = st.radio(
    "",
    ("A) Me tiro de cabeza", 
     "B) Me apunto, pero sin prisas ",
     "C) Solo si me siento segur@",
     "D) Mira, déjame con mis cosas" )
)
st.header("¿Qué nivel de travesura manejas?")
op13 = st.radio(
    "",
    ("A) Light, que yo soy más de “ay qué mono” que de “ay qué miedo”", 
     "B) Medio, un poquito de picante para no dormirme",
     "C) Alto, que me gusta el riesgo pero sin ambulancia",
     "D) Nivel Paquita: “sujétame el cubata que voy”")
)
st.header("¿Qué tipo de juego te llama más? ")
op14 = st.radio(
    "",
    ("A) Dados o cartas, que me pone el azar ", 
     "B) Plumas y antifaces, que soy misteriosa pero fina",
     "C) Látigos, cuerdas o mordazas… que una tiene fantasías",
     "D) Todo lo anterior, que yo soy muy de packs completos")
)
st.header("¿Qué ambiente te ayuda a conectar contigo?")
op15 = st.radio(
    "",
    ("A) Luz suave, que si me veo de golpe me asusto yo sola", 
     "B) Un sitio calmado, que como haya ruido me desconcentro y me pongo nerviosa",
     "C) Me quiero sentir como “La maja desnuda”",
     "D) Un rincón íntimo, donde ni el gato me juzgue")
)
st.header("¿Qué accesorio te vendría mejor ahora mismo?")
op16 = st.radio(
    "",
    ("A) Un limpiador, que la higiene es sexy ", 
     "B) Una bolsa con profundidad, como yo ",
     "C) Aceite de masaje, que quiero que se me corra hasta el DNI",
     "D) Todo, hija, que yo soy muy de “ya que estamos…”")
)
st.header("¿Eres de preparar el ambiente?")
op17 = st.radio(
    "",
    ("A) Sí, yo lo monto todo: luces, olores y hasta el escenario por si acabamos empotrando muebles ", 
     "B) Lo justo, que si me lío mucho se me calienta antes la cabeza que el coño",
     "C) Nada, hija, yo voy directa como un tren sin frenos a la estación final",
     "D) Depende: hay días que soy porno suave y otros que soy categoría “no apto para menores ni para mi madre”")
)
st.header("¿Cómo describirías tu experiencia en tu intimidad?")
op18 = st.radio(
    "",
    ("A) Estoy empezando, chica, tranquilízate", 
     "B) Tengo práctica, que una ha vivido cosas",
     "C) Bastante experiencia, no te voy a mentir, hija",
     "D) Poco explorad@, pero con más ganas que Indiana con un látigo")
)
st.header("¿Qué necesitas ahora mismo?")
op19 = st.radio(
    "",
    ("A) Bajar estrés", 
     "B) Reconectar con mi cuerpo",
     "C) Probar algo nuevo",
     "D) Subir la intensidad")
)
st.header("¿Qué estilo va más contigo?")
op20 = st.radio(
    "",
    ("A) Tranquilo y minimalista", 
     "B) Curioso y explorador",
     "C) Creativo y cambiante",
     "D) Intenso y apasionado")
)
st.header("¿Qué tal te llevas con los juguetes sexuales?")
op21 = st.radio(
    "",
    ("A) Somos íntimos, casi familia", 
     "B) Tengo alguno por casa",
     "C) Ninguno… pero no por falta de ganas")
)
# -------------------------------------------------------
# Procesar respuestas
# -------------------------------------------------------

if st.button("Ver resultado"):
    # Generar secuencia de preguntas 2 a 4
    seq = op2[0] + op3[0] + op4[0] + op5[0] + op6[0] + op7[0] + op8[0] + op9[0] + op10[0] + op11[0] + op12[0] + op13[0] + op14[0] + op15[0] + op16[0] + op17[0] + op18[0] + op19[0] + op20[0]+ op21[0]

    st.write("Secuencia generada:", seq)

    # --- LÓGICA CORREGIDA ---
    # Si la persona eligió grupo A → muestra finales del grupo A
    # Si la persona eligió grupo B → muestra finales del grupo B
    # Las otras preguntas NO cambian la rama principal

    if rama == "A":
        # Final principal del grupo A depende de secuencia AAA
        if seq == "CAAAAAABABAAAAAAAAAB":
            caja_resultado("Resultado: La Caricia Mojada (A)")
        else:
            if rama == "A":
            # Final principal del grupo A depende de secuencia AAA
                if seq == "BAABAAABABCAABAAAAAB":
                    caja_resultado("Resultado: La Caricia Mojada (A)")
                else:
                    if rama == "A":
                        if seq == "AAAAAACBACBAAAABAAAC":
                            caja_resultado("Resultado: La Caricia Mojada (A)")
                        else:
                            if rama == "A":
                                if seq == "BAABCBCBCBBBABBBBCBB":
                                    caja_resultado("Resultado: La Novata (A)")
                                else:  
                                    if rama == "A":
                                        if seq == "AAABCBCCBBBBABBCBCBB":
                                            caja_resultado("Resultado: La Novata (A)")
                                        else:
                                            if rama == "A":
                                                if seq == "CAABCCCBCBBBABBBBCBC":
                                                    caja_resultado("Resultado: La Novata (A)")
                                                else:
                                                    caja_resultado("Ups, esta combinación no la hemos hecho")

            # Si no coincide con AAA, igualmente se queda en grupo A,
            # solo que recibe un final alternativo del grupo A

    
    if rama == "C":
        # Final principal del grupo A depende de secuencia AAA
        if seq == "AACBCDAACBABDCDBBCCA":
            caja_resultado("Resultado: La Navaja Suiza (C)")
        else:
            if rama == "C":
            # Final principal del grupo A depende de secuencia AAA
                if seq == "BACBCCACCBABDDDBBCCB":
                    caja_resultado("Resultado: La Navaja Suiza (C)")
                else:
                    if rama == "C":
                        if seq == "AACCCDAACCACDCCBCCA":
                            caja_resultado("Resultado: La Navaja Suiza (C)")
                        else:
                            if rama == "C":
                                if seq == "ABAAAADBDBBBBACABAAB":
                                    caja_resultado("Resultado: La Romantica Guarrilla (C)")
                                else:  
                                    if rama == "C":
                                        if seq == "ABABAAACDBBABACABAAB ":
                                            caja_resultado("Resultado: La Romantica Guarrilla (C)")
                                        else:
                                            if rama == "C":
                                                if seq == "BBAABADBCBBBBACBBABB ":
                                                    caja_resultado("Resultado: La Romantica Guarrilla (C)")
                                                else:
                                                    if rama == "C":
                                                        if seq == "CACBCCCACBBCDCDDCCCB":
                                                            caja_resultado("Resultado: La kamasutras (C)")
                                                        else:
                                                            if rama == "C":
                                                                if seq == "BACBCDCACBCCDCDDCCCB ":
                                                                    caja_resultado("Resultado: La kamasutras (C)")
                                                                else:  
                                                                    if rama == "C":
                                                                        if seq == "CACCCCCBCCBDDCDDCCCB  ":
                                                                            caja_resultado("Resultado: La kamasutras (C)")
                                                                        else:
                                                                            if rama == "C":
                                                                                if seq == "CCCDDDBABADDDDDCCDDA ":
                                                                                    caja_resultado("Resultado: La Vibraluxe (C)")
                                                                                else:
                                                                                    if rama == "C":
                                                                                        if seq == "CCCCDCBABBDDDDDCCDDC ":
                                                                                            caja_resultado("Resultado: La Vibraluxe (C)")
                                                                                        else:
                                                                                            if rama == "C":
                                                                                                if seq == "CCCDCDBABADCDDDCCDDA ":
                                                                                                    caja_resultado("Resultado: La Vibraluxe (C)")
                                                                                                else:
                                                                                                    caja_resultado("Ups, esta combinación no la hemos hecho")
    if rama == "D":
        # Final principal del grupo A depende de secuencia AAA
        if seq == "CBABDDBABAACCCCCCDDA":
            caja_resultado("Resultado: La Turbo Coño (D)")
        else:
            if rama == "D":
            # Final principal del grupo A depende de secuencia AAA
                if seq == "BBACDCBABAADCCCCCDDA":
                    caja_resultado("Resultado: La Turbo Coño (D)")
                else:
                    if rama == "D":
                        if seq == "CBABCDBABBACDCCCCDDB":
                            caja_resultado("Resultado: La Turbo Coño (D)")
                        else:
                            if rama == "D":
                                if seq == "BCACBBBCBCCBCBABBDBB":
                                    caja_resultado("Resultado: La Ojetelux (D)")
                                else:  
                                    if rama == "D":
                                        if seq == "CCACBCBCBCDBCBABBDBB":
                                            caja_resultado("Resultado: La Ojetelux (D)")
                                        else:
                                            if rama == "D":
                                                if seq == "BCADBBBDBCCCCBABBDBC":
                                                    caja_resultado("Resultado: La Ojetelux (D)") 
                                                else:                                               
                                                    caja_resultado("Ups, esta combinación no la hemos hecho")                                                                                                              
