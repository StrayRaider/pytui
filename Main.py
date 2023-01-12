import TermTk as ttk

name_t = "emre"
pw_t = "123e"

name = "give me your name     : "
password = "give me your password : "

root = ttk.TTk()
VBox = ttk.TTkVBoxLayout()
HBox = ttk.TTkHBoxLayout()
HBox_1 = ttk.TTkHBoxLayout()
HBox_2 = ttk.TTkHBoxLayout()
VBox.addItem(HBox_1)
VBox.addItem(HBox_2)
root.setLayout(VBox)

label_1 = ttk.TTkLabel(text=name)
name_inp = ttk.TTkLineEdit()
label_2 = ttk.TTkLabel(text=password)
pw_inp = ttk.TTkLineEdit()
HBox_1.addWidget(label_1,0,0)
HBox_1.addWidget(name_inp,0,1)
HBox_2.addWidget(label_2,0,0)
HBox_2.addWidget(pw_inp,0,1)

enter_button = ttk.TTkButton(border=True, text="Enter")
exp_label = ttk.TTkLabel(text="")
VBox.addWidget(enter_button)
VBox.addWidget(exp_label)


def enter_button_clicked():
    name_inp_text = name_inp.text()
    pw_inp_text = pw_inp.text()
    if(name_inp_text == name_t and pw_inp_text==pw_t):
        exp_label.setText("veri alındı")
    else:
        exp_label.setText("hatalı veri girişi yapıldı")


enter_button.clicked.connect(lambda : enter_button_clicked())

#ttk.TTkButton(parent=root, border=True, text="Button2")
#gridLayout.addWidget(ttk.TTkButton(parent=root, border=True, text="Button4"), 3,4)

root.mainloop()


