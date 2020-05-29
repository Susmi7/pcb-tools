import os
from gerber import *

from gerber.render import RenderSettings, theme
from gerber.render.cairo_backend import GerberCairoContext


GERBER_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'not-working'))


# Create a new drawing context
ctx = GerberCairoContext()

# Create a new PCB instance
pcb = PCB.from_directory(GERBER_FOLDER)



# Render PCB bottom view
ctx.render_layers(pcb.bottom_layers,
                  os.path.join(os.path.dirname(__file__), 'not-working-bottom.png'), max_width=800, max_height=600)
ctx.render_layers(pcb.top_layers,
                  os.path.join(os.path.dirname(__file__), 'not-working-top.png'),max_width=800, max_height=600)

