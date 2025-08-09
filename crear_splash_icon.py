from PIL import Image

# Abrir el icono original
icon = Image.open('android/app/src/main/res/drawable/nuevo_icono.png').convert('RGBA')

# Crear fondo negro cuadrado
size = 1024
background = Image.new('RGBA', (size, size), (0, 0, 0, 255))

# Calcular posición para centrar el icono
icon.thumbnail((size, size), Image.LANCZOS)
icon_w, icon_h = icon.size
pos = ((size - icon_w) // 2, (size - icon_h) // 2)

# Pegar el icono sobre el fondo
background.paste(icon, pos, icon)

# Convertir a RGB (sin transparencia)
background = background.convert('RGB')

# Guardar el resultado
background.save('android/app/src/main/res/drawable/splash_icon.png')
print('¡Splash icon generado correctamente!')
