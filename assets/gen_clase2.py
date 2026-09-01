"""
Genera las imágenes de la Clase 2 (Convolución y filtros) a partir de la
misma escena sintética de la Clase 1. Todas las salidas son 480x300, mismo
tamaño y estilo que el resto de la unidad.

Uso:  python3 assets/gen_clase2.py
"""
import os
import cv2
import numpy as np

HERE = os.path.dirname(__file__)
IMG = os.path.join(HERE, "img")
SRC = os.path.join(IMG, "escena.png")


def save(name, mat):
    path = os.path.join(IMG, name)
    cv2.imwrite(path, mat)
    print("  ->", name)


def to_bgr(gray):
    # Se guardan en 1 canal (PNG en escala de grises) para que pesen poco.
    return gray


def norm8(mat):
    """Lleva cualquier rango (incluye negativos) a 0..255 uint8 para poder verlo."""
    return cv2.normalize(mat, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)


def main():
    color = cv2.imread(SRC, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
    print("fuente:", SRC, color.shape)

    # ---- 0. Aritmética: suma, resta/diferencia, logaritmo, gamma -----------
    capa = np.full_like(gray, 80)  # "imagen B": una capa pareja, +80 en todo el cuadro
    save("c2-capa.png", capa)

    suma = cv2.add(gray, capa)  # satura donde la escena ya estaba clara (cielo, sol)
    save("c2-suma.png", suma)

    cuadro2 = gray.copy()
    cv2.rectangle(cuadro2, (150, 90), (280, 200), 255, thickness=-1)  # "algo" que entra al cuadro
    save("c2-cuadro2.png", cuadro2)

    diferencia = cv2.absdiff(gray, cuadro2)
    save("c2-diferencia.png", diferencia)

    c = 255 / np.log(1 + 255)
    log_img = np.uint8(c * np.log(1 + gray.astype(np.float64)))
    save("c2-log.png", log_img)

    gamma_claro = np.uint8(((gray / 255.0) ** 0.4) * 255)
    save("c2-gamma-claro.png", gamma_claro)

    gamma_oscuro = np.uint8(((gray / 255.0) ** 2.5) * 255)
    save("c2-gamma-oscuro.png", gamma_oscuro)

    # ---- 1. Ruido: motiva el suavizado --------------------------------------
    rng = np.random.default_rng(7)
    noise = rng.normal(0, 22, gray.shape)
    noisy = np.clip(gray.astype(np.float64) + noise, 0, 255).astype(np.uint8)
    # sal y pimienta encima
    sp = rng.random(gray.shape)
    noisy[sp < 0.02] = 0
    noisy[sp > 0.98] = 255
    save("c2-ruido.png", to_bgr(noisy))

    # ---- 2. Blur de promedio (box) vs gaussiano ----------------------------
    box = cv2.blur(noisy, (9, 9))
    save("c2-blur-box.png", to_bgr(box))

    gauss = cv2.GaussianBlur(noisy, (9, 9), 2.5)
    save("c2-blur-gauss.png", to_bgr(gauss))

    median = cv2.medianBlur(noisy, 5)
    save("c2-blur-median.png", to_bgr(median))

    # ---- 3. filter2D: realce (sharpen) -----------------------------------
    k_sharp = np.array([[0, -1, 0],
                        [-1, 5, -1],
                        [0, -1, 0]], dtype=np.float32)
    sharp = cv2.filter2D(gray, -1, k_sharp)
    save("c2-sharpen.png", to_bgr(sharp))

    # ---- 4. Sobel X / Y / magnitud -------------------------------------------
    g = cv2.GaussianBlur(gray, (3, 3), 0)
    sx = cv2.Sobel(g, cv2.CV_64F, 1, 0, ksize=3)
    sy = cv2.Sobel(g, cv2.CV_64F, 0, 1, ksize=3)
    save("c2-sobel-x.png", to_bgr(norm8(np.abs(sx))))
    save("c2-sobel-y.png", to_bgr(norm8(np.abs(sy))))

    mag = np.sqrt(sx ** 2 + sy ** 2)
    save("c2-gradiente.png", to_bgr(norm8(mag)))

    # ---- 5. Laplaciano -----------------------------------------------------
    lap = cv2.Laplacian(g, cv2.CV_64F, ksize=3)
    save("c2-laplaciano.png", to_bgr(norm8(np.abs(lap))))

    # Laplaciano aplicado directo sobre la imagen con ruido: lo amplifica todo.
    lap_noisy = cv2.Laplacian(noisy, cv2.CV_64F, ksize=3)
    save("c2-laplaciano-ruido.png", to_bgr(norm8(np.abs(lap_noisy))))

    # ---- 6. Canny ---------------------------------------------------------
    canny = cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 0), 80, 160)
    save("c2-canny.png", to_bgr(canny))

    # umbrales bajos y sin suavizar, sobre la imagen con ruido -> bordes falsos
    canny_low = cv2.Canny(noisy, 20, 50)
    save("c2-canny-bajo.png", to_bgr(canny_low))

    # umbrales altos -> solo sobreviven los bordes de mayor contraste
    canny_high = cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 0), 180, 300)
    save("c2-canny-alto.png", to_bgr(canny_high))

    # ---- 7. Pipeline: contornos sobre la imagen ---------------------------
    edges = cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 0), 80, 160)
    cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    draw = color.copy()
    cv2.drawContours(draw, cnts, -1, (29, 35, 214), 2)  # rojo de la marca (BGR)
    save("c2-contornos.png", draw)

    print("listo.")


if __name__ == "__main__":
    main()
