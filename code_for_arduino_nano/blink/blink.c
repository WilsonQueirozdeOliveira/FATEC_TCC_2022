#define F_CPU 16000000UL
#define LED_PIN 0

#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRB |= (1<<LED_PIN);// set pin (PORTB 0) as output
	while(1)
	{
		PORTB ^= (1<<LED_PIN);// toggles pin (PORTB 0)
		_delay_ms(1000); // busy wait, 500ms
	}
}
