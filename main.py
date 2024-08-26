from gradio import Interface

def greet(name):
    return "Hello " + name + "!"

io = Interface(fn=greet, inputs="text", outputs="text")
io.launch()
