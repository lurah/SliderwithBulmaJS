from fasthtml.common import *

hdrs=(Link(rel='icon', type='image/png', href='static/school-bus.png'),
      Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css',
      type='text/css'),
      Link(rel='stylesheet', href='static/styles.css', type='text/css'),
      Script(src='static/slider.js'))


app = FastHTML(pico=False, hdrs=hdrs)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def baru():
    return Title("Bulma CSS"), \
           Section(Div(H1("Hello World",cls="title"),
                       P("My first website with ",Strong("Bulma!", cls="has-text-primary"),cls="subtitle"),
                       cls="container has-text-centered mb-4"),
                   Section(Span("0", cls="has-text-success"),
                           Input(type="range",min="0",max="255",id="slider", cls="custom-range"),
                           Span("255", id="maks", cls="has-text-success"),
                           cls="container has-text-centered"),
                   cls="section")

serve()