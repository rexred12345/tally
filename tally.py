from tkinter import Tk, Canvas
import keyboard

# Initialize variables
tally_marks = []
previous_tally = {}

# Vertical distance between tally marks
vertical_distance = 90

def draw_tally():
    global previous_tally
    
    # Get the current tally
    current_tally = previous_tally.get(key, 0)
    
    # Check if the maximum tally count has been reached
    if current_tally >= 3:
        return
    
    # Calculate coordinates for the new tally mark
    x = window.winfo_width() - (current_tally + 1) * (window.winfo_width() / 10) - 11
    y = key * (window.winfo_height() / 4) - 55
    
    # Create a vertical white tally mark
    tally = canvas.create_line(x, y, x, y + (window.winfo_height() / 12), width=2, fill="white")
    
    # Update the tally marks list
    tally_marks.append((tally, x, y))
    
    # Update the previous tally
    previous_tally[key] = current_tally + 1

def undo_tally():
    global tally_marks, previous_tally
    
    if not tally_marks:
        return
    
    # Remove the last tally mark from the canvas
    last_tally, x, y = tally_marks.pop()
    canvas.delete(last_tally)
    
    # Decrement the previous tally count
    key = y // (window.winfo_height() / 4) + 1
    previous_tally[key] -= 1
    
    # Update the coordinates of remaining tally marks
    for i in range(len(tally_marks)):
        tally, prev_x, prev_y = tally_marks[i]
        if prev_y == y:
            tally_marks[i] = (tally, prev_x + (window.winfo_width() / 10), prev_y)

def reset_tally():
    global tally_marks, previous_tally
    # Clear the canvas
    canvas.delete("all")
    
    # Reset variables
    tally_marks = []
    previous_tally = {}

def on_key_press(event):
    global key
    
    try:
        key = int(event.name)
    except ValueError:
        if event.name == "-":
            undo_tally()
        return
    
    if key == 0:
        reset_tally()
    elif key in [1, 2, 3, 4]:
        if key not in previous_tally:
            previous_tally[key] = 0
        draw_tally()

# Create the window
window = Tk()
window.title("Tally Program")
window.geometry("120x370")

# Create the canvas
canvas = Canvas(window, width=120, height=370, bg="black")
canvas.pack()

# Bind the key press event
keyboard.on_press(on_key_press)

# Focus the window
window.focus_set()

# Start the main loop
window.mainloop()
