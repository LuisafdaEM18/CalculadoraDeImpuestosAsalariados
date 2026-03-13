# CalculadoraDeImpuestosAsalariados
Entrevista experto: https://drive.google.com/drive/folders/1g3MmJq6Oadjpt-1ZybUw4uBtIkHcx8Tm?usp=drive_link
Calculadora de Impuestos Colombia 2026 – Casos de Prueba

- Juan Pablo Arango Correa
- Jerónimo Roldán Cardona

¿Qué es y para qué es?

Esta aplicación calcula el impuesto de renta que debe pagar un trabajador asalariado en Colombia para el año gravable 2026, siguiendo las tarifas y reglas establecidas por la DIAN.
A partir de los ingresos del usuario y sus deducciones aplicables (seguridad social, dependientes, crédito hipotecario, entre otras), la calculadora determina la renta gravable en UVT y aplica la tabla de tarifas progresivas vigente para 2026.

¿Cómo lo hago funcionar?

Antes de ejecutar la aplicación, es necesario que se ejecuten las pruebas unitarias para asegurar que este funcione correctamente, además de que estas pruebas crean las tablas de base de datos necesarias para la aplicación.
También es recomendable instalar todas las dependencias necesarias para que la aplicación funcione correctamente. Esto lo puede hacer con el siguiente comando:
Comando para ejecutar: 

src/view/consola_calculadora.py

📥 Entradas
La función calcular_impuestos() recibe los siguientes parámetros:

ingresos_anuales (float) — Ingresos brutos totales del año en COP
deducciones (float) — Deducciones generales permitidas en COP
pension (float) — Aportes obligatorios a pensión del año en COP
salud (float) — Aportes obligatorios a salud del año en COP
dependientes (int) — Número de personas a cargo (máximo 4 aplican)
vivienda_propia (bool) — True si tiene crédito hipotecario activo, False si no
intereses_vivienda (float) — Intereses pagados en el año por crédito hipotecario en COP
⚙️ Proceso de Cálculo
El cálculo se realiza en tres etapas a través de funciones auxiliares:
Etapa 1 — renta_gravable(): Base gravable en pesos
Se parte de los ingresos brutos y se aplican los siguientes descuentos:
1. Renta exenta
El 25% de los ingresos está exento de impuesto por ley, con un tope máximo de 790 UVT (~$41.3M COP en 2026).
2. Seguridad social
Los aportes a pensión y salud se descuentan en su totalidad, sin ningún límite.
3. Deducciones especiales
Se acumulan las siguientes deducciones:

Deducciones generales ingresadas directamente
10% de los ingresos (máx. 384 UVT)
72 UVT por cada dependiente (máx. 4 dependientes = 288 UVT)
Intereses de crédito hipotecario (máx. 1.200 UVT, solo si vivienda_propia = True)
Etapa 2 — renta_gravable_uvt(): Conversión a UVT
La renta gravable en pesos se convierte a Unidades de Valor Tributario para poder ubicarla en la tabla de tarifas
 El valor de la UVT para 2026 es $52.374 COP, según resolución de la DIAN.
Etapa 3 — calcular_impuestos(): Tabla de tarifas progresivas
Con la renta en UVT se determina el tramo correspondiente y se calcula el impuesto. La tarifa es progresiva: solo la porción de renta que supera el límite inferior de cada tramo tributa a esa tarifa.

Hasta 1.090 UVT → 0% — no es contribuyente
De 1.090 a 1.700 UVT → 19%
De 1.700 a 4.100 UVT → 28%
De 4.100 a 8.670 UVT → 33%
De 8.670 a 18.970 UVT → 35%
De 18.970 a 31.000 UVT → 37%
Más de 31.000 UVT → 39%
📤 Salida
La función retorna un único valor:

impuesto (float) — Impuesto de renta a pagar en COP, redondeado al peso más cercano

❌ Validaciones y Manejo de Errores
Antes de realizar cualquier cálculo, la función valida que los datos sean coherentes. Si algún valor es inválido, se lanza una excepción ValueError con un mensaje descriptivo:

Ingresos negativos → "Los ingresos no pueden ser negativos"
Deducciones mayores a los ingresos → "Las deducciones no pueden superar los ingresos totales"
Dependientes negativos → "El número de dependientes debe ser mayor o igual a cero"
Aportes a pensión negativos → "Los aportes a pensión no pueden ser negativos"
Intereses de vivienda negativos → "Los intereses de vivienda no pueden ser negativos"
🧪 Casos de Prueba
Los casos de prueba están documentados en el archivo casos_prueba.xlsx e incluyen tres categorías:
Casos Normales — situaciones típicas de contribuyentes con diferentes perfiles:

Normal 1: $80M ingresos, $10M deducciones, 2 dependientes, con crédito hipotecario ($5M intereses)
Normal 2: $150M ingresos, $20M deducciones, 1 dependiente, sin vivienda propia
Normal 3: $200M ingresos, $15M deducciones, sin dependientes, con crédito hipotecario ($2M intereses)

Casos Extraordinarios — ingresos muy altos o muy bajos para verificar los límites del sistema:

Extraordinario 1: $600M ingresos, 4 dependientes, máximas deducciones aplicables
Extraordinario 2: $15M ingresos, sin deducciones (por debajo del umbral mínimo)
Extraordinario 3: $1.200M ingresos, sin ninguna deducción (caso límite máximo de tarifa)

Casos de Error — entradas inválidas para verificar que las validaciones funcionen correctamente:

Ingresos negativos, deducciones excesivas, dependientes negativos, aportes negativos e intereses negativos
 Constantes del Sistema

UVT 2026: $52.374 COP
Renta exenta: 25% de los ingresos, tope 790 UVT
Deducción por gastos: 10% de los ingresos, tope 384 UVT
Deducción por dependiente: 72 UVT por persona, máximo 4 (288 UVT)
Deducción por intereses de vivienda: máximo 1.200 UVT
Límite total de deducciones especiales: 40% de ingresos o 1.340 UVT (el menor)
Seguridad social: sin límite de deducción
