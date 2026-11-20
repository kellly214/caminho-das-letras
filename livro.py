from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGB", (1240, 1754), "white")
draw = ImageDraw.Draw(img)

# tenta usar fonte grande, se não tiver usa padrão
try:
    font_titulo = ImageFont.truetype("arial.ttf", 60)
    font_texto = ImageFont.truetype("arial.ttf", 40)
except:
    font_titulo = ImageFont.load_default()
    font_texto = ImageFont.load_default()

# Titulo
draw.text((300, 30), "Coordenacao Motora C", fill="black", font=font_titulo)

# Capivara - INICIO
draw.ellipse([100, 300, 400, 500], outline="black", width=8)
draw.text((150, 380), "INICIO", fill="black", font=font_texto)
draw.text((120, 430), "Capivara", fill="black", font=font_texto)

# Caminho 1
draw.rectangle([450, 350, 900, 500], outline="black", width=6)

# Caminho 2
draw.rectangle([250, 800, 1000, 1100], outline="black", width=6)

# Chegada - Letra C
draw.text((700, 1400), "CHEGADA", fill="black", font=font_titulo)
draw.text((750, 1480), "Letra C", fill="black", font=font_titulo)

# Treino embaixo
draw.text((200, 1600), "Treine: C C C C C", fill="black", font=font_texto)

img.save("pagina1_coord_C_LINDA.png")
print("Folha LINDA criada!")