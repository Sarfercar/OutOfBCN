# Prompts.md · OutofBCN

Este documento recopila los *prompts* principales utilizados durante el proceso de diseño, desarrollo y depuración de la aplicación **OutofBCN**, estructurados por fases del proyecto.

---

## 1. Fase de Definición y Especificación
*Utilizado para estructurar el alcance inicial, los casos de uso y las restricciones de la app antes de escribir código.*

> **Prompt:**
> *"Ayúdame a redactar la especificación técnica para una aplicación web en Streamlit llamada OutofBCN. Su objetivo es recomendar tres escapadas de fin de semana desde Barcelona según la duración, el presupuesto, el ambiente deseado y el medio de transporte del usuario. Define el problema, el flujo del usuario, los criterios de aceptación (incluyendo casos límite como presupuestos extremos o saturación de API) y mantén un enfoque de coste cero utilizando la API de Gemini."*

---

## 2. Fase de Lógica e Ingeniería de Prompts (Core de la IA)
*El prompt maestro integrado en `app.py` para guiar al modelo a devolver datos estructurados y limpios.*

> **Prompt (System / Core Prompt):**
> ```text
> Eres un experto asesor de viajes enfocado en escapadas desde Barcelona. 
> Tu objetivo es proponer exactamente tres destinos que se adapten a la duración, presupuesto, transporte y ambiente seleccionados por el usuario. 
> Sé claro, directo y práctico. 
> 
> Preferencias del usuario:
> - Duración: {dias}
> - Presupuesto aproximado: {presupuesto}
> - Ambiente deseado: {ambiente}
> - Medio de transporte desde Barcelona: {transporte}
> 
> IMPORTANTE: Devuelve la respuesta ÚNICAMENTE en formato JSON válido (una lista de 3 objetos), sin texto adicional antes ni después ni bloques de markdown adicionales. Cada objeto debe tener exactamente estas claves:
> - "nombre": El nombre del destino.
> - "porque_encaja": Breve explicación de por qué encaja con sus preferencias.
> - "consejo_rapido": Un consejo práctico e indispensable sobre el lugar.
> ```

---

## 3. Fase de Despliegue y Resiliencia (Manejo de Errores / Fallback)
*Prompt utilizado para diseñar el sistema de respaldo automático que evita que la aplicación falle en producción ante cuotas agotadas o caídas de la API.*

> **Prompt:**
> *"Escribe un bloque `try/except` en Python utilizando la nueva librería `google-genai` de Streamlit que capture cualquier error en la llamada a la IA (como saturación 503 o límites de cuota 429). Haz que active instantáneamente un sistema de respaldo local (*fallback*) con tres destinos predeterminados desde Barcelona (Sitges, Montserrat y Vic), mostrando un aviso amigable mediante `st.toast` para evitar que la interfaz de Streamlit se quede bloqueada."*

---

## 4. Fase de Optimización de Interfaces (UI / UX)
*Prompt para refinar la interacción con el usuario mediante formularios nativos y contenedores limpios.*

> **Prompt:**
> *"Modifica el código de Streamlit para que los selectores de preferencias del usuario estén organizados dentro de un formulario (`st.form`) con un botón de envío claro. Asegúrate de que los resultados devueltos por la IA se muestren en tarjetas independientes utilizando `st.container(border=True)` con iconos descriptivos para que la lectura sea limpia y accesible para usuarios sin perfil técnico."*
