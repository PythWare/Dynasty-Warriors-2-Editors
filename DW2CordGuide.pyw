import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# folder used for storing map files, map files must be kept there.
folder1 = "maps"

class ImageMarkerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DW2 Coordinate Guide")

        self.original_width = 800
        self.original_height = 800

        # Create a canvas to display the image
        self.canvas = tk.Canvas(root, width=self.original_width, height=self.original_height)
        self.canvas.pack()

        # Entry widgets for x and y coordinates
        vcmd = (self.root.register(self.validate_int), '%S', '%P')
        
        self.x_entry = tk.Entry(root, width=10, validate='key', validatecommand=vcmd)
        self.x_entry.pack(side=tk.LEFT, padx=5)
        
        self.y_entry = tk.Entry(root, width=10, validate='key', validatecommand=vcmd)
        self.y_entry.pack(side=tk.LEFT, padx=5)

        # Button to mark the image
        self.mark_button = tk.Button(root, text="Mark", command=self.mark_image)
        self.mark_button.pack(pady=5)

        # Combobox for selecting images
        self.image_selector = ttk.Combobox(root, values=["YellowTurban.png", "HuLaoGate.png", "GuanDu.png", "ChangBan.png", "ChiBi.png",
                                                         "HeFei.png", "YiLing1.png", "YiLing2.png", "WuZhangPlains.png"], state="readonly")
        self.image_selector.current(0)  # Select the first image by default
        self.image_selector.pack(pady=5)
        self.image_selector.bind("<<ComboboxSelected>>", self.update_image)

        # Button to clear markers on the image
        self.clear_button = tk.Button(root, text="Clear Markers", command=self.clear_markers)
        self.clear_button.pack(pady=5)

        # Initialize variables
        self.image = None
        self.markers = []

        # Bind mouse click to mark image
        self.canvas.bind("<Button-1>", self.mark_image_with_click)

    def validate_int(self, new_value, current_value):
        # Validate if the input value is an integer
        if new_value.isdigit() or new_value == "":
            return True
        else:
            return False

    def load_image(self, image_path):
        # Clear previous image and markers
        self.canvas.delete("all")
        self.markers = []

        # Load image using tkinter's PhotoImage
        self.image = tk.PhotoImage(file=os.path.join(folder1,image_path))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    # Used to update the image being displayed based on the selected file
    def update_image(self, event=None):
        selected_image = self.image_selector.get()
        self.load_image(selected_image)

    # used for marking positions on the map
    def mark_image(self):
        # Get x and y coordinates from entry widgets
        try:
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
            
            # Validate x and y coordinates within the range 0 to 800
            if 0 <= x <= 800 and 0 <= y <= 800:
                # Adjust y-coordinate to match upward-increasing coordinate system
                adjusted_y = self.original_height - y
                
                # Draw a red dot at the specified coordinates
                marker = self.canvas.create_oval(x-5, adjusted_y-5, x+5, adjusted_y+5, outline="red", width=3)
                self.markers.append(marker)
            else:
                # Display an error message or handle out-of-range coordinates
                messagebox.showerror("Error", "Coordinates must be within the range 0 to 800.")
        except ValueError:
            # Handle cases where x or y is not a valid integer
            messagebox.showerror("Error", "Invalid input. Please enter valid integer coordinates.")

    # used for marking the image based on where the user clicks
    def mark_image_with_click(self, event):
        # Get coordinates of mouse click
        x = event.x
        y = event.y

        # Adjust y-coordinate to match upward-increasing coordinate system
        adjusted_y = self.original_height - y

        # Display current coordinates
        self.x_entry.delete(0, tk.END)
        self.x_entry.insert(0, str(x))
        self.y_entry.delete(0, tk.END)
        self.y_entry.insert(0, str(adjusted_y))

        # Draw a red dot at the clicked coordinates
        marker = self.canvas.create_oval(x-5, y-5, x+5, y+5, outline="red", width=3)
        self.markers.append(marker)
    # used to remove markers on the image
    def clear_markers(self):
        for marker in self.markers:
            self.canvas.delete(marker)
        self.markers = []

if __name__ == "__main__":
    os.makedirs(folder1, exist_ok= True)
    root = tk.Tk()
    app = ImageMarkerApp(root)
    root.mainloop()
