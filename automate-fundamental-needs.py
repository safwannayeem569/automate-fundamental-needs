#!/usr/bin/env python

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from os.path import exists
from os.path import expanduser
from pathlib import Path
import os
import shutil
import subprocess

class MyWindow1(Gtk.Window):
    def __init__(self):
        super().__init__(title="Automate Fundamental Needs")

        self.set_border_width(15)
        self.set_default_size(900, 700)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)

        frame1 = Gtk.Frame(label="")

        grid1 = Gtk.Grid(row_spacing    = 35,
                         column_spacing = 20,
                         column_homogeneous = True)

        image1 = Gtk.Image()
        image1.set_from_file("/home/safwan/Desktop/gtk/code-examples/gtk-with-python/image1.png")

        label1 = Gtk.Label(label="Welcome to the world of automation! Need help fulfilling your Fundamental Needs?")
        label1.set_hexpand(True)

        label2 = Gtk.Label(label="We've got you covered. Use this app if you don't want to lag behind a decade.")
        label2.set_hexpand(True)
\
        button1 = Gtk.Button(label="Food Supply")
        button1.set_hexpand(True)
        button1.connect("clicked", self.on_button1_clicked)

        button2 = Gtk.Button(label="Uber")
        button2.set_hexpand(True)
        button2.connect("clicked", self.on_button2_clicked)

        button3 = Gtk.Button(label="Collage Notice")
        button3.set_hexpand(True)
        button3.connect("clicked", self.on_button3_clicked)

        button4 = Gtk.Button(label="Share Location")
        button4.set_hexpand(True)
        button4.connect("clicked", self.on_button4_clicked)

        button5 = Gtk.Button(label="Call 999")
        button5.set_hexpand(True)
        button5.connect("clicked", self.on_button5_clicked)

        button6 = Gtk.Button(label="Medicine")
        button6.set_hexpand(True)
        button6.connect("clicked", self.on_button6_clicked)

        button7 = Gtk.Button(label="Books")
        button7.set_hexpand(True)
        button7.connect("clicked", self.on_button7_clicked)

        button8 = Gtk.Button(label="Plane Ticket")
        button8.set_hexpand(True)
        button8.connect("clicked", self.on_button8_clicked)

        button9 = Gtk.Button(label="Newspapers")
        button9.set_hexpand(True)
        button9.connect("clicked", self.on_button9_clicked)

        button10 = Gtk.Button(label="Hospitals")
        button10.set_hexpand(True)
        button10.connect("clicked", self.on_button10_clicked)

        button11 = Gtk.Button(label="Residential Hotels")
        button11.set_hexpand(True)
        button11.connect("clicked", self.on_button11_clicked)

        button12 = Gtk.Button(label="Groceries")
        button12.set_hexpand(True)
        button12.connect("clicked", self.on_button12_clicked)

        button13 = Gtk.Button(label="Clothing")
        button13.set_hexpand(True)
        button13.connect("clicked", self.on_button13_clicked)

        button14 = Gtk.Button(label="Refreshment")
        button14.set_hexpand(True)
        button14.connect("clicked", self.on_button14_clicked)

        button15 = Gtk.Button(label="Namaz & Roza")
        button15.set_hexpand(True)
        button15.connect("clicked", self.on_button15_clicked)

        button16 = Gtk.Button(label="Exit")
        button16.set_hexpand(True)
        button16.connect("clicked", Gtk.main_quit)

        grid1.attach(image1,  0, 0, 3, 2)
        grid1.attach(label1,  0, 2, 3, 2)
        grid1.attach(label2,  0, 3, 3, 2)
        grid1.attach(button1, 0, 6, 1, 2)
        grid1.attach(button2, 1, 6, 1, 2)
        grid1.attach(button3, 2, 6, 1, 2)
        grid1.attach(button4, 0, 10, 1, 2)
        grid1.attach(button5, 1, 10, 1, 2)
        grid1.attach(button6, 2, 10, 1, 2)
        grid1.attach(button7, 0, 14, 1, 2)
        grid1.attach(button8, 1, 14, 1, 2)
        grid1.attach(button9, 2, 14, 1, 2)
        grid1.attach(button10, 0, 18, 1, 2)
        grid1.attach(button11, 1, 18, 1, 2)
        grid1.attach(button12, 2, 18, 1, 2)
        grid1.attach(button13, 0, 22, 1, 2)
        grid1.attach(button14, 1, 22, 1, 2)
        grid1.attach(button15, 2, 22, 1, 2)
        grid1.attach(button16, 1, 26, 1, 2)

        self.add(frame1)
        frame1.add(grid1)

    def on_button1_clicked(self, widget):
        print("User chose: About DTOS")
        subprocess.run(["xdg-open", "https://www.foodpanda.com.bd/city/dhaka"])

    def on_button2_clicked(self, widget):
        print("User chose: Knowledge Base")
        subprocess.run(["xdg-open", "https://m.uber.com/looking"])

    def on_button3_clicked(self, widget):
        print("User chose: Collage Notice")
        subprocess.run(["xdg-open", "https://ndc.edu.bd/notice-lists"])

    def on_button4_clicked(self, widget):
        print("User chose: Share Location")
        subprocess.run(["xdg-open", "https://www.google.com/maps/"])

    def on_button5_clicked(self, widget):
        print("User chose: Call 999")
        subprocess.run(["xdg-open", "https://imgs.search.brave.com/TcyAElhGQnKjZPg5l7R8heLRZ5XxrEgjswckI4pxn60/rs:fit:1190:595:1/g:ce/aHR0cDovL3N0YXRp/YzYuYnVzaW5lc3Np/bnNpZGVyLmNvbS9p/bWFnZS81ODdkZjQw/YWRkMDg5NTk5MjI4/YjRiOWEtMTE5MC02/MjUvaG93LXRvLWFs/ZXJ0LXRoZS1wb2xp/Y2Utb24tdGhlLXBo/b25lLWlmLWl0LWlz/bnQtc2FmZS10by1z/cGVhay5qcGc"])

    def on_button6_clicked(self, widget):
        print("User chose: Medicine")
        subprocess.run(["xdg-open", "https://www.arogga.com/"])

    def on_button7_clicked(self, widget):
        print("User chose: Books")
        subprocess.run(["xdg-open", "https://drive.google.com/file/d/1O_qmMAUIlVDIPcz1UPUoPlrg14wDOPik/view"])

    def on_button8_clicked(self, widget):
        print("User chose: Plane Ticket")
        subprocess.run(["xdg-open", "https://www.alternativeairlines.com/biman-bangladesh-airlines"])

    def on_button9_clicked(self, widget):
        print("User chose: Newspapers")
        subprocess.run(["xdg-open", "https://www.allbanglanewspaper.xyz/"])

    def on_button10_clicked(self, widget):
        print("User chose: Hospitals")
        subprocess.run(["xdg-open", "http://www.dscc.gov.bd/site/page/c6818c61-93b4-4b91-97c9-ab814113a88b/%E0%A6%B9%E0%A6%BE%E0%A6%B8%E0%A6%AA%E0%A6%BE%E0%A6%A4%E0%A6%BE%E0%A6%B2"])

    def on_button11_clicked(self, widget):
        print("User chose: Residential Hotels")
        subprocess.run(["xdg-open", "https://www.booking.com/city/bd/coxs-bazar.en-gb.html"])

    def on_button12_clicked(self, widget):
        print("User chose: Groceries")
        subprocess.run(["xdg-open", "https://chaldal.com/"])

    def on_button13_clicked(self, widget):
        print("User chose: Clothing")
        subprocess.run(["xdg-open", "https://www.aarong.com/brands/taaga-man/taaga-man-eid-22"])

    def on_button14_clicked(self, widget):
        print("User chose: Refreshment")
        subprocess.run(["xdg-open", "https://www.youtube.com/"])

    def on_button15_clicked(self, widget):
        print("User chose: Knowledge Base")
        subprocess.run(["xdg-open", "https://www.salahtimes.com/bangladesh/dhaka"])

    def on_button16_clicked(self, widget):
        print("User chose: Exit")




win1 = MyWindow1()

win1.connect("destroy", Gtk.main_quit)

win1.show_all()
Gtk.main()
