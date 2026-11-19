# CODIGO 2 - VERSAO 2 - BEM MAIS BONITA

from PIL import Image, ImageDraw, ImageFont
import math

img = Image.new("RGB", (1240, 1754), "white")
draw = ImageDraw.Draw(img)

try:
    titulo = ImageFont.truetype("arial.ttf", 70)
    texto = ImageFont.truetype("arial.ttf", 45)
    gigante = ImageFont.truetype("arial.ttf", 400)
except:
    titulo = ImageFont.load_default()
    texto = ImageFont.load_default()
    gigante = ImageFont.load_default()

# Titulo no meio
draw.text((300, 40), "Coordenacao Motora C", fill="black", font=titulo)

# --- CAPIVARA - INICIO ---
# cabeca
draw.ellipse([120, 250, 450, 550], outline="black", width=5)
# orelhas
draw.ellipse([160, 220, 230, 290], outline="black", width=4)
draw.ellipse([340, 220, 410, 290], outline="black", width=4)
# olhos
draw.ellipse([210, 350, 250, 390], fill="black")
draw.ellipse([330, 350, 370, 390], fill="black")
# focinho
draw.ellipse([240, 430, 340, 490], outline="black", width=3)
draw.text((180, 580), "INICIO - Capivara", fill="black", font=texto)

# --- CAMINHO PONTILHADO ---
# Agora vai do lado da capivara até a letra C
for i in range(80):
    x = 500 + i * 8
    y = 400 + math.sin(i/6)*80
    draw.ellipse([x, y, x+12, y+12], fill="black")

# --- LETRA C GIGANTE - CHEGADA ---
draw.text((350, 850), "CHEGADA", fill="black", font=texto)
draw.text((400, 950), "C", fill="black", font=gigante)

# --- TREINO ---
draw.text((180, 1550), "Treine: C  C  C  C  C", fill="black", font=texto)

img.save("pagina_C_final.png")
print("Versao 2 prontinha!")