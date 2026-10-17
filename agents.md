# AGENTS.md · OutofBCN

> **Instrucciones para agentes de IA (Cursor, Copilot, Gemini CLI, etc.):** Seguir estrictamente las pautas de este archivo antes de modificar el código.

## Qué es este proyecto
Aplicación para proponer tres destinos de escapada personalizados saliendo desde Barcelona según la duración, el presupuesto, el ambiente y el transporte del usuario.

## Cómo está hecho
- Python 3.12.
- Interfaz: Streamlit.
- IA: API de Gemini con el SDK `google-genai`. El modelo está en la constante `MODELO` de `app.py`.
- Archivos: `app.py` (toda la app), `requirements.txt` (dependencias), `README.md` y `especificacion.md`.
- La especificación completa está en `especificacion.md`.

## Reglas
- La clave de la API va SIEMPRE en secretos de Streamlit (`st.secrets["GEMINI_API_KEY"]`). Nunca en el código, en el README ni en el chat.
- Cada llamada a la API va dentro de `try/except` y muestra un mensaje claro para el usuario.
- Textos de la interfaz en español, sencillos, pensados para alguien sin conocimientos técnicos.
- Cambios pequeños: uno por petición. Al terminar, explica qué has cambiado y por qué.
- Si añades una librería, añádela también a `requirements.txt` y dilo.
- No uses datos personales reales. Para probar, inventa ejemplos.

## Cómo comprobar que funciona
- Ejecuta `streamlit run app.py` en local (asegurándote de tener la clave en `.streamlit/secrets.toml`), o haz push a GitHub y revisa la app en Streamlit Community Cloud.
- Casos de prueba (entrada → lo que esperamos):
  1. Formulario completado con preferencias normales (ej. 3 días, presupuesto medio, naturaleza, coche/tren) → La app muestra tres propuestas de destino coherentes y bien argumentadas.
  2. Criterios contradictorios o extremos (ej. presupuesto muy bajo y viaje largo) → La app ofrece opciones realistas explicando amablemente cómo se adaptan a las limitaciones introducidas.
  3. Entrada fuera de tema / Error de cuota → La app muestra un mensaje claro y amigable indicando que el servicio no está disponible temporalmente.

## Qué no hacer
- No borres ni reescribas el README sin preguntar.
- Não cambies el modelo ni la arquitectura sin preguntar.
- No hagas push ni despliegues sin que yo lo haya revisado.