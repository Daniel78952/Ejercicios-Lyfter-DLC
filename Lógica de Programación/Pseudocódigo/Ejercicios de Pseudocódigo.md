Precio de producto



Inicio

Definir *precio*

Definir *descuento*

Definir *precio\_final*

Mostrar "Digite el precio del producto: "

Pedir *precio*

Si *precio* >= 100 entonces:

&nbsp;	*descuento* = *precio* \* 0.10

&nbsp;	*precio\_final* = *precio* - *descuento*

Sino:

&nbsp;	*descuento* = *precio* \* 0.02

 	*precio\_final* = *precio* - *descuento*

FinSi

Mostrar "El precio final --> "

Mostrar *precio\_final*

Fin





Tiempo en segundos



Inicio

Definir *segundos\_de\_usuario*

Definir *segundos\_faltantes*

Mostrar "Introduzca los segundos"

Pedir *segundos\_de\_usuario*

Si *segundos\_de\_usuario* = 600:

&nbsp;	Mostrar "Igual"

Sino: 

&nbsp;	Si *segundos\_de\_usuario* > 600:

&nbsp;		Mostrar "Mayor"

&nbsp;	Sino: 

&nbsp;		*segundos\_faltantes* = 600 - *segundos\_de\_usuario*

&nbsp;		Mostrar *segundos\_faltantes*

	FinSi

FinSi

Fin





Sumas

Inicio

Definir *num\_usuario*

Definir *contador*

Definir *suma*

*contador* = 1

*suma* = 0

Mostrar "Digite un número"

Pedir *num\_usuario*

Mientras *num\_usuario* >= *contador*:

&nbsp;	*suma* = *contador* + *suma*

&nbsp;	*contador* = *contador + 1*

FinMientras

Mostrar *suma*

Fin



