# Especificación · [OutofBCN]

## 1. Problema y usuario

- **Quién tiene el problema:** [Una persona que vive en Barcelona o alrededores, tiene un fin de semana libre y quiere viajar, pero aún no ha elegido destino.]
- **Cómo lo resuelve hoy:** [Busca ideas de forma dispersa en redes sociales, blogs y buscadores de viajes, guardando muchas opciones y tratando de compararlas a mano.]
- **Qué le molesta de cómo lo hace hoy:** [Encuentra mucha inspiración, pero le cuesta reducir las opciones, perder tiempo comparando y decidirse por algo que encaje con su tiempo, presupuesto y el tipo de viaje que le apetece.]
- **Qué parte resuelve la IA:** [La IA selecciona y justifica 3 destinos personalizados según las preferencias del usuario; se queda fuera asegurar la disponibilidad de vuelos o indicar precios reales.]

## 2. Qué hace el producto

Máximo tres funcionalidades. Si hay más, van al apartado 8.

1. [Formulario interactivo de preferencias de viaje (duración, presupuesto, ambiente y medio de transporte desde Barcelona).]
2. [Generador de recomendaciones mediante IA que propone exactamente tres destinos con una breve explicación de por qué encajan.]
3. [Opción para generar nuevas alternativas o reajustar los parámetros de búsqueda con un solo clic.]

## 3. Entradas y salidas

| El usuario da… | La app devuelve… | Ejemplo |
|---|---|---|
| Selecciones en un formulario de preferencias (días, presupuesto, tipo de escapada y transporte desde Barcelona). | Tres propuestas de destinos estructuradas con título, motivo de la recomendación y un consejo breve. | Entrada: "3 días, presupuesto medio, naturaleza, en coche/tren". Salida: La Garrotxa, Priorat y Vall de Núria con su respectiva justificación. |

## 4. La pieza de IA

- **Opción elegida:** [API de un LLM (Gemini)]
- **Por qué:** [Permite razonar sobre preferencias cualitativas y generar sugerencias turísticas creativas y contextualizadas desde Barcelona de forma inmediata, sin necesidad de mantener una base de datos propia.]
- **Instrucciones para el modelo (system prompt):** [Eres un experto asesor de viajes enfocado en escapadas desde Barcelona. Tu objetivo es proponer exactamente tres destinos que se adapten a la duración, presupuesto, transporte y ambiente seleccionados por el usuario. Sé claro, directo y práctico. Para cada destino indica: nombre, por qué encaja y un consejo rápido. No inventes disponibilidad de vuelos ni precios exactos.]

## 5. Flujo del usuario

1. [El usuario entra a la app y ve el título "OutofBCN" junto con un formulario sencillo de preferencias de viaje.]
2. [Selecciona sus parámetros de escapada (días, presupuesto, ambiente y medio de transporte) y pulsa en buscar.]
3. [Recibe en pantalla tres tarjetas con los destinos recomendados y una explicación personalizada de cada uno.]

## 6. Restricciones

- Coste cero: capa gratuita de la API y despliegue gratuito (ruta A o B).
- La clave de la API va en secretos, nunca en el código.
- Sin datos personales reales.
- Lenguaje sencillo, para alguien sin conocimientos técnicos.
- Todos los destinos propuestos deben ser alcanzables de forma realista desde Barcelona según el transporte indicado.

## 7. Criterios de aceptación

La app está bien si:

| Entrada | Resultado esperado |
|---|---|
| [caso normal: Formulario completado con preferencias normales.] | [qué debe pasar: La app muestra tres propuestas de destino coherentes y bien argumentadas.] |
| [caso límite: Criterios contradictorios o extremos (ej. presupuesto muy bajo y viaje largo).] | [qué debe pasar: La app ofrece opciones realistas explicando amablemente cómo se adaptan a las limitaciones introducidas.] |
| [error: se acaba la cuota] | [mensaje claro para el usuario: La app muestra un mensaje claro y amigable al usuario indicando que el servicio no está disponible temporalmente.] |

## 8. Fuera de alcance (por ahora)

- [Integración con buscadores de vuelos, trenes u hoteles en tiempo real (como Skyscanner o Booking).]
- [Compra de billetes o reserva directa de alojamientos.]
- [Registro de usuarios o guardado de historiales de viaje.]

## 9. Despliegue

- Ruta: Streamlit Community Cloud.
- Proyecto individual (sin equipo).
