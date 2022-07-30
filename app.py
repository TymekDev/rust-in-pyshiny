from shiny import App, render, ui

from pyshiny_rust_lib import hello_rust, calc_in_rust

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.output_text_verbatim("hello"),
    ui.output_text_verbatim("calc")
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

    @output
    @render.text
    def hello():
        return hello_rust()

    @output
    @render.text
    def calc():
        return f"n*2+2={calc_in_rust(input.n())}"


app = App(app_ui, server)
