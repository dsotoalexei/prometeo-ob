# Instalar IPYTHON

**IPython** es un shell interactivo que añade funcionalidades extra al modo interactivo incluido con Python, como resaltado de líneas y errores mediante colores, una sintaxis adicional para el shell, autocompletado mediante tabulador de variables, módulos y atributos; entre otras funcionalidades.

## Instalar dependencias

```
$> poetry add -D ipython
```

| Nombre  | Descripción                                 |
| ------- | ------------------------------------------- |
| ipython | IPython: Computación interactiva productiva |

## Ejecutar shell con IPYTHON

```zsh
# Primero activamos el entorno virtual
$> source venv/bin/activate

# Segundo ejecutar shell django con ipython
(venv) $> poetry run python manage.py shell -i ipython
```

## Bibliografía

- [Web oficial](https://ipython.org/)
