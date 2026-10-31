
from google.adk.agents.llm_agent import Agent


def explicar_concepto(concepto: str) -> dict:
    """Busca y explica conceptos básicos de informática."""

    conceptos = {
        "api": "Una API permite la comunicación entre diferentes sistemas.",
        "algoritmo": "Un algoritmo es una secuencia ordenada de pasos para resolver un problema.",
        "base de datos": "Una base de datos almacena y organiza información para facilitar su consulta.",
        "python": "Python es un lenguaje de programación de alto nivel, conocido por su sintaxis sencilla.",
        "inteligencia artificial": "La inteligencia artificial permite que las máquinas realicen tareas que normalmente requieren inteligencia humana.",
        "machine learning": "Machine Learning es una rama de la inteligencia artificial que permite a los sistemas aprender a partir de datos.",
        "software": "El software es el conjunto de programas e instrucciones que permiten realizar tareas en una computadora.",
        "red informática": "Una red informática conecta dispositivos para compartir información y recursos."
    }

    if not isinstance(concepto, str) or not concepto.strip():
        return {
            "status": "error",
            "explicacion": "Debes ingresar un concepto válido."
        }

    concepto = concepto.lower().strip()

    if concepto in conceptos:
        return {
            "status": "success",
            "explicacion": conceptos[concepto]
        }

    return {
        "status": "not_found",
        "explicacion": "Concepto no registrado. Intenta con otro concepto."
    }


def calcular_promedio(numeros: list[float]) -> dict:
    """Calcula el promedio de una lista de números."""

    if not isinstance(numeros, list) or not numeros:
        return {
            "status": "error",
            "resultado": None,
            "mensaje": "Debes proporcionar una lista de números."
        }

    if any(
        isinstance(numero, bool)
        or not isinstance(numero, (int, float))
        for numero in numeros
    ):
        return {
            "status": "error",
            "resultado": None,
            "mensaje": "Todos los valores deben ser números."
        }

    promedio = sum(numeros) / len(numeros)

    return {
        "status": "success",
        "resultado": round(promedio, 2),
        "mensaje": "Promedio calculado correctamente."
    }


root_agent = Agent(
    model="gemini-3.5-flash-lite",
    name="agente_ucv",
    description="Agente académico UCV especializado en conceptos de informática.",
    instruction="""
    Eres un asistente académico de la Universidad César Vallejo.

    Tus funciones son:
    1. Explicar conceptos relacionados con informática y tecnología.
    2. Utilizar la herramienta explicar_concepto cuando el usuario
       pregunte por un concepto técnico registrado.
    3. Utilizar calcular_promedio cuando el usuario solicite
       calcular el promedio de varias notas o números.
    4. Responder siempre en español.
    5. Utilizar lenguaje sencillo y ejemplos prácticos.
    6. Si un concepto no está registrado, puedes explicar el
       significado general con tus conocimientos.
    7. No inventar resultados de cálculos.
    """,
    tools=[explicar_concepto, calcular_promedio]
)
