import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
from IPython.display import display

class InteractiveYinYang:
    def __init__(self, small_circle_ratio=0.125, angle=0, color1='black', color2='white', bg_color='white'):
        self.small_circle_ratio = small_circle_ratio
        self.angle = angle
        self.color1 = color1
        self.color2 = color2
        self.bg_color = bg_color
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self.ax.axis('off')
        self.draw_yin_yang()
    
    def rotate(self, x, y):
        theta = np.radians(self.angle)
        x_new = x * np.cos(theta) - y * np.sin(theta)
        y_new = x * np.sin(theta) + y * np.cos(theta)
        return x_new, y_new
    
    def draw_yin_yang(self):
        self.ax.clear()
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-1.1, 1.1)
        self.ax.set_ylim(-1.1, 1.1)
        self.ax.axis('off')
        self.fig.patch.set_facecolor(self.bg_color)
        
        main_circle = plt.Circle((0, 0), 1, color=self.color1, fill=True)
        self.ax.add_patch(main_circle)
        
        x1, y1 = self.rotate(0, 0.5)
        half_circle_white = plt.Circle((x1, y1), 0.5, color=self.color2, fill=True)
        self.ax.add_patch(half_circle_white)
        
        x2, y2 = self.rotate(0, -0.5)
        half_circle_black = plt.Circle((x2, y2), 0.5, color=self.color1, fill=True)
        self.ax.add_patch(half_circle_black)
        
        x3, y3 = self.rotate(0, -0.5)
        small_white_circle = plt.Circle((x3, y3), self.small_circle_ratio, color=self.color2, fill=True)
        self.ax.add_patch(small_white_circle)
        
        x4, y4 = self.rotate(0, 0.5)
        small_black_circle = plt.Circle((x4, y4), self.small_circle_ratio, color=self.color1, fill=True)
        self.ax.add_patch(small_black_circle)
        
        self.fig.canvas.draw()
    
    def update(self, small_circle_ratio, angle, color1, color2, bg_color):
        self.small_circle_ratio = small_circle_ratio
        self.angle = angle
        self.color1 = color1
        self.color2 = color2
        self.bg_color = bg_color
        self.draw_yin_yang()

    def interactive_controls(self):
        small_circle_slider = widgets.FloatSlider(value=self.small_circle_ratio, min=0.05, max=0.2, step=0.005, description='Kis kör méret')
        angle_slider = widgets.FloatSlider(value=self.angle, min=0, max=360, step=1, description='Elforgatás')
        
        color1_picker = widgets.ColorPicker(value=self.color1, description='Szín 1')
        color2_picker = widgets.ColorPicker(value=self.color2, description='Szín 2')
        bg_color_picker = widgets.ColorPicker(value=self.bg_color, description='Háttérszín')
        
        ui = widgets.VBox([small_circle_slider, angle_slider, color1_picker, color2_picker, bg_color_picker])
        widgets.interactive(self.update, small_circle_ratio=small_circle_slider, angle=angle_slider, color1=color1_picker, color2=color2_picker, bg_color=bg_color_picker)
        display(ui)
        
# Példányosítás
yin_yang = InteractiveYinYang()
yin_yang.interactive_controls()