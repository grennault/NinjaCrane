# Written by G. Renault - 15.03.2023
# This script is a pythonic Graphical User Interface (GUI) for the attacker.
# It draws a sketch of the attack scenario.

# Copyright (C) 2023  Gaiëtan Renault.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import PySimpleGUI as sg
import os
import numpy as np
from PIL import Image, ImageColor, ImageDraw
from matplotlib.image import imread
from io import BytesIO
import base64
import cv2
import asyncio
from bleak import BleakScanner, BleakClient, exc
import ctypes
import platform
# import bluetooth
import types
import multiprocessing
import bluetooth_send
import time

# Print the available font (OS-dependent) : sg.Text.fonts_installed_list()

BLE_address = "CE:31:66:D0:67:EC"  # USB Ninja BLE Address
password = b'\x35\x39\x37\x32'     # Password is '5972'
console_msg = ""                   # Console message to print
laser_pointer_cursor = False       # Cursor pointer
# USB Ninja cable ("USB Ninja cable") or USB Ninja cable pro. ("USB Ninja cable pro.")
cable = "USB Ninja cable"


def open_window(state_success):
    if not state_success:
        msg = " Connection with cable failed,\nplease try again"
    elif state_success:
        msg = " Success"
    layout = [
        [sg.Text(msg, font=("Arial", 15), justification="center", text_color="red")]]
    window = sg.Window("Warning", layout, modal=True, size=(
        600, 100), icon=path + "\\img\\icon.ico", element_justification="center")
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


def activate_bluetooth():
    """Activates bluettoth using bluetooth (pybluez) package
    """
    # print(bluetooth.read_local_bdaddr())
    # OR
    os.system("powershell \"[CmdletBinding()] Param () If ((Get-Service bthserv).Status -eq 'Stopped') {Start-Service bthserv} Add-Type -AssemblyName System.Runtime.WindowsRuntime;$asTaskGeneric=([System.WindowsRuntimeSystemExtensions].GetMethods()|?{$_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0];Function Await($WinRtTask,$ResultType) {$asTask = $asTaskGeneric.MakeGenericMethod($ResultType);$netTask=$asTask.Invoke($null,@($WinRtTask));$netTask.Wait(-1) | Out-Null;$netTask.Result};[Windows.Devices.Radios.Radio,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;[Windows.Devices.Radios.RadioAccessStatus,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;Await ([Windows.Devices.Radios.Radio]::RequestAccessAsync()) ([Windows.Devices.Radios.RadioAccessStatus]) | Out-Null;$radios=Await ([Windows.Devices.Radios.Radio]::GetRadiosAsync()) ([System.Collections.Generic.IReadOnlyList[Windows.Devices.Radios.Radio]]);$bluetooth = $radios | ? {$_.Kind -eq 'Bluetooth'};[Windows.Devices.Radios.RadioState,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;Await ($bluetooth.SetStateAsync('On')) ([Windows.Devices.Radios.RadioAccessStatus]) | Out-Null\"")

# For resolution compatibility


def make_dpi_aware():
    if int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)


make_dpi_aware()

# Draw image from image name at location with a zoom scale


def _draw_img_from_name(img_name, zoom_size, location, crop=None):
    image_data = imread(path + "/img/" + img_name)
    if crop is not None:
        image_data = image_data[crop[0]: -crop[0], crop[1]: -crop[1]]
    image_data = cv2.resize(image_data, zoom_size)
    buffered = BytesIO()
    Image.fromarray(image_data).save(buffered, format="PNG", compress_level=0)
    img_str = base64.b64encode(buffered.getvalue())
    buffered.close()
    window["-GRAPH-"].DrawImage(data=img_str, location=location)


# Convert np array image to Tkinter Image
def _photo_image(image: np.ndarray):
    height, width = image.shape
    data = f"P5 {width} {height} 255 ".encode(
    ) + image.astype(np.uint8).tobytes()
    return ImageTk.PhotoImage(width=width, height=height, data=data, format="PPM")


# Draw dashed line
def _draw_dash_line(point_from, point_to, width, color, nbr_dash, shift=0.5):
    dir_unit = (np.array(point_to) - np.array(point_from)) // nbr_dash
    point_from_tmp = np.array(point_from) + shift * dir_unit
    point_to_tmp = np.array(point_from) + dir_unit + shift * dir_unit
    for _ in range(nbr_dash // 2):
        window["-GRAPH-"].draw_line(
            tuple(point_from_tmp), tuple(point_to_tmp), width=width, color=color
        )
        point_from_tmp += 2 * dir_unit
        point_to_tmp += 2 * dir_unit


def _draw_on_graph():
    air_gap = window["-GRAPH-"].draw_rectangle(
        (450, 150), (1700, 750), line_color="black", line_width=3, fill_color="white"
    )

    _draw_img_from_name("eng_station.jpg", (200, 200), (500, 400))
    _draw_img_from_name("HMI.jpg", (200, 200), (800, 700))
    _draw_img_from_name("M580.jpg", (200, 200), (500, 700))
    _draw_img_from_name("USB_cable.jpg", (75, 75), (470, 250), crop=(100, 200))
    _draw_img_from_name("hacker.jpg", (150, 150), (0, 300))
    _draw_img_from_name("pont-polaire.jpg", (200, 200), (1400, 400))
    _draw_img_from_name("hub_88012.jpg", (100, 100), (1375, 275))
    _draw_img_from_name("ESP32.jpg", (200, 200), (1100, 400))

    infected_usb_cable = window["-GRAPH-"].draw_rectangle(
        (470, 175), (545, 250), line_color="red", line_width=3
    )
    infected_usb_cable = window["-GRAPH-"].draw_rectangle(
        (1375, 175), (1475, 275), line_color="red", line_width=3
    )

    window["-GRAPH-"].draw_text(
        "Serial", (90, 550), font=("Helvetica", 10), color="black"
    )
    window["-GRAPH-"].draw_text(
        "Bluetooth", (90, 600), font=("Helvetica", 10), color="black"
    )
    window["-GRAPH-"].draw_text(
        "Bluetooth connection", (300, 250), font=("Helvetica", 10), color="black"
    )

    window["-GRAPH-"].draw_text(
        "Modicon M580", (600, 720), font=("Helvetica", 10), color="black"
    )
    window["-GRAPH-"].draw_text(
        "HMI", (900, 720), font=("Helvetica", 10), color="black"
    )
    window["-GRAPH-"].draw_text(
        "Engineering Station", (600, 420), font=("Helvetica", 10), color="black"
    )
    window["-GRAPH-"].draw_text(
        "Rotary overhead crane", (1500, 420), font=("Helvetica", 10), color="black"
    )
    window["-GRAPH-"].draw_text(
        "ESP32", (1200, 420), font=("Helvetica", 10), color="black"
    )

    # Link between engineering station and M580
    window["-GRAPH-"].draw_line((600, 440), (600, 490),
                                color="black", width=10)
    # Link between M580 and HMI
    window["-GRAPH-"].draw_line((720, 600), (800, 600),
                                color="black", width=10)
    # Link between M580 and ESP32
    window["-GRAPH-"].draw_line((690, 510), (1080, 310),
                                color="black", width=10)
    window["-GRAPH-"].draw_line((140, 550), (200, 550),
                                color="black", width=10)  # Legend serial

    _draw_dash_line((140, 210), (470, 210), 8, "blue",
                    10)  # Link between hacker and cable
    _draw_dash_line((1280, 260), (1375, 210), 8, "blue",
                    4)  # Link between ESP32 and Hub
    _draw_dash_line((140, 600), (200, 600), 8, "blue", 4)   # Legend BLE


# Absolute path of this file
path = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    sg.theme("Dark")

    graph_size = (1900, 800)
    img_to_print = [
        [
            sg.Graph(
                background_color="white",
                expand_x=True,
                expand_y=True,
                canvas_size=graph_size,
                graph_bottom_left=(0, 0),
                graph_top_right=graph_size,
                key="-GRAPH-",
                motion_events=True,
                drag_submits=False,
                enable_events=True,
                right_click_menu=["&Right", ["clear graph"]],
            )
        ]
    ]

    console = [
        [
            sg.Text(" " * 100, font=("DejaVu Sans Mono", 10)),
        ],
        [
            sg.Text(
                "\n\n\n",
                font=("Lucida Sans Typewriter", 10),
                key="-console-msg-",
            ),
        ],
    ]

    layout = [
        [sg.Text(" Say hello to HiJack! This graphical user interface models an attack on the Modicon M580. \n"),
         sg.Push(),
         sg.Combo(["USB Ninja cable", "USB Ninja cable pro."], default_value=cable, button_background_color="white", button_arrow_color="black", key="combo-cable", pad=(10, 0), readonly=True)],
        [sg.Column(img_to_print)],
        [
            sg.Push(),
            sg.Button("Deploy Malware.",
                      key="Bluetooth_connection_A", button_color="black"),
            sg.Button("Trigger Attack A.",
                      key="Bluetooth_connection_B", button_color="black"),
            sg.Push()
        ],
        [
            sg.Text("")
        ],
        [
            sg.Frame(
                " Console ",
                console,
                pad=(10, 0),
                expand_y=True,
                expand_x=True,
                right_click_menu=["&Right", ["clear console"]],
            )
        ],
        [
            sg.Text("Made by Gaiëtan Renault", expand_x=True,
                    justification='center', tooltip="gaietan.renault@epfl.alumni.ch"),
        ],
    ]

    window = sg.Window(
        "HiJack!", layout, size=(1800, 1000), icon=path + "\\img\\icon.ico", resizable=True
    ).Finalize()
    window.Maximize()

    _draw_on_graph()

    while True:
        (
            event,
            values,
        ) = window.read(timeout=10)

        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "-GRAPH-":
            if laser_pointer_cursor:
                laser_pointer_cursor = not laser_pointer_cursor
                window.set_cursor("arrow")
            else:
                laser_pointer_cursor = not laser_pointer_cursor
                window.set_cursor("cross")

        elif event == "clear graph":
            _draw_on_graph()

        elif event == "clear console":
            window["-console-msg-"].update(f"\n\n\n")

        elif "Bluetooth_connection" in event:
            window["-console-msg-"].update(f"Activating bluetooth...\n\n")
            window.read(timeout=10)
            activate_bluetooth()
            console_msg = "Activating bluetooth. Done.\n\n"
            window["-GRAPH-"].draw_text(
                "Bluetooth connection", (300, 250), font=("Helvetica", 10), color="red"
            )
            window["-console-msg-"].update(console_msg)
            window.read(timeout=10)
            time.sleep(0.5)

            window["-console-msg-"].update(console_msg +
                                           f"\nEstablishing connection with the antenna...\n")
            window.read(timeout=10)
            manager = multiprocessing.Manager()
            return_dict = manager.dict()
            return_dict["success"] = False

            payload = event[-1]
            process1 = multiprocessing.Process(target=bluetooth_send.deamon, args=(
                BLE_address, password, payload, return_dict))
            process1.start()
            window.read(timeout=10)
            process1.join()

            if return_dict.values()[0]:
                if payload == "A":
                    msg = "Malware is now running on engineering worksation"
                elif payload == "B":
                    msg = "Attacking industrial process"
                console_msg += f"\nEstablishing connection with the antenna.\n{msg} !"
                window["-console-msg-"].update(console_msg)

                _draw_dash_line((140, 210), (470, 210), 8, "red", 10)
                window["-GRAPH-"].draw_line((600, 440), (600, 490),
                                            color="red", width=10)
                window["-GRAPH-"].draw_text(
                    "Engineering Station", (600, 420), font=("Helvetica", 10), color="black"
                )
                if payload == "B":
                    window["-GRAPH-"].draw_line((690, 510),
                                                (1080, 310), color="red", width=10)
                    _draw_dash_line((1280, 260), (1375, 210), 8, "red", 4)
            else:
                console_msg += f"\nEstablishing connection with the antenna... Failed :'("
                window["-console-msg-"].update(console_msg)

            window.read(timeout=10)
            open_window(return_dict.values()[0])

    window.close()
