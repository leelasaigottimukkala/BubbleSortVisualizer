from tkinter import *
import time

# Tk window
root = Tk()
root.title("Bubble Sort Visualizer")
root.geometry("600x420")

# Canvas for bars
canvas = Canvas(root, width=560, height=300, bg="white")
canvas.pack(pady=10)

# draw function — uses root.update() to force repaint
def draw_bars(data, colorArray):
    canvas.delete("all")
    c_height = 300
    c_width = 560
    margin = 20
    bar_width = (c_width - 2 * margin) / len(data)
    max_val = max(data)
    for i, val in enumerate(data):
        # scale bar height relative to max
        x0 = margin + i * bar_width
        y0 = c_height - (val / max_val) * (c_height - 20)
        x1 = margin + (i + 1) * bar_width - 2
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 3, y0 - 10, anchor=NW, text=str(val), font=("Arial", 9), fill="black")
    root.update()            # <- ensure the GUI updates immediately

# bubble sort with animation
def bubble_sort(data, delay=0.9):
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            # show current comparison
            colors = ["yellow" if x == j or x == j + 1 else "lightblue" for x in range(n)]
            draw_bars(data, colors)
            time.sleep(delay)
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
                # show after swap
                colors = ["green" if x == j or x == j + 1 else "lightblue" for x in range(n)]
                draw_bars(data, colors)
                time.sleep(delay)
        # mark the already placed elements with a different color
        colors = ["blue" if x >= n - i - 1 else "lightblue" for x in range(n)]
        draw_bars(data, colors)
        time.sleep(delay / 2)
        if not swapped:
            break
    # final color
    draw_bars(data, ["purple" for _ in range(n)])

# start button callback
def start_sort():
    raw = entry.get()
    if not raw.strip():
        return
    try:
        data = list(map(int, raw.split()))
    except ValueError:
        status_label.config(text="Enter integers separated by spaces", fg="red")
        return
    status_label.config(text="", fg="black")
    draw_bars(data, ["lightblue" for _ in range(len(data))])
    # call the sorting (this blocks the GUI while sorting; acceptable for learning/visualization)
    bubble_sort(data, delay=0.25)

# UI controls
Label(root, text="Enter numbers (space-separated):", font=("Arial", 12)).pack(pady=(8,0))
entry = Entry(root, font=("Arial", 12), width=50)
entry.pack(pady=6)

control_frame = Frame(root)
control_frame.pack(pady=6)
Button(control_frame, text="Start Bubble Sort", command=start_sort, font=("Arial", 11), bg="#a3d5ff").pack(side=LEFT, padx=6)
Button(control_frame, text="Example", command=lambda: entry.delete(0, END) or entry.insert(0, "5 2 9 1 6 3"), font=("Arial", 11)).pack(side=LEFT, padx=6)

status_label = Label(root, text="", font=("Arial", 10))
status_label.pack()

# initial empty canvas
draw_bars([1], ["white"])
canvas.delete("all")

root.mainloop()
