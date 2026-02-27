# CalculadoraDeImpuestosAsalariados
Entrevista experto: https://drive.google.com/drive/folders/1g3MmJq6Oadjpt-1ZybUw4uBtIkHcx8Tm?usp=drive_link
Calculadora de Impuestos Colombia 2026 – Casos de Prueba

- Juan Pablo Arango Correa
- Jerónimo Roldán Cardona

📥 Entradas
La función recibe 7 parámetros:
ParámetroTipoDescripcióningresos_anualesfloatIngresos brutos totales del año en COPdeduccionesfloatDeducciones generales permitidas en COPpensionfloatAportes obligatorios a pensión del año en COPsaludfloatAportes obligatorios a salud del año en COPdependientesintNúmero de personas a cargo (máximo 4 aplican)vivienda_propiaboolTrue si tiene crédito hipotecario activo, False si nointereses_viviendafloatIntereses pagados en el año por crédito hipotecario en COP

⚙️ Proceso de Cálculo
El cálculo se divide en 3 etapas:
1. Calcular la Renta Gravable en pesos
Se parte de los ingresos y se hacen los siguientes descuentos en orden:
Renta exenta: 25% de los ingresos, con tope de 790 UVT (~$41.3M COP).
Seguridad social: Los aportes a pensión y salud se descuentan en su totalidad, sin límite.
Deducciones especiales: Se suman las siguientes deducciones y se aplican con un límite conjunto:
DeducciónTopeDeducciones generalesSin tope individual10% de los ingresosMáx. 384 UVT72 UVT por dependienteMáx. 4 dependientes (288 UVT)Intereses de viviendaMáx. 1.200 UVT (solo si vivienda_propia = True)

⚠️ El total de deducciones especiales no puede superar el 40% de los ingresos ni 1.340 UVT — se aplica el menor de los dos.

2. Convertir a UVT
Renta en UVT = Renta Gravable / 52.374
El valor de la UVT para 2026 es $52.374 COP.
3. Aplicar la tabla de tarifas progresivas
Renta Gravable (UVT)TarifaFórmula0 — 1.0900%$01.090 — 1.70019%(renta - 1.090) × 19% × UVT1.700 — 4.10028%(116 + (renta - 1.700) × 28%) × UVT4.100 — 8.67033%(788 + (renta - 4.100) × 33%) × UVT8.670 — 18.97035%(2.296 + (renta - 8.670) × 35%) × UVT18.970 — 31.00037%(5.901 + (renta - 18.970) × 37%) × UVT> 31.00039%(10.352 + (renta - 31.000) × 39%) × UVT
Solo la porción de renta que supera el límite inferior de cada tramo se grava a esa tarifa.

📤 Salida
La función retorna un único valor:
VariableTipoDescripciónimpuestofloatImpuesto de renta a pagar en COP, redondeado

Si la renta gravable es ≤ 1.090 UVT, el impuesto retornado es $0 (no es contribuyente).


❌ Validaciones
La función lanza ValueError con mensaje descriptivo si alguna entrada es inválida:
CasoMensajeingresos_anuales < 0"Los ingresos no pueden ser negativos"deducciones > ingresos_anuales"Las deducciones no pueden superar los ingresos totales"dependientes < 0"El número de dependientes debe ser mayor o igual a cero"pension < 0"Los aportes a pensión no pueden ser negativos"intereses_vivienda < 0"Los intereses de vivienda no pueden ser negativos"

📋 Casos de Prueba
Casos Normales
CasoIngresosDeduccionesPensiónSaludDep.ViviendaInteresesNormal 1$80.000.000$10.000.000$6.400.000$3.200.0002✅$5.000.000Normal 2$150.000.000$20.000.000$12.000.000$6.000.0001❌$0Normal 3$200.000.000$15.000.000$10.000.000$5.000.0000✅$2.000.000
Casos Extraordinarios
CasoIngresosDeduccionesPensiónSaludDep.ViviendaInteresesExtraordinario 1$600.000.000$60.000.000$48.000.000$24.000.0004✅$25.000.000Extraordinario 2$15.000.000$0$1.200.000$600.0000❌$0Extraordinario 3$1.200.000.000$0$0$00❌$0
