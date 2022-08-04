# Adicionar EDITORCONFIG

## Información sobre editorconfig

EditorConfig ayuda a mantener estilos de código de manera consistente para múltiples desarrolladores que trabajan en el mismo proyecto, independientemente del IDE que utilicen.

El proyecto EditorConfig consiste en un **formato de archivo** que definen estilos de códigos y de una colección de **plugins de editor de texto** que proporcionan al editor la capacidad de leer el formato de archivo en cuestión para aplicar la configuración definida en este. Los archivos EditorConfig son legibles y funcionan bastante bien con sistemas de control de versiones.

Un archivo `.editorconfig` sirve para configurar los estilos de código que un editor de texto va a aplicar a la hora de aplicar "auto formato" o a la hora de sugerir cambios en el código (como por ejemplo la indentación, estilo de llaves, insertar nueva línea al final de cada archivo)

## Configurar editorconfig

Crear fichero `.editorconfig` en la raíz del proyecto

```
$> touch .editorconfig
```

Adicionar el siguiente contenido

```
# Check http://editorconfig.org for more information
# This is the main config file for this project:
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 2
trim_trailing_whitespace = true

[*.py]
indent_style = space
indent_size = 4

[*.pyi]
indent_style = space
indent_size = 4

[Makefile]
indent_style = tab

[*.md]
trim_trailing_whitespace = false
```

## Bibliografía

- [Web Oficial](https://editorconfig.org/)
