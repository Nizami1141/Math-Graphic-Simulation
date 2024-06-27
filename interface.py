import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
import re

def convert_symbols(expression):
    # Replace "^" with "np.power" for raising to a power
    expression = re.sub(r'(\d+|\w+)\s*\^\s*(\d+|\w+)', r'np.power(\1, \2)', expression)
    # Replace "~" with "np.sqrt" for square root
    expression = re.sub(r'~(\d+|\w+)', r'np.sqrt(\1)', expression)
    
    # Add trigonometric functions
    expression = re.sub(r'\b(sin|cos|tan|asin|acos|atan|sinh|cosh|tanh|asinh|acosh|atanh)\b', r'np.\1', expression)
    
    return expression

def simulate_2d():
    try:
        func_str = entry_2d.get()
        func_str = convert_symbols(func_str)
        func = lambda x: eval(func_str)
        
        x = np.linspace(0, 10, 100)
        y = func(x)
        
        fig, ax = plt.subplots()
        ax.plot(x, y, label=f'y = {func_str}')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('2D Function Simulation')
        ax.legend()
        ax.grid(True)
        
        canvas = FigureCanvasTkAgg(fig, master=frame_2d_plot)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
    except Exception as e:
        print(f"Error in 2D function: {e}")

def simulate_3d():
    try:
        func_str = entry_3d.get()
        func_str = convert_symbols(func_str)
        func = lambda x, y, z: eval(func_str)
        
        x = np.linspace(-5, 5, 30)
        y = np.linspace(-5, 5, 30)
        z = np.linspace(-5, 5, 30)
        x, y, z = np.meshgrid(x, y, z)
        w = func(x, y, z)
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x[:,:,0], y[:,:,0], w[:,:,0], cmap='viridis')
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Function Simulation')
        
        canvas = FigureCanvasTkAgg(fig, master=frame_3d_plot)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
    except Exception as e:
        print(f"Error in 3D function: {e}")

# Create the main window
window = Tk()
window.title("Math Function Simulation")
window.geometry("800x600")

# Create a notebook (tab control)
notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both")

# Create frames for 2D and 3D functions
tab_2d = Frame(notebook)
tab_3d = Frame(notebook)

notebook.add(tab_2d, text="2D Function")
notebook.add(tab_3d, text="3D Function")

# Create frames within the tabs for better organization
frame_2d_input = Frame(tab_2d)
frame_2d_input.pack(side=TOP, fill=X, padx=10, pady=10)

frame_2d_plot = Frame(tab_2d)
frame_2d_plot.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)

frame_3d_input = Frame(tab_3d)
frame_3d_input.pack(side=TOP, fill=X, padx=10, pady=10)

frame_3d_plot = Frame(tab_3d)
frame_3d_plot.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)

# Create Label and Entry for 2D function
label_2d = Label(frame_2d_input, text="f(x) =")
label_2d.pack(side=LEFT, padx=10)

entry_2d = Entry(frame_2d_input, width=30)
entry_2d.pack(side=LEFT, padx=10)

Button(frame_2d_input, text="Simulate", command=simulate_2d).pack(side=LEFT, padx=10)

# Create Label and Entry for 3D function
label_3d = Label(frame_3d_input, text="f(x, y, z) =")
label_3d.pack(side=LEFT, padx=10)

entry_3d = Entry(frame_3d_input, width=30)
entry_3d.pack(side=LEFT, padx=10)

Button(frame_3d_input, text="Simulate", command=simulate_3d).pack(side=LEFT, padx=10)

# Run the application
window.mainloop()
