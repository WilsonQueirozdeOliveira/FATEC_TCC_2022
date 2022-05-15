/*

red	= gnd	=
black	= D2	= PORTD 2 LED_PIN_R
green	= D4	= PORTD 4 LED_PIN_Y
yellow	= D6	= PORTD 6 LED_PIN_G

*/


#define F_CPU 16000000UL
#define LED_PIN_R 2
#define LED_PIN_Y 4
#define LED_PIN_G 6

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRD |= (1<<LED_PIN_R);// set pin (PORTD 2) as output
	DDRD |= (1<<LED_PIN_Y);// set pin (PORTD 4) as output
	DDRD |= (1<<LED_PIN_G);// set pin (PORTD 6) as output
	while(1)
	{
		PORTD ^= (1<<LED_PIN_G);// toggles pin (PORTD 6)
		_delay_ms(5000);
		PORTD ^= (1<<LED_PIN_G);// toggles pin (PORTD 6)
		PORTD ^= (1<<LED_PIN_Y);// toggles pin (PORTD 4)
		_delay_ms(1000);
		PORTD ^= (1<<LED_PIN_Y);// toggles pin (PORTD 4)
		PORTD ^= (1<<LED_PIN_R);// toggles pin (PORTD 2)
		_delay_ms(5000);
		PORTD ^= (1<<LED_PIN_R);// toggles pin (PORTD 2)
	}
}
