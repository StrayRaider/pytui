import TermTk as ttk

    # Set the VBoxLayout as default in the terminal widget
root = ttk.TTk(layout=ttk.TTkVBoxLayout())

    # Attach 4 buttons to the root widget
ttk.TTkButton(parent=root, border=True, text="Button1")
ttk.TTkButton(parent=root, border=True, text="Button2")
ttk.TTkButton(parent=root, border=True, text="Button3")
ttk.TTkButton(parent=root, border=True, text="Button4")

root.mainloop()
