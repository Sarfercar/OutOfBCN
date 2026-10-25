import json
from google import genai
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="OutofBCN", page_icon="✈️", layout="centered")

# Cabecera limpia y nativa de Streamlit
st.title("OutofBCN ✈️🚗")
st.markdown(
    "### Encuentra tu escapada perfecta de fin de semana desde Barcelona"
)
st.write("---")

# Formulario de preferencias
with st.form("formulario_preferencias"):
  dias = st.selectbox(
      "¿Cuántos días tienes?",
      ["1 día", "2 días (Fin de semana)", "3-4 días (Puente)"],
  )

  presupuesto = st.selectbox(
      "Presupuesto aproximado",
      [
          "Bajo (Mochilero/Económico)",
          "Medio (Equilibrado)",
          "Alto (Capricho/Premium)",
      ],
  )

  ambiente = st.selectbox(
      "¿Qué tipo de ambiente te apetece?",
      [
          "Naturaleza y Montaña",
          "Playa y Relax",
          "Cultural e Histórico",
          "Gastronómico",
          "Aventura / Activo",
      ],
  )

  transporte = st.selectbox(
      "¿Cómo te vas a desplazar desde Barcelona?",
      [
          "Coche propio / Alquiler",
          "Tren (Renfe/FGC)",
          "Autobús",
          "Avión (vuelo directo corto)",
      ],
  )

  buscar = st.form_submit_button(
      "Buscar Recomendaciones 🤖", use_container_width=True
  )

if buscar:
  # Intentar obtener la API KEY desde st.secrets de forma segura
  try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
  except Exception as e:
    st.error(
        f"🔑 Error al configurar la clave de API en los secretos: {e}"
    )
    st.stop()

  prompt_completo = f"""
    Eres un experto asesor de viajes enfocado en escapadas desde Barcelona. 
    Tu objetivo es proponer exactamente tres destinos que se adapten a la duración, presupuesto, transporte y ambiente seleccionados por el usuario. 
    Sé claro, directo y práctico. 
    
    Preferencias del usuario:
    - Duración: {dias}
    - Presupuesto aproximado: {presupuesto}
    - Ambiente deseado: {ambiente}
    - Medio de transporte desde Barcelona: {transporte}

    IMPORTANTE: Devuelve la respuesta ÚNICAMENTE en formato JSON válido (una lista de 3 objetos), sin texto adicional antes ni después ni bloques de markdown adicionales. Cada objeto debe tener exactamente estas claves:
    - "nombre": El nombre del destino.
    - "porque_encaja": Breve explicación de por qué encaja con sus preferencias.
    - "consejo_rapido": Un consejo práctico e indispensable sobre el lugar.
    """

  with st.spinner("Consultando con nuestro asesor de IA..."):
    try:
      response = client.models.generate_content(
          model="gemini-3.8-flash", contents=prompt_completo
      )

      texto_respuesta = response.text.strip()
      if texto_respuesta.startswith("```json"):
        texto_respuesta = texto_respuesta[7:]
      if texto_respuesta.endswith("```"):
        texto_respuesta = texto_respuesta[:-3]
      texto_respuesta = texto_respuesta.strip()

      destinos = json.loads(texto_respuesta)

      st.success("¡Aquí tienes tus propuestas de escapada!")

      for i, dest in enumerate(destinos, 1):
        with st.container(border=True):
          st.subheader(f"📍 Opción {i}: {dest.get('nombre')}")
          st.write(f"**¿Por qué encaja?** {dest.get('porque_encaja')}")
          st.info(f"💡 **Consejo rápido:** {dest.get('consejo_rapido')}")

    except Exception as e:
      # Si hay saturación (503) u otro error, se muestra el aviso amigable
      st.warning(
          "⚠️ El servicio de recomendaciones está experimentando una alta"
          " demanda en este momento (Error 503). Por favor, espera unos"
          " segundos y vuelve a pulsar el botón."
      )
