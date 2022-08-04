# Adicionar Coverage

## Instalar dependencias

```zsh
$> poetry add -D coverage
```

| Nombre   | Descripción                                 |
| -------- | ------------------------------------------- |
| coverage | Medición de cobertura de código para Python |

## Configurar Coverage

Adicionar la siguiente configuración en el fichero `pyproject.toml`

```toml
[tool.coverage.paths]
source = ["src", "*/site-packages"]

[tool.coverage.run]
branch = true
source = ["src"]
omit = ["*/venv/*", "*/staticfiles/*", "*/media/*", "*/tests/*", "*/migrations/*", "*/__init__.py", "*/manage.py", "*/asgi.py*", "*/wsgi.py", "*/settings/*", "*/docs/*", "*/sphinx/*", "*/conf.py"]

[tool.coverage.report]
show_missing = true
fail_under = 85
exclude_lines = [
  "raise NotImplementedError",
  "def __repr__",
  "if __name__ == .__main__.:",
]
```

Adicionar en la configuración de `.pre-commit-config.yaml`

```yaml
- repo: local
  hooks:
    - id: coverage
      name: coverage
      entry: cd src && poetry run coverage run manage.py test -v 2 && poetry run coverage report -m
      language: system
      types: [python]
```

Ahora podemos ejecutar los siguientes comando

```zsh
# Ejecutar las pruebas y recolectar la información con coverage
$> poetry run coverage run src/manage.py test -v 2

# Generar reporte
$> poetry run coverage report -m

# Generar html
$> poetry run coverage html
```

## Bibliografía

- [Documentación](https://coverage.readthedocs.io/en/6.3.2/)
