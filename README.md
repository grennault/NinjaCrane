<!-- PROJECT TITLE -->
<br />
<div align="center">
<h1 align="center"> <i>NinjaCrane</i>  : a Cybersecurity Attack Demonstrator on a polar crane's Industrial Control System (ICS)</h1>
</div>

<!-- SHIELDS -->

[![Contact Me](https://img.shields.io/badge/Contact_Me-blue)](mailto:gaietan.renault@alumni.epfl.ch)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/grennault)
[![License: FDL v1.3](https://img.shields.io/badge/License-FDLv1.3-blue.svg)](https://github.com/grennault)

<!-- INTRODUCTION -->

> **Welcome to my MSc Thesis in industry repository**
>
> This thesis is academically supervised by [Prof. M. Payer](https://nebelwelt.net/) from [HexHive lab.](https://hexhive.epfl.ch/) at [Ecole Polytechnique Fédérale de Lausanne (EPFL)](https://epfl.ch/).
>
> [<img src="img/epfl.png" height="80">](https://www.epfl.ch) [<img src="img/hexhive.png" height="80">](https://hexhive.epfl.ch/#)
>
> The internship is supervised in company by N. Sursin from [Electricité de France (EDF)](https://www.edf.fr/en) - Direction Projet Nouveau Nucléaire (DIPNN) - Direction Technique (DT) - Département Composants Electriques et Electromécaniques (CEE) - Groupe Contrôle-Commande (CC).
>
> [<img src="img/edf.png" height="90">](https://www.edf.fr/)

<!-- TABLE OF CONTENTS -->
<h2>
  <summary>&nbsp;&nbsp;&nbsp;&nbsp;Table of Contents</summary>
  <ol>
    <h6><li><a href="#abstract">Abstract</a></li></h6>
    <h6><li><a href="#structure">Structure</a></li></h6>
    <h6><li><a href="#how-to-start-">How to start ?</a></li></h6>
    <h6><li><a href="#use--distribution">Use & Distribution</a></li></h6>
    <h6><li><a href="#contributor">Contributor</a></li></h6>
  </ol>
</h2>

<!-- ABSTRACT -->

## Abstract

> Despite the sophisticated _Stuxnet_ attack discovered in 2010, the cybersecurity awareness around the _Industrial and Control System_ (ICS) remains a challenge. The necessity to train ICS actors and raise awareness on this issue increases. Moreover, listing the best practices to follow regarding a security policy has a limited impact on their effectiveness compared to an awareness program. In this context, this Master’s Project builds a cyberattack demonstrator targeting a part of a nuclear power-plant ICS and more precisely the polar crane's _Control System_. The described attack, called _NinjaCrane_, infects an engineering workstation through an USB cable or a maliciously modified mouse and deploys a malware targeting the communication with a _Modicon M580_, a _Programmable Logic Controller_ (PLC), by conducting a _Meet-In-The-Middle Attack_ (MITM) exploiting the CVE-2021-22779 vulnerability (a.k.a. _ModiPwn_). This work illustrates and highlights the necessity to respect the ICS security policy and may well suit an awareness program.

<!-- REPOSITORY STRUCTURE -->

## Structure

> ### Folders
>
> - `Attacks`: Explore bluetooth (BLE) and TCP/Modbus/UMAS (in Unity Pro v13.1) attack vectors.
>
> - `gui`: Graphical User Interface (GUI) run by the attacker (for demonstration purpose).
>
> - `img`: Images folder.
>
> - `report`: LaTeX Report & Slides folder. You will find in this folder all the technical informations regarding my project.
>
> - `LICENSE`: LICENSE folder containing the GNU Free Documentation License v1.3 and the GNU General Public License v3. All documents and scripts in this repo are respectively released under those Licenses.

<!-- HOW TO START ? -->

## How to start ?

> - Read my MSc report at [`\report\report.pdf`](https://github.com/grennault/NinjaCrane/tree/main/report/report.pdf).
> - Explore the [`\Attacks`](https://github.com/grennault/NinjaCrane/tree/main/Attacks) folder containing the attack vectors like the USB Ninja pro cable, the USB Ninja cable, the maliciously tampered mouse and the _NinjaCrane_ Meet-In-The-Middle malware targetting the connection between a Modicon M580 PLC and an engineering workstation.
> - Explore the [`\gui`](https://github.com/grennault/NinjaCrane/tree/main/gui) folder containing a ~~beautiful~~ pythonic GUI controlling the USB Ninja cable or the USB Ninja pro. cable. This GUI allows to trigger the cables and deploy & control the _NinjaCrane_ malware.

<!-- DEMONSTRATION -->

## Demo

> - Watch the [`\report\demo.mp4`](https://github.com/grennault/NinjaCrane/tree/main/report/demo.mp4) video.

![Demo video of the attack](/report/demo.mp4)

<!-- USE & DISTRIBUTION -->

## Use & Distribution

### Licence

> All my scripts are released under the GNU General Public License v3. See LICENCE folder to have the text of the GNU GPLv3.
>
> All my documents are released under the GNU Free Documentation License v1.3. See LICENCE folder to have the text of the GNU FDLv1.3.

### Code of conduct

> This work is provided AS IS without warranty of any kind. The author of this GitHub repository does not condone the use of this work for any illegal or malicious activities.

### Responsible Disclosure

> This work has been previously disclosed to Schnieder Electric and all presented vulnerabilities have already been identified.

<!-- CONTRIBUTOR -->

## Contributor

> [Gaiëtan Renault](mailto:gaietan.renault@alumni.epfl.ch)
