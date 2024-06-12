import tkinter
import tkintermapview

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("map.py")



# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
# set current widget position and zoom
map_widget.set_position(40, -3.7)
map_widget.set_zoom(6)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()