import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def rgb888_to_rgb565(r, g, b):
    """Convert 24-bit RGB to 16-bit RGB565."""
    return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)

def convert_image():
    # Ask for input PNG
    input_path = filedialog.askopenfilename(
        title="Select PNG file",
        filetypes=[("PNG files", "*.png")]
    )
    if not input_path:
        return  # user canceled

    try:
        img = Image.open(input_path).convert("RGBA")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open image:\n{e}")
        return

    width, height = img.size
    pixels = list(img.getdata())

    # Convert pixels to RGB565
    rgb565_data = []
    for r, g, b, a in pixels:
        rgb565_data.append(0x0000 if a == 0 else rgb888_to_rgb565(r, g, b))

    # Output filename in same folder
    default_name = os.path.splitext(os.path.basename(input_path))[0] + ".h"
    output_path = filedialog.asksaveasfilename(
        title="Save C Header As",
        initialdir=os.path.dirname(input_path),
        initialfile=default_name,
        defaultextension=".h",
        filetypes=[("C Header", "*.h")]
    )
    if not output_path:
        return  # user canceled

    # Write C header
    try:
        with open(output_path, "w") as f:
            f.write(f"// Image: {os.path.basename(input_path)}\n")
            f.write(f"// Size: {width}x{height}\n\n")
            f.write(f"const uint16_t image[{width * height}] = {{\n")

            for i, val in enumerate(rgb565_data):
                f.write(f"0x{val:04X}, ")
                if (i + 1) % 12 == 0:
                    f.write("\n")

            f.write("\n};\n")

        messagebox.showinfo("Success", f"Saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file:\n{e}")

# --- GUI ---
root = tk.Tk()
root.title("PNG → RGB565 Converter")
root.geometry("300x100")
root.resizable(False, False)

btn = tk.Button(root, text="Convert PNG to RGB565", command=convert_image)
btn.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()
