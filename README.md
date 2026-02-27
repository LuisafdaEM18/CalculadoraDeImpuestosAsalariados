# CalculadoraDeImpuestosAsalariados
Entrevista experto: https://drive.google.com/drive/folders/1g3MmJq6Oadjpt-1ZybUw4uBtIkHcx8Tm?usp=drive_link
Calculadora de Impuestos Colombia 2026 – Casos de Prueba

- Juan Pablo Arango Correa
- Jerónimo Roldán Cardona

📥 ENTRADAS

Las siguientes columnas corresponden a los datos que el usuario debe ingresar en la calculadora:

Campo	Descripción	Tipo de Dato
Ingresos Anuales (COP)	Total de ingresos brutos percibidos en el año	Numérico (mayor o igual a 0)
Deducciones (COP)	Valor total de deducciones aplicables	Numérico (≥ 0 y ≤ ingresos)
Aportes Pensión (COP)	Total anual aportado a pensión	Numérico (≥ 0)
Aportes Salud (COP)	Total anual aportado a salud	Numérico (≥ 0)
Dependientes	Número de personas dependientes económicamente	Entero (≥ 0)
Vivienda Propia (1=Sí, 0=No)	Indica si el contribuyente tiene vivienda propia	Entero (1 o 0)
⚙️ PROCESO

La lógica general aplicada por la calculadora es la siguiente:

1️⃣ Validaciones Iniciales

Antes de realizar el cálculo:

Los ingresos no pueden ser negativos.

Las deducciones no pueden superar los ingresos.

Los dependientes no pueden ser negativos.

Los campos obligatorios no pueden estar vacíos.

Los valores deben ser numéricos cuando corresponda.

Si alguna validación falla → el sistema retorna ERROR con mensaje descriptivo.

2️⃣ Cálculo de la Renta Líquida Gravable

Se calcula restando de los ingresos:

Deducciones

Aportes a pensión

Aportes a salud

Beneficios adicionales (dependientes y vivienda, si aplican)

Fórmula general conceptual:

Renta Líquida Gravable =
Ingresos
- Deducciones
- Aportes Pensión
- Aportes Salud
- Beneficios aplicables
3️⃣ Cálculo del Impuesto a Pagar

Una vez obtenida la renta líquida gravable:

Se aplica la tabla o tarifa correspondiente.

Se calcula el valor final del impuesto.

Se obtiene la tasa efectiva.

4️⃣ Cálculo de la Tasa Efectiva
Tasa Efectiva (%) = (Impuesto a Pagar / Ingresos Anuales) * 100

Este valor permite analizar el porcentaje real que el contribuyente paga respecto a sus ingresos.

📤 SALIDAS

El archivo genera las siguientes columnas de resultado:

Campo	Descripción
Renta Líquida Gravable	Base final sobre la cual se calcula el impuesto
Impuesto a Pagar (COP)	Valor final del impuesto calculado
Tasa Efectiva (%)	Porcentaje efectivo pagado sobre los ingresos
Resultado Completo	Resumen textual del caso con entradas y resultado

En casos de error:

La columna de renta líquida muestra ERROR

Se incluye un mensaje descriptivo indicando la causa

🧪 TIPOS DE CASOS INCLUIDOS

✅ 1. Casos Normales

Escenarios típicos de contribuyentes promedio.

Ejemplo:

Caso Normal 1

Caso Normal 2

📈 2. Casos Extraordinarios

Escenarios extremos o especiales:

Alto Ejecutivo (ingresos elevados)

Salario Mínimo (ingresos bajos)

❌ 3. Casos de Error

Pruebas de validación del sistema:

Ingresos negativos

Deducciones excesivas

Dependientes negativos

Campo vacío

Tipo de dato incorrecto
