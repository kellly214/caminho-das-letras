from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 1600
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def fonte(tamanho, negrito=False):
    try:
        if negrito:
            return ImageFont.truetype("arialbd.ttf", tamanho)
        return ImageFont.truetype("arial.ttf", tamanho)
    except:
        return ImageFont.load_default()

# Moldura
d.rectangle([25, 25, W-25, H-25], outline="black", width=7)

# Titulo
d.text((W//2, 105), "Caminho das Letras", font=fonte(72, True), fill="black", anchor="mm")
d.text((W//2, 190), "Um livro para colorir", font=fonte(36), fill="black", anchor="mm")
d.line([200, 240, 1000, 240], fill="black", width=3)

# Sol sorrindo - canto superior direito
cx, cy = 1080, 180
d.ellipse([cx-55, cy-55, cx+55, cy+55], outline="black", width=4)
for ang in range(0, 360, 30):
    x1 = cx + int(75 * math.cos(math.radians(ang)))
    y1 = cy + int(75 * math.sin(math.radians(ang)))
    x2 = cx + int(100 * math.cos(math.radians(ang)))
    y2 = cy + int(100 * math.sin(math.radians(ang)))
    d.line([x1, y1, x2, y2], fill="black", width=3)
d.ellipse([cx-25, cy-10, cx-15, cy], fill="black")
d.ellipse([cx+15, cy-10, cx+25, cy], fill="black")
d.arc([cx-25, cy+5, cx+25, cy+30], 0, 180, fill="black", width=3)

# Nuvem esquerda
d.ellipse([90, 300, 220, 380], outline="black", width=3)
d.ellipse([180, 270, 310, 350], outline="black", width=3)
d.ellipse([260, 300, 380, 380], outline="black", width=3)
d.ellipse([140, 320, 320, 390], outline="black", width=3)

# LETRA A grande - esquerda
d.text((110, 430), "A", font=fonte(150, True), fill="black")

# ARARA - direita, bem visivel
# corpo
d.ellipse([830, 400, 1030, 650], outline="black", width=5)
# cabeca
d.ellipse([860, 360, 990, 490], outline="black", width=5)
# bico
d.polygon([(990, 420), (1045, 445), (990, 475)], outline="black", width=4)
# olho
d.ellipse([910, 410, 935, 435], fill="black")
d.ellipse([918, 415, 925, 422], fill="white")
# asa
d.ellipse([850, 500, 990, 620], outline="black", width=3)
d.line([870, 540, 970, 540], fill="black", width=2)
d.line([870, 570, 970, 570], fill="black", width=2)
# rabo comprido
d.polygon([(850, 620), (780, 750), (820, 750), (880, 640)], outline="black", width=3)
# galho
d.line([750, 770, 1050, 770], fill="black", width=5)
d.line([900, 770, 900, 810], fill="black", width=3)

# CAPIVARA GRANDONA - centro
# corpo
d.ellipse([300, 750, 900, 1150], outline="black", width=6)
# cabeca
d.ellipse([430, 580, 770, 850], outline="black", width=6)
# orelhas
d.ellipse([450, 560, 510, 620], outline="black", width=4)
d.ellipse([690, 560, 750, 620], outline="black", width=4)
# olhos
d.ellipse([520, 680, 550, 710], fill="black")
d.ellipse([650, 680, 680, 710], fill="black")
# focinho
d.ellipse([550, 760, 650, 830], outline="black", width=4)
d.line([600, 830, 600, 855], fill="black", width=3)
d.arc([560, 850, 640, 890], 0, 180, fill="black", width=3)
# patinhas
d.rectangle([380, 1130, 450, 1220], outline="black", width=4)
d.rectangle([750, 1130, 820, 1220], outline="black", width=4)

# LETRA B - esquerda embaixo
d.text((110, 900), "B", font=fonte(150, True), fill="black")
# LETRA C - direita embaixo
d.text((1030, 900), "C", font=fonte(150, True), fill="black")

# TARTARUGA - embaixo no centro, entre B e C
# casco
d.ellipse([380, 1280, 820, 1450], outline="black", width=5)
d.ellipse([500, 1310, 700, 1420], outline="black", width=3)
d.line([600, 1310, 600, 1420], fill="black", width=2)
d.line([500, 1365, 700, 1365], fill="black", width=2)
# cabeca
d.ellipse([810, 1330, 900, 1400], outline="black", width=4)
d.ellipse([860, 1355, 872, 1367], fill="black")
# patinhas
d.rectangle([450, 1440, 500, 1480], outline="black", width=3)
d.rectangle([650, 1440, 700, 1480], outline="black", width=3)

# Chão
d.line([60, 1520, W-60, 1520], fill="black", width=3)
d.text((W//2, 1560), "Capivara  •  Arara  •  Tartaruga", font=fonte(28), fill="black", anchor="mm")

img.save("capa_caminho_das_letras.png")
print("Capa nova prontinha!")