# OutofBCN ✈️🚗

**Enlace a la app:** https://outofbcn.streamlit.app  
**Autor/a:** Sara Fernández Carmona

## Pitch

Muchas personas que viven en Barcelona quieren hacer una escapada de fin de semana, pero pierden horas navegando entre recomendaciones dispersas sin saber qué encaja con su tiempo y presupuesto. OutofBCN resuelve esta parálisis por análisis ofreciendo en segundos tres propuestas de destino personalizadas desde la capital catalana. La IA actúa como un asesor experto que razona sobre criterios cualitativos (como el ambiente o el tipo de transporte) y justifica cada recomendación. Tras probar la app en producción, descubrí lo crítica que es la gestión de errores cuando la API se satura por picos de tráfico o cuota. Si continuara el proyecto, añadiría filtros para actividades específicas e integración con información de transporte en tiempo real.

## El problema

Quienes residen en Barcelona y buscan improvisar un viaje corto suelen consultar múltiples blogs, redes sociales y buscadores, guardando decenas de opciones sin llegar a decidirse. El problema no es la falta de información, sino el exceso de datos fragmentados y la dificultad para filtrar destinos realistas según el presupuesto, los días disponibles y el medio de transporte (coche, Rodalies, autobús o avión). Merece la pena resolverlo para transformar un proceso agotador de planificación en una toma de decisiones rápida, clara y sin fricción.

## Qué hace la app

1. **Formulario de preferencias:** El usuario selecciona la duración de su viaje (1 a 4 días), el presupuesto estimado, el ambiente deseado (naturaleza, playa, cultura, gastronomía o aventura) y el transporte desde Barcelona.
2. **Generación de propuestas:** Al hacer clic en "Buscar Recomendaciones", la app consulta al asesor de IA y devuelve tres opciones estructuradas en tarjetas individuales.
3. **Justificación y consejos:** Cada propuesta incluye el nombre del destino, una explicación de por qué encaja con los criterios seleccionados y un consejo práctico clave para disfrutar la escapada.

## La pieza de IA

- **Qué usa:** API de Gemini con el SDK `google-genai` y el modelo `gemini-3.8-flash`.
- **Por qué esa opción:** Permite razonar sobre combinaciones cualitativas de viaje y generar sugerencias personalizadas y bien argumentadas sin necesidad de mantener ni estructurar una base de datos propia.
- **Qué pasa si falla:** Si se agota la cuota (`429 Resource Exhausted`) o los servidores están saturados (`503 Service Unavailable`), la app activa un modo de respaldo inteligente (*fallback*) mediante una notificación `st.toast` y muestra propuestas predeterminadas accesibles desde Barcelona (Sitges, Montserrat y Vic) para evitar que la interfaz se cuelgue o devuelva pantallas de error.

## Cómo la he construido

- **Herramientas:** Gemini CLI, Google Colab y VS Code.
- **Fichero de contexto del agente:** [AGENTS.md](./AGENTS.md)
- **Prompts clave:**
  1. *Prompt de especificación inicial:* "Ayúdame a redactar la especificación técnica para una app en Streamlit que recomiende 3 escapadas desde Barcelona según tiempo, presupuesto, transporte y ambiente."
  2. *Prompt de generación del JSON:* `"Eres un experto asesor de viajes enfocado en escapadas desde Barcelona. Tu objetivo es proponer exactamente tres destinos que se adapten a la duración, presupuesto, transporte y ambiente seleccionados por el usuario. IMPORTANTE: Devuelve la respuesta ÚNICAMENTE en formato JSON válido (una lista de 3 objetos)..."`
  3. *Prompt de manejo de fallos:* "Escribe un bloque try/except en Python utilizando la nueva librería google-genai que capture errores HTTP 503/429 y muestre una alternativa local sin tumbar la app de Streamlit."
- **Qué delegué al agente y qué revisé a mano:** Delegué la estructura base de las tarjetas en Streamlit y la limpieza del marcado JSON (````json`). Revisé a mano el control de excepciones de la API, las claves de secrets en Streamlit Cloud y la consistencia de los datos en el *fallback* local.

## Prueba y mejora

| Quién la probó | Qué probó | Qué pasó | Qué cambié |
|---|---|---|---|
| Yo como usuaria | Pruebas continuadas de generación con varias preferencias | Al realizar múltiples peticiones seguidas, la app se colgaba devolviendo un error `429` (cuota superada) y `503` (servicio no disponible). | Implementé un bloque `try/except` con un sistema de respaldo local (*fallback*) que muestra opciones predeterminadas (Sitges, Montserrat, Vic) mediante un aviso amigable (`st.toast`), evitando que la app falle. |
| Yo como usuaria | Invocación de la API con el SDK | El modelo a veces devolvía el código JSON envuelto en bloques de markdown (````json ... ````), lo que hacía fallar el parseo con `json.loads()`. | Añadí una lógica de limpieza de string (`strip()` y remoción de etiquetas de markdown) antes de convertir la respuesta a un objeto JSON. |
| Compañero de clase | Introducción de criterios extremos (presupuesto muy bajo y viaje largo) | La app generaba destinos demasiado lejanos que no encajaban bien con el presupuesto indicado. | Refiné el *system prompt* exigiendo que las opciones fueran alcanzables de forma estrictamente realista desde Barcelona según el transporte elegido. |

## Capturas

<p align="center">
  <img width="641" height="908" alt="Captura de OutofBCN" src="https://github.com/user-attachments/assets/3030aca0-99ca-4e27-bd01-806b84865b9c">
</p>

## Ejecutar en local (opcional)

```bash
pip install -r requirements.txt

# Configurar la clave en .streamlit/secrets.toml:
# GEMINI_API_KEY="tu_api_key_aqui"

streamlit run app.py
