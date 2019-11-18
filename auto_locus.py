import get_locus, get_common_points
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Auto Locus")
root.resizable(False, False)


def calculate_locus_button_click():
    input_function = input_entry.get()
    input_function = get_locus.convert_function_to_python(input_function)
    x_param = None
    points = None

    # check if function is empty
    if input_function == "":
        locus_output_label.config(text="Missing Parameter")
        return False
    kind_of_points = points_combobox.get()

    # check if combobox is empty
    if kind_of_points == "":
        locus_output_label.config(text="Missing Parameter")
        return False
    elif kind_of_points == "Bend Points":
        try:
            points = get_locus.get_bend_points(input_function)
            print("bend_points:", points)
        except:
            locus_output_label.config(text="Invalid Input")
            return False

        if not points:
            locus_output_label.config(text="No bendpoints found")
            return False

    elif kind_of_points == "Turning Points":
        try:
            points = get_locus.get_turning_points(input_function)
            print("turning_points:", points)
        except:
            locus_output_label.config(text="Invalid Input")
            return False

        if not points:
            locus_output_label.config(text="No turning points found")
            return False

    x_param = get_locus.get_x_param(points[0][0])
    print("x_param:", x_param)

    if not x_param:
        locus_output_label.config(text="No locus found")
        return False
    try:
        output_function = get_locus.insert_into_y_value(x_param, points[0][1])
        print("output_function:", output_function)
    except:
        locus_output_label.config(text="No locus found")
        return False

    # reconverting function
    output_function = get_locus.convert_function_from_python(output_function)
    locus_output_label.config(text="g(x)=" + output_function)


def calculate_bend_points_button_click():
    input_function = input_entry.get()
    input_function = get_locus.convert_function_to_python(input_function)

    # check if function is empty
    if input_function == "":
        common_points_label.config(text="Missing Parameter")
        return False

    try:
        common_points = get_common_points.get_common_points(input_function)
        print("common_points:", common_points)
    except:
        common_points_label.config(text="Invalid Input")
        return False

    if not common_points:
        common_points_label.config(text="No common points found")
        return False

    output_string = ""
    for n in common_points:
        output_string += str(n)
        if common_points.index(n) > 0:
            output_string += ", "

    common_points_label.config(text=output_string)


# Row 0
input_label = ttk.Label(root, text="Input Function:")
input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

input_entry = ttk.Entry(root)
input_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")

# Row 1
points_label = ttk.Label(root, text="Points:")
points_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

points_combobox = ttk.Combobox(root, values=["Bend Points", "Turning Points"], state="readonly")
points_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="e")

# Row 2
run_button = ttk.Button(root, text="Calculate Locus", command=calculate_locus_button_click)
run_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")

run_button_2 = ttk.Button(root, text="Calculate Common Points", command=calculate_bend_points_button_click)
run_button_2.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Row 3
space_label = ttk.Label(root)
space_label.grid(row=3, column=0, pady=4, sticky="w")

# Row 4
locus_output_label_name = ttk.Label(root, text="Locus:")
locus_output_label_name.grid(row=4, column=0, padx=5, pady=5, sticky="w")

locus_output_label = ttk.Label(root, borderwidth=2, relief="groove")
locus_output_label.grid(row=4, column=1, padx=5, pady=5, sticky="we")

# Row 5
common_points_label_name = ttk.Label(root, text="Common Points:")
common_points_label_name.grid(row=5, column=0, padx=5, pady=5, sticky="w")

common_points_label = ttk.Label(root, borderwidth=2, relief="groove")
common_points_label.grid(row=5, column=1, padx=5, pady=5, sticky="we")


root.mainloop()
