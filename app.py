import os
from google.colab import files

# Código de la aplicación adaptado para Streamlit
codigo_streamlit = """import streamlit as st
import json
from google import genai

st.set_page_config(page_title="OutofBCN", page_icon="✈️", layout="centered")

# Estilos de cabecera
st.markdown("""
<div style='background-color: #e0f2fe; padding: 20px; border-radius: 8px; margin-bottom: 25px; text-align: center;'>
    <h1 style='color: #0369a1; margin: 0;'>OutofBCN ✈️🚗</h1>
    <p style='color: #0c4a6e; margin: 5px 0 0 0; font-size: 1.1rem;'>Encuentra tu escapada perfecta de fin de semana desde Barcelona</p>
</div>
""", unsafe_allow_html=True)

# Formulario de preferencias
with st.form("formulario_preferencias"):
    dias = st.selectbox(
        "¿Cuántos días tienes?",
        ['1 día', '2 días (Fin de semana)', '3-4 días (Puente)']
    )
    
    presupuesto = st.selectbox(
        "Presupuesto aproximado",
        ['Bajo (Mochilero/Económico)', 'Medio (Equilibrado)', 'Alto (Capricho/Premium)']
    )
    
    ambiente = st.selectbox(
        "¿Qué tipo de ambiente te apetece?",
        ['Naturaleza y Montaña', 'Playa y Relax', 'Cultural e Histórico', 'Gastronómico', 'Aventura / Activo']
    )
    
    transporte = st.selectbox(
        "¿Cómo te vas a desplazar desde Barcelona?",
        ['Coche propio / Alquiler', 'Tren (Renfe/FGC)', 'Autobús', 'Avión (Vuelo directo corto)']
    )
    
    buscar = st.form_submit_button("Buscar Recomendaciones 🤖", use_container_width=True)

if buscar:
    # Intentar obtener la API KEY desde st.secrets
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
        client = genai.Client(api_key=api_key)
    except Exception:
        st.error("🔑 Error: No se ha configurado la clave GOOGLE_API_KEY en los secretos de Streamlit (secrets.toml).")
        st.stop()

    system_prompt = """
    Eres un experto asesor de viajes enfocado en escapadas desde Barcelona. 
    Tu objetivo es proponer exactamente tres destinos que se adapten a la duración, presupuesto, transporte y ambiente seleccionados por el usuario. 
    Sé claro, directo y práctico. 
    
    Para CADA uno de los 3 destinos, debes responder en un formato JSON estructurado como una lista de objetos. 
    Cada objeto debe tener exactamente estas claves:
    - "nombre": El nombre del destino.
    - "porque_encaja": Breve explicación de por qué encaja con sus preferencias.
    - "consejo_rapido": Un consejo práctico e indispensable sobre el lugar.
    
    No inventes disponibilidad de vuelos ni precios exactos.
    Tu respuesta debe ser EXCLUSIVAMENTE el bloque de código JSON, sin textos de introducción o despedida.
    """

    user_prompt = f"""
    Quiero una escapada con estas preferencias:
    - Duración: {dias}
    - Presupuesto aproximado: {presupuesto}
    - Ambiente deseado: {ambiente}
    - Medio de transporte desde Barcelona: {transporte}
    """

    with st.spinner("Consultando con nuestro asesor de IA..."):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash-lite',
                contents=user_prompt,
                config={
                    'system_instruction': system_prompt,
                    'response_mime_type': 'application/json'
                }
            )
            
            destinos = json.loads(response.text.strip())
            
            for i, dest in enumerate(destinos, 1):
                st.markdown(f"""
                <div style='border: 1px solid #cbd5e1; border-radius: 8px; padding: 15px; background-color: #f8fafc; border-left: 6px solid #0284c7; margin-bottom: 15px;'>
                    <h3 style='margin: 0 0 8px 0; color: #0f172a;'>📍 Opción {i}: {dest.get('nombre')}</h3>
                    <p style='margin: 0 0 10px 0; color: #334155;'><strong>¿Por qué encaja?</strong> {dest.get('porque_encaja')}</p>
                    <div style='background-color: #f0fdf4; padding: 8px 12px; border-radius: 4px; font-size: 0.9rem; color: #166534; border: 1px dashed #bbf7d0;'>
                        💡 <strong>Consejo rápido:</strong> {dest.get('consejo_rapido')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"Ha ocurrido un error al generar las recomendaciones: {e}")
"""

# Escribir el archivo app.py en el entorno de Colab
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(codigo_streamlit)

print("Archivo 'app.py' generado exitosamente en el entorno. Iniciando descarga...")
# Descargar el archivo al ordenador del usuario
files.download('app.py')
