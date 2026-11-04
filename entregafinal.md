<img width="875" height="877" alt="image" src="https://github.com/user-attachments/assets/abd835ca-7c10-4cc8-b3f0-2b53b2ed05b1" /># Entrega final · OutofBCN

**Nombre y apellidos:** Sara Fernández Carmona

## 1. Enlaces

- **App principal desplegada:** [https://outofbcn.streamlit.app/](https://outofbcn.streamlit.app/)
- **Repositorio principal:** [https://github.com/Sarfercar/OutOfBCN](https://github.com/Sarfercar/OutOfBCN)
- **App extra de desarrollo:** [https://v7quiz.streamlit.app/](https://v7quiz.streamlit.app/) (Aplicación creada con los conocimientos adquiridos para sugerir destinos de la red de rutas de Volotea, con repositorio asociado en [https://github.com/Sarfercar/v7quiz](https://github.com/Sarfercar/v7quiz)).

---

## 2. Problema y usuario

Quienes residen en Barcelona y buscan improvisar un viaje corto de fin de semana suelen consultar múltiples blogs, redes sociales y buscadores, acumulando decenas de opciones dispersas sin llegar a decidirse. El problema no es la falta de información, sino el exceso de datos fragmentados y la dificultad para filtrar destinos realistas según el presupuesto, los días disponibles y el medio de transporte (coche, Rodalies, autobús o avión). La IA resuelve este proceso seleccionando, estructurando y justificando tres propuestas de destino personalizadas a partir de los criterios del usuario, mientras que fuera del alcance quedan la disponibilidad en tiempo real de billetes, las reservas de alojamiento o la compra directa.

---

## 3. Especificación

Puedes consultar la especificación completa en el repositorio o revisar su resumen técnico aplicado:

* **Funcionalidades:** 
  1. Formulario interactivo de preferencias (duración, presupuesto, ambiente y transporte desde Barcelona).
  2. Generador de recomendaciones mediante IA que devuelve tres propuestas estructuradas.
  3. Sistema de respaldo automático (*fallback*) ante incidencias de cuota o servicio.
* **Entradas y salidas:** 
  * *Entrada:* Selección de parámetros en el formulario (ej. 3 días, presupuesto medio, naturaleza, tren).
  * *Salida:* Tres tarjetas estructuradas con el nombre del destino, por qué encaja y un consejo rápido.
* **Criterios de aceptación y casos límite:** 
  * *Caso normal:* Formulario completado con preferencias equilibradas $\rightarrow$ Muestra tres propuestas de destino coherentes y bien argumentadas.
  * *Caso límite / Error de cuota:* Saturación de la API (503 / 429) $\rightarrow$ La app activa instantáneamente el respaldo local mediante `st.toast` mostrando destinos seguros (Sitges, Montserrat y Vic) sin bloquear la interfaz.

---

## 4. La pieza de IA

- **Qué usa:** API de Gemini con el SDK `google-genai` y el modelo `gemini-3.8-flash`.
- **Por qué esa opción:** Permite razonar sobre combinaciones cualitativas de viaje y generar sugerencias turísticas creativas y contextualizadas desde Barcelona de forma inmediata, sin necesidad de mantener ni estructurar una base de datos propia.
- **Qué pasa si falla:** Si se agota la cuota (`429`) o los servidores están saturados (`503`), la app intercepta el error mediante un bloque `try/except`, muestra una notificación flotante amigable (`st.toast`) y despliega tres opciones de respaldo local predeterminadas para evitar que la interfaz se quede congelada.
- **Dónde está la clave:** Configurada de forma segura en los secretos de la plataforma (`st.secrets["GEMINI_API_KEY"]`), sin rastro de credenciales expuestas en el código fuente ni en el repositorio público.

---

## 5. Proceso con IA

- **Herramientas:** Gemini CLI, Google Colab y VS Code.
- **Fichero de contexto del agente:** [AGENTS.md](https://github.com/Sarfercar/OutOfBCN/blob/main/AGENTS.md)
- **Prompts clave:**
  1. *Prompt de especificación inicial:* `"Ayúdame a redactar la especificación técnica para una app en Streamlit que recomiende 3 escapadas desde Barcelona según tiempo, presupuesto, transporte y ambiente."`
  2. *Prompt de generación del JSON:* `"Eres un experto asesor de viajes enfocado en escapadas desde Barcelona. Tu objetivo es proponer exactamente tres destinos que se adapten a la duración, presupuesto, transporte y ambiente seleccionados por el usuario. IMPORTANTE: Devuelve la respuesta ÚNICAMENTE en formato JSON válido (una lista de 3 objetos)..."`
  3. *Prompt de manejo de fallos (Solución al bloqueo de la app):* `"Escribe un bloque try/except en Python utilizando la nueva librería google-genai que capture cualquier error de la API (503/429) y despliegue un respaldo local con Sitges, Montserrat y Vic usando st.toast para evitar que la interfaz se quede pillada en el spinner."`
- **Qué delegué al agente y qué revisé a mano:** Delegué la estructura base de los componentes visuales en Streamlit, el filtrado inicial de cadenas JSON y la redacción del planteamiento técnico. Revisé y corregí a mano la captura universal de excepciones en el bloque `try/except`, la correcta lectura de variables en `st.secrets` y la integración del CSV de destinos en la app auxiliar.

---

## 6. Prueba y mejora

| Quién la probó | Qué probó | Qué pasó | Qué cambié |
|---|---|---|---|
| Yo como usuaria | Peticiones continuadas a la API de Gemini desde la interfaz de Streamlit | La app se quedaba congelada indefinidamente en el spinner *"Consultando con nuestro asesor de IA..."* al saltar errores de cuota o saturación que no estaban cubiertos por el filtro estricto de excepciones. | Modifiqué el bloque `except` para capturar de forma universal cualquier fallo de la API y programé un sistema de respaldo local (*fallback*) con `st.toast` y destinos predeterminados para garantizar una experiencia fluida. |
| Yo como usuaria | Integración de destinos comerciales en app auxiliar (`v7quiz`) | Para la herramienta de Volotea se necesitaba un filtrado estructurado que relacionase aeropuertos (IATA), duraciones y temporadas sin depender al 100% de llamadas abiertas al LLM. | Creé un archivo CSV delimitado por punto y coma (`;`) con campos como `country`, `destination`, `iata`, `interests`, `trip_length`, `seasons`, `budget_tier` y `description` para procesar y filtrar rápidamente las rutas con Pandas. |
| Compañero de clase | Introducción de parámetros extremos de presupuesto bajo y trayectos largos | El modelo sugería destinos geográficamente inviables o demasiado costosos para el transporte seleccionado. | Refiné el *system prompt* limitando estrictamente las recomendaciones a opciones alcanzables de manera realista desde Barcelona. |

---

## 7. Pitch escrito

1. Muchas personas que viven en Barcelona quieren hacer una escapada de fin de semana, pero pierden horas navegando entre recomendaciones dispersas sin saber qué encaja con su tiempo y presupuesto.
2. OutofBCN resuelve esta parálisis por análisis ofreciendo en segundos tres propuestas de destino personalizadas desde la capital catalana a través de un sencillo formulario web.
3. La IA actúa como un asesor experto que razona sobre criterios cualitativos como el ambiente o el tipo de transporte, algo que una consulta estática en bases de datos tradicionales no conseguiría.
4. Tras probar la app en producción, descubrí lo crítica que es la gestión de errores ante caídas de la API, lo que me llevó a implementar un sistema de respaldo automático que evita bloqueos en la interfaz.
5. Si continuara el proyecto, añadiría filtros avanzados para actividades específicas e integración en tiempo real con horarios de transporte público (como Rodalies o FGC), respaldado por datos de uso de usuarios reales.

---

## 8. Capturas

1. **La app funcionando en su caso principal:** Formulario de preferencias completado e interfaz respondiendo correctamente.
   <br>
   <img width="650" alt="La app funcionando" src="https://github.com/user-attachments/assets/3030aca0-99ca-4e27-bd01-806b84865b9c" />

2. **La app ante un caso límite o error:** Aviso flotante amigable (`st.toast`) activando el modo de respaldo local ante la saturación de la API.
   <br>
   <img width="650" alt="Aviso de respaldo local ante error" src="https://github.com/user-attachments/assets/d2465900-f80c-4375-8889-f74e55e5d3c1" />

3. **Trabajo con la IA (Prompting y depuración):** Conversación con el asistente para definir la lógica del prompt y la captura de excepciones universal.
   <br>
   <img width="650" alt="Trabajo con la IA - Prompting" src="https://github.com/user-attachments/assets/84442512-68ce-4dc4-868c-c95e5c0377fe" />

4. **Prueba y validación:** Interacción y revisión de la lógica de respuesta ante casos límite y estructura de datos.
   <br>
   <img width="650" alt="Prueba de la app" src="https://github.com/user-attachments/assets/fa426ee4-a149-4801-9b23-da8bd4cbf2dc" />
