/*

red		= gnd	=
black	= D2	= PORTD 2
green	= D4	= PORTD 4
yellow	= D6	= PORTD 6

*/


#define F_CPU 16000000UL
#define LED_PIN_R 0
#define LED_PIN_Y 0
#define LED_PIN_G 0

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRB |= (1<<LED_PIN_R);// set pin (PORTB 0) as output
	while(1)
	{
		PORTB ^= (1<<LED_PIN_R);// toggles pin (PORTB 0)
		_delay_ms(1000); // busy wait, 500ms
	}
}
