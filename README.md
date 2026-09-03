# IoT orientado a Visión Artificial (AIoT / Edge Vision)

**Programa:** Ingeniería de Sistemas — Universidad de La Guajira
**Docente:** Eduardo Luis Sierra Fragozo ([elsierra@uniguajira.edu.co](mailto:elsierra@uniguajira.edu.co))

Electiva de IoT orientada a Visión Artificial aplicada a IoT (AIoT / Edge
Vision): mismo pipeline de IoT — sensor → procesamiento → red → acción —
pero con la cámara como sensor principal y un modelo de visión artificial en
la capa de procesamiento. Enfoque práctico, sin diseño de circuitos.
Material independiente de periodo académico.

## Contenido del repositorio

- `index.html` — índice del curso: lista todo el material publicado para
  que los estudiantes lo encuentren desde un solo enlace.
- `plan-de-aula.html` — presentación de la asignatura (portada, presentación
  del curso, temario, Unidad 01 · Fundamentos de IoT — Arquitectura, y
  evaluación corte a corte: Corte 1, 2 y 3).
- `VisionClase1_ImagenDigital.html` — Unidad 02 · Clase 1: qué es una
  imagen digital (matriz de píxeles, muestreo y cuantización, RGB/RGBA,
  cómo la pantalla recrea el color).
- `VisionClase2_Convolucion.html` — Unidad 02 · Clase 2: qué es una
  convolución y cómo un kernel transforma una imagen; filtros de suavizado
  (promedio, gaussiano, mediana) y de bordes (Sobel, Laplaciano, Canny),
  con ejemplos en OpenCV.
- `IoTClase14_EticaDelDato.html` — Unidad 04 · Clase 14: ética del dato
  (finalidad, minimización, consentimiento, retención), seguridad frente a
  privacidad y el costo energético y material de un despliegue IoT.
- `IoTClase15_EnfoqueSTEAM.html` — Unidad 04 · Clase 15: enfoque STEAM
  aplicado al proyecto integrador, dimensión educativa y comunitaria, y
  revisión entre pares.
- `IoTClase16_Sustentacion.html` — Unidad 04 · Clase 16: sustentación del
  proyecto integrador, verificación técnica previa, guion de la presentación
  e informe final del Corte 3.
- `assets/img/` — imágenes de las clases. `assets/gen_clase2.py` regenera
  las de la Clase 2 a partir de `assets/img/escena.png` (requiere
  `opencv-python` y `numpy`).

Las clases 14 y 15 caen en el periodo de movilidad académica del docente
(12 al 22 de noviembre): son clases grabadas, con tutoría sincrónica el
miércoles y foro de dudas con respuesta dentro de las 24 horas. Cada deck lo
declara en su segunda diapositiva.

## Plan de evaluación

Igual que en Desarrollo de Videojuegos: el proyecto crece corte a corte
siguiendo el pipeline AIoT (sensor → procesamiento → red → acción). Stack
de referencia: Python + OpenCV, sin diseño de circuitos.

| Corte | Peso | Entrega principal | Entrega secundaria |
|---|---|---|---|
| 1 | 30% | Sustentación: pipeline básico — webcam + OpenCV + modelo preentrenado que clasifica/detecta y muestra el resultado (20%) | Exposición grupal de un caso real de AIoT/Edge Vision (10%) |
| 2 | 35% | Entrega completa: transmisión del resultado (no video crudo) + acción visible (20%) | Preentrega obligatoria: diagrama de arquitectura + prototipo de envío (15%) |
| 3 | 35% | Contribución en la sala: sustentación final del proyecto (25%) | Entrega final documentada — README, capturas o video (10%) |

## Cómo abrir el material

Publicado en <https://eduardosierraf.github.io/iot-vision-artificial/>. En
local, abre `index.html` en el navegador y desde ahí entra a cualquier
clase. No requiere build ni dependencias — es HTML/CSS/JS plano.

Al agregar una clase nueva, súmala también al listado de `index.html`; es
la única página por la que los estudiantes llegan al resto.

Navegación por teclado: flechas / `Page Up` / `Page Down` / `Space` para
avanzar, `Home` / `End` para ir al inicio o al final.
