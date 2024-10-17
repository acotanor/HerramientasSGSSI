# HerramientasSGSSI

Este repositorio contiene las herramientas desarrolladas en los laboratorios de la asignatura Sistemas de Gestión de Seguridad de Sistemas de la Información para su uso en los exámenes prácticos.

Las herramientas se encuentran en la carpeta HerramientasSGSSI/Herramientas/, mientras que los archivos de la carpeta principal son wrappers sencillos escritos en bash que nos ahorran la escritura de "python3" al principio y el ".py" al final del nombre de cada comando para agilizar su uso.

Todas las herramientas están documentadas y poseen explicaciones que se muestran con cualquiera de los argumentos (-h, --h, -help, --help).

# Descripción corta de cada herramienta:

## Criptfrec:

Abre un entorno en la terminal con un texto cifrado (primer argumento), el progreso de descifrado (se guarda el resultado en el segundo argumento), recomendaciones de cambios de letras y un registro de los cambios efectuados.

Ejemplo de uso:

```sh
./criptfrec "/ejemplo/mensaje_cifrado.txt" "/ejemplo/output_descifrado.txt"
```

## Steganos:

Dados un directorio con imágenes, un hash a comparar y la contraseña de stegosuite, comprueba que imagen del directorio contiene el hash dado y utiliza stegosuite para desvelar el mensaje oculto de dicha imagen.

```sh
./steganos "/ejemplo/imágenes" "250ac5b66818a143eb9e9e78551b9436" "Contraseña"
```

## 