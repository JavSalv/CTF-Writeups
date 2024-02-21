# Bocadillo Accidentado

## Enunciado

> Esta mañana terminé de prepararme mi bocadillo de bacon pero me dí cuenta de que no me quedaba papel de aluminio para envolverlo. A la desesperada, cogí 
> DOS folios que tenía cerca para envolverlo, sin darme cuenta de que era el papel donde tenía apuntada la flag.
> Después de comermelo intenté recuperarla pero había quedado completamente ilegible.
> Lo mas importante estaba en la segunda página, ayudadme a recuperarlo por favor.

## Archivos
[Envoltorio_Bocadillo.pdf](./Envoltorio_Bocadillo.pdf)

_ _ _

## Solución

Al abrir el PDF nos damos cuenta de que tiene solo una página, y el enunciado menciona que debería de tener dos páginas.
Hay que conseguir acceder a la segunda página.

Según se describe en [esta página](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7517136/) el número de páginas que contiene un
fichero PDF se almacena en hexadecimal con la estructura:

>~~~
>1 0 obj
><<
>/Kids [3 0 R 11 0 R]
>/Type /Pages
>/Count 2
>>>
>endobj
>~~~

Donde /Count indica el número de páginas del documento.
Si abrimos el PDF en un editor hexadecimal, vemos que efectivamente el número de páginas está puesto a 1.

>~~~
> $ xxd Envoltorio_Bocadillo.pdf
> ...
> 00016e50: 0a2f 4b69 6473 205b 3320 3020 5220 3137  ./Kids [3 0 R 17
> 00016e60: 2030 2052 5d0a 2f54 7970 6520 2f50 6167   0 R]./Type /Pag
> 00016e70: 6573 0a2f 436f 756e 7420 310a 3e3e 0a65  es./Count 1.>>.e
> 00016e80: 6e64 6f62 6a0a 0a32 3720 3020 6f62 6a0a  ndobj..27 0 obj.
> ...
>~~~

Si cambiamos el número de páginas a 2 podremos acceder a la segunda página del documento.











