# Metodología de trabajo Git Flow

Git Flow es una metodología de trabajo basada en [Git](https://git-scm.com/), creada por [Vincent Driessen](https://nvie.com/about/). Dicha metodología, define un modelo de ramificación estricto, diseñado alrededor del proyecto. Esto proporciona un marco robusto para gestionar proyectos más grandes.

![git-flow](./images/git-flow.png)

Git Flow es ideal para proyectos que tienen un ciclo de lanzamiento programado. Esta metodología de trabajo no agrega ningún concepto o comando nuevo más allá de los que se utilizan comúnmente cuando trabajas con Git (status, add, commit, checkout, merge, pull y push). Lo que sí hace, es asignar roles muy específicos a diferentes ramas y define cómo y cuándo deben interactuar.

Vamos a ver, las distintas ramas con las que vamos a trabajar, y para qué sirve cada una de ellas.

## Ramas principal y de desarrollo: `master` y `develop`

Cuando trabajas con Git Flow, en lugar de trabajar solamente con la rama `master` (cosa que es muy poco recomendable hacer), utilizas dos ramas para registrar el historial del proyecto: `master` y `develop`. Mientras que la primera de ellas contiene el historial de lanzamiento oficial, y por tanto, el código que está en producción, la rama `develop` sirve como una rama de integración de características.

## Ramas de características: `feature`

Este tipo de ramas, se utilizan para añadir nuevas características a tu proyecto, en futuras versiones. Estas ramas, dependerán de la rama `develop` y se creará una por cada característica que se quiera incorporar al proyecto.

Como la mejor forma de explicar las cosas, es con un ejemplo, imagina que tienes un blog en el que quieres incorporar una funcionalidad para compartir tus artículos en Redes Sociales. Para ello, sobre tu rama `develop`, ejecutarás el siguiente comando de Git:

```zsh
$> git checkout -b feature/share-social-network
```

Si te das cuenta, lo que he hecho ha sido crear una nueva rama, en la que he indicado que es una característica (`feature/` y una descripción de para qué va a servir (`share-social-network`). De esta forma, podremos identificarla rápidamente sin necesidad de examinar el código, además de facilitar el trabajo en equipo.

De ahora en adelante, todo el desarrollo que hagas para esta característica, lo harás sobre esta rama.

## Ramas de corrección de errores: `hotfix`

Mientras que las ramas `feature` las vas a utilizar para planificar nuevas características para tu proyecto (o mejora de las existentes), `hotfix` servirán para corregir errores que se hayan encontrado en el código (ya sean de rendimiento o de seguridad) y que no puedan esperar a una nueva versión para ser arreglados.

Ahora, imagina que tu blog cuenta con un formulario de contacto, a través del cual, tus lectores te envían dudas. Un día, por alguna razón, detectas que el formulario está fallando, así que tienes que ponerle solución rápidamente, antes de que tus seguidores piensen que no les contestas a sus mensajes y pasas de ellos. En esta ocasión, crearás una nueva rama, de esta forma:

```zsh
$> git checkout -b hotfix/contact-form-001
```

Vamos a ver con detenimiento el por qué de este nombre para la rama:

- En primer lugar, se trata de una rama de corrección de errores, por lo que debe llevar el prefijo `hotfix/` para que se identifique rápidamente su objetivo.
- A continuación, como se trata de una incidencia relacionada con el formulario de contacto, le añades el nombre de la característica que vas a arreglar (`contact-form`).
- Por último, como no sabes si en un futuro aparecerá otro error en el formulario de contacto, te sugiero que añadas un código. Así, la siguiente incidencia relacionada con esta característica será la `-002`, luego la `-003`,…

Una vez hayas reparado el fallo y testado para que no vuelva a ocurrir, lo tienes que incorporar a la rama `develop`. Para ello, tendrás que ejecutar la siguiente secuencia de comandos Git (dando por hecho que estas en la rama de la incidencia):

```zsh
$> git add [nombre-de-los-archivos]
$> git commit -m "hotfix contact form 001"
$> git checkout develop
$> git pull
$> git merge hotfix/contact-form-001
$> git push
```

Los comandos que acabas de ejecutar, sirven para (en el orden de ejecución):

- Indicar los archivos que vas a subir al repositorio y a desplegar.
- Comitear los archivos. Como puedes ver, en tu commit, pones el nombre de la rama para que en tu historial quede reflejado que se trata de la corrección de un error relacionado con el formulario de contacto.
- Cambiar a la rama `develop`.
- Incorporar posibles cambios que hayas podido hacer en la rama `develop` a la rama `hotfix/contact-form-001`. Esto, además de para tener todo el proyecto actualizado en tu rama de corrección de errores, te puede servir también para comprobar si uno de los archivos que has modificado para reparar la incidencia ha sido modificado en otra rama, y si sus cambios entran en conflicto con los tuyos.
- Incorporar los cambios hechos en el código para resolver la incidencia a la rama `develop`.
- Subir los cambios al repositorio.

Una vez tu código haya sido probado en `develop`, estará listo para sacarlo a producción, por lo que solo tendrás que incorporarlo a la rama `master`, con una secuencia similar a la anterior:

```zsh
$> git add [nombre-de-los-archivos]
$> git commit -m "hotfix contact form 001"
$> git checkout master
$> git pull
$> git merge develop
$> git push
$> git checkout develop
$> git merge master
```

Fíjate, que en esta secuencia, además, has vuelto a cambiar a la rama `develop`, ya que en la rama `master` nunca se trabaja, y has incorporado todos los posibles cambios que hubiese en la rama principal, para así tener tu rama de desarrollo actualizada.

Cuando tu código haya sido desplegado a producción y probado, solo te queda eliminar la rama que has estado utilizando, pues ya no la vas a necesitar más. Para ello, usa este comando, desde tu rama `develop`:

```zsh
$> git branch -D hotfix/contact-form-001
```

### Ramas de versiones y lanzamiento: `release`

En estas ramas es donde vas a preparar todo para el lanzamiento de una nueva versión para tu proyecto, o dicho de otra forma, donde incorporarás todas las características de las ramas `feature` y las terminarás de probar antes de sacarlas a producción.

Para ello, primero tienes que crear tu rama de lanzamiento, de la siguiente forma:

```zsh
$> git checkout -b release/v1-0-0
```

Como ya podrás imaginar, después de ver como se han formado los nombres de otras ramas, en esta ocasión estarás indicando que se trata de una rama de lanzamiento (`release/`) y que la versión que se va a lanzar va a ser la 1.0.0 (`v1-0-0`).

Siguiendo con nuestro ejemplo de la funcionalidad para compartir en Redes Sociales, y suponiendo que ya está probada, procederemos a incorporarla con la rama de lanzamiento, con una secuencia de comandos Git similar a la de la corrección de errores:

```zsh
$> git add [nombre-de-los-archivos]
$> git commit -m "feature share social network"
$> git checkout release/v1-0-0
$> git pull
$> git merge feature/share-social-network
$> git push
```

Cuando hayan sido incorporadas todas estas características a la rama de desarrollo, y tras comprobar que no hay ningún conflicto, deberás incorporar la rama `release/` a la rama `develop`:

```zsh
$> git add [nombre-de-los-archivos]
$> git commit -m "release v1.0.0"
$> git checkout develop
$> git merge release/v1-0-0
$> git push
```

Y de ahí, tras hacer nuevos tests, a la rama principal:

```zsh
$> git add [nombre-de-los-archivos]
$> git commit -m "release v1.0.0"
$> git checkout master
$> git pull
$> git merge develop
$> git push
$> git checkout dev
$> git merge master
```

Al igual que haces con las ramas `hotfix`, cuando despliegues tu código en producción y compruebes que todo funciona correctamente, solo te quedará eliminar la rama `release/v1-0-0`. Para ello, usa este comando, desde tu rama `develop`:

```zsh
$> git branch -D release/v1-0-0
```

## Conclusiones

Como has podido ver, la metodología Git Flow te permite dividir tu proyecto en varias ramas de desarrollo dedicadas a tareas muy específicas de tu proyecto.

A lo largo de este artículo, has podido ver:

- Qué es la metodología Git Flow
- Tipos de ramas con las que se trabaja
  - Principal (`master`).
  - Desarrollo (`develop`).
  - Características (`feature`).
  - Corrección de errores (`hotfix`).
  - Versión y lanzamiento (`release`).

Es cierto, que esta es una adaptación de la metodología real, en la que se utilizan algunos tipos de ramas más, como por ejemplo, la de correción de errores antes de la salida a producción (`bugfix`). También utiliza una variación de los comandos básicos de Git. Por aquí te dejo un [enlace al artículo donde el propio inventor de Git Flow te explica la metodología](https://nvie.com/posts/a-successful-git-branching-model/), tal y como él la diseñó, por si quieres echarle un vistazo y ampliar la información.

## Bibliografía

- https://www.juanmacivico87.com/metodologia-trabajo-git-flow/
