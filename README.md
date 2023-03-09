# SDR-Proyect
Sistema de captura de señales FM y reconocimiento de voz para la asistencia de personas con problemas auditivos

1. Captura de una señal de FM por medio del uso de la tarjeta LimeSDR y GNU Radio.
2. Demodulación y generación de la señal de audio de un programa de radio.
3. Implementación de un sistema de reconocimiento de voz para detectar al hablante del programa de radio.
4. Presentación de la conversación en tiempo real en una interfaz gráfica.

**Sistema:**
1. Interfaz gráfica con la posibilidad de seleccionar la estación a recibir (GNU Radio).
2. Interfaz gráfica con la conversación en tiempo real.

**Stack de Software:**

  Backend:
    1. GNU Radio y Python
    2. Python + wav2vec2 + Transformers
  
  Fronted:
    1. Python + Flask + HTML + CSS + JS
