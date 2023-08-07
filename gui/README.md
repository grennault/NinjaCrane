# gui - (Amazing) Graphical User Interface

This folder contains the graphical user interface (gui) of this project.

## Requirement

OS: Windows ONLY (I apologize for this, but the `HiJack.py` file could be modified to be run on UNIX).

Python packages :

- `cv2`
- `PIL`
- `matplotlib`
- `numpy`
- `PySimpleGUI`
- `pybluez` (For windows, requires `pip install setuptools==58` and C++ build tools `https://visualstudio.microsoft.com/visual-cpp-build-tools/`)

(See `requirements.txt` file for exact version, generated with `pipreqs --force path/to/gui` command)

## Structure

### Files

- `HiJack.py` : Main file, run this file to launch the gui. This
- `HiJack.exe` : Executable file, run this file to launch the gui without the need of requirements.
- `Bluetooth.py` : Bluetooth function, used to trigger the USBNinja cable payload. A BIG THANK YOU to the Embedded Lab Vienna for IoT & Security and its ELVIS project for their help. See [Exploiting the USB Ninja BLE Connection Wiki page](https://wiki.elvis.science/index.php?title=Exploiting_the_USB_Ninja_BLE_Connection).
- `requirements.txt` : Python packages required to run the gui
- `README.md` : This file

### Folders

- `img` : Contains all the images used in the gui

## How to use ?

Run `HiJack.py` !

I.e. : `python HiJack.py`

## Don't want to use python ? No problem run `HiJack.exe` file !

The `HiJack.exe` file has been generate using `pyinstaller --noconfirm --onefile --console --add-data "C:/Users/user/***TO_COMPLETE***/MSc_Project/gui/img;img/"  "C:/Users/user/***TO_COMPLETE***/MSc_Project/gui/HiJack.py"` (OR use easy to use auto-py-to-exe)
