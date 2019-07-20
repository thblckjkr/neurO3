# Import and initialize UI
from ux import ui
import math

u = ui()

u.show("Importando clases")
# import loader & recognizer
from recognition import recognition
from loader import loader

## Initialize the recognizer and give him some interface
r = recognition(u)
l = loader()
u.show("Clases importadas e inicializadas", "success")

# Cargar datos del CSV
data = l.get()

# Establecer epocas
epochs = u.askNumber("Con cuantas epocas desea probar?", "warning")
if epochs <= 0 or epochs > 10000:
    u.show("La cantidad de epocas no es coherente, se han establecido 5000", "warning")
    epochs = 5000

middlesize = u.askNumber("Cuantas neuronas desea en la capa interior?", "warning")
if middlesize <= 0 or middlesize > 10000:
    u.show("La cantidad de epocas no es coherente, se han establecido 13", "warning")
    middlesize = 10

r.set(
    data['inputs'],
    data['targets'],
    # TODO: Automate things
    [[
        1,
        1
    ],
    [
        10,
        100
    ],
    [   15,
        15 * 15
    ],
    [   20,
        20 * 20
    ]], 
    epochs = epochs,
    middlesize = middlesize
)

cont = u.askYesNo("Deseas comenzar el analisis?")
if cont == 1:
    u.show("Comenzando analisis")
    r.analyze()
else:
    u.show("La operacion ha sido cancelada", "error")