#define LAYOUT_FRENCH  //Add this line before include
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

byte* pointer = 0;

char tmpString[33] = "echo|set/p=00>>ArduinoMemory.txt";
String tmpString2 = "  ";

void setup() 
{
  //SetRunOnce(PAYLOADA,true);
  //SetRunOnce(PAYLOADB,true);
  //If you want payload to run only once, run this function.

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
                        //line was temporarily cut off.
	/*
	You should call NinjaKeyboard.begin() after you call 
	NinjaKeyboard.end()
	Or, the NinjaKeyboard was disconnected and any action was not usable.
	*/
	  NinjaKeyboard.begin();     //Initliaze NinjaKeyboard USB Interface.
    NinjaKeyboard.delay(1000);     //Delay 1 sec to compatibility Win7,
                        //Some systems require 5 sec of preparation time.
    NinjaKeyboard.sendKeyStroke(0);//Send HID '0' to compatibility Win7.
    NinjaKeyboard.delay(1000);     //Delay 1 second to wait system.
                                     //Recognize the NinjaKeyboard.
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
    //Call out the run window.
    NinjaKeyboard.delay(100);                           //Delay 100mS.
    NinjaKeyboard.print(F("cmd"));                //Open a notepad.
    NinjaKeyboard.sendKeyStroke(MOD_SHIFT_LEFT);      
    //Press SHIFT to compatible Chinese Input Method.
    NinjaKeyboard.delay(100); 
    NinjaKeyboard.sendKeyStroke(KEY_ENTER); 
    NinjaKeyboard.delay(500); 
    NinjaKeyboard.sendKeyStroke(MOD_SHIFT_LEFT);      
    //Press SHIFT to compatible Chinese Input Method.
    NinjaKeyboard.println(F("cd Desktop"));
    NinjaKeyboard.delay(100); //Delay 100 millisecond , 
    NinjaKeyboard.println(F("mkdir script"));
    NinjaKeyboard.delay(100); //Delay 100 millisecond , 
    NinjaKeyboard.println(F("cd script"));
    NinjaKeyboard.delay(100); //Delay 100 millisecond , 
    NinjaKeyboard.println(F(".>ArduinoMemory.txt 2>NUL"));
    NinjaKeyboard.delay(100); //Delay 100 millisecond , 

    for(int i=0; i < 2048; ++i) {
      pointer += 1;
      tmpString2 =  String((*pointer), HEX);
      if (tmpString2.length() > 1) {
          tmpString[11] = (char) tmpString2[0];
          tmpString[12] = (char) tmpString2[1];
      } else {
          tmpString[11] = '0';
          tmpString[12] = (char) tmpString2[0];
          
      }
      NinjaKeyboard.delay(50); //Delay 1000 millisecond ,
      NinjaKeyboard.println( tmpString ); 
    }
    
                          
	/*
	While your cable connect to Some Phone, Only switch USB DATA was 
	not enough. The PC was still think that your phone was Ninja 
	(Your Phone Not send USB ReEmulate command), it may cause 
	non-stoppable input or NinjaKeyboard Device still Retain in your system.
	*/
  	NinjaKeyboard.end();          //Send Disconnect command to
  	                                //NinjaKeyboard USB Interface	
    USBninjaOffline();  //USBNinja disappear. Cable Line back to normal.
  	NinjaKeyboard.begin();  //ReStart Keyboard Interface while USB DATA
  	                        //was cut off. So you can use payloadB without 
							//ReEmulate NinjaKeyboard.
}

/*
When the Bluetooth remote control button B is pressed. 
The program in payloadB() will be executed in a loop. 
Until the button B is released.
*/

void payloadB()
{
    USBninjaOnline();  // USBNinja appears.  
                         //The cable's data line was temporarily cut off.
    NinjaKeyboard.sendKeyStroke(0); //Send HID '0' to compatibility Win7.
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
}
