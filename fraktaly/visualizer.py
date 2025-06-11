import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.patches import Rectangle
from .mandelbrot import compute_mandelbrot_set
from .julia import compute_julia_set

def run_visualizer() -> None:
    """Runs an interactive visualization of Mandelbrot and Julia fractals."""
    width, height = 800, 800
    max_iter_default = 100
    c_re, c_im = -0.4, 0.6
    julia_mode = [False]
    default_window = [[-2.0, 1.5], [-1.5, 1.5]]
    window = [default_window[0][:], default_window[1][:]]

    fig, ax = plt.subplots(figsize=(6, 6))
    plt.subplots_adjust(left=0.3, bottom=0.35)

    selection_rect = [None]
    press = [None]

    def draw() -> None:
        """Renders the fractal based on current view and settings."""
        ax.clear()
        xmin, xmax = window[0]
        ymin, ymax = window[1]
        iterace = int(slider_iter.val)
        if julia_mode[0]:
            c = complex(slider_re.val, slider_im.val)
            data = compute_julia_set(c, xmin, xmax, ymin, ymax, width, height, iterace)
            ax.set_title("Julia")
        else:
            data = compute_mandelbrot_set(xmin, xmax, ymin, ymax, width, height, iterace)
            ax.set_title("Mandelbrot")
        ax.imshow(data, extent=(xmin, xmax, ymin, ymax), cmap="hot", origin="lower", aspect='auto')
        plt.draw()

    def on_press(event):
        """Handles mouse press to start zoom selection."""
        if event.inaxes != ax:
            return
        press[0] = (event.xdata, event.ydata)
        selection_rect[0] = Rectangle((event.xdata, event.ydata), 0, 0,
                                      linewidth=1, edgecolor='white', facecolor='none')
        ax.add_patch(selection_rect[0])
        plt.draw()

    def on_motion(event):
        """Handles mouse motion to adjust zoom rectangle."""
        if press[0] is None or selection_rect[0] is None or event.inaxes != ax:
            return
        x0, y0 = press[0]
        x1, y1 = event.xdata, event.ydata
        selection_rect[0].set_width(x1 - x0)
        selection_rect[0].set_height(y1 - y0)
        plt.draw()

    def on_release(event):
        """Handles mouse release to finalize zoom."""
        if press[0] is None or event.inaxes != ax:
            return
        x0, y0 = press[0]
        x1, y1 = event.xdata, event.ydata
        press[0] = None
        if selection_rect[0] is not None:
            selection_rect[0].remove()
            selection_rect[0] = None
        if abs(x1 - x0) > 0.01 and abs(y1 - y0) > 0.01:
            window[0][0], window[0][1] = sorted([x0, x1])
            window[1][0], window[1][1] = sorted([y0, y1])
            draw()

    fig.canvas.mpl_connect("button_press_event", on_press)
    fig.canvas.mpl_connect("motion_notify_event", on_motion)
    fig.canvas.mpl_connect("button_release_event", on_release)

    ax_re = plt.axes([0.3, 0.25, 0.6, 0.03])
    ax_im = plt.axes([0.3, 0.2, 0.6, 0.03])
    ax_iter = plt.axes([0.3, 0.15, 0.6, 0.03])
    slider_re = Slider(ax_re, 'Re(c)', -1.0, 1.0, valinit=c_re)
    slider_im = Slider(ax_im, 'Im(c)', -1.0, 1.0, valinit=c_im)
    slider_iter = Slider(ax_iter, 'Iterace', 10, 300, valinit=max_iter_default, valstep=10)

    slider_re.on_changed(lambda val: draw())
    slider_im.on_changed(lambda val: draw())
    slider_iter.on_changed(lambda val: draw())

    ax_button = plt.axes([0.05, 0.5, 0.2, 0.05])
    button = Button(ax_button, 'Mandelbrot / Julia')
    button.label.set_fontsize(9)

    ax_reset = plt.axes([0.05, 0.43, 0.2, 0.05])
    reset_button = Button(ax_reset, 'Reset Zoom')
    reset_button.label.set_fontsize(9)

    fig._widgets = [button, reset_button]

    button.on_clicked(lambda event: (julia_mode.__setitem__(0, not julia_mode[0]), draw()))
    reset_button.on_clicked(lambda event: (window.__setitem__(0, default_window[0][:]),
                                           window.__setitem__(1, default_window[1][:]), draw()))
    draw()
    plt.show()