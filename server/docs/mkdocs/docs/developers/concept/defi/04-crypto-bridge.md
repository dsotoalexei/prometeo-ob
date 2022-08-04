# ¿Qué es un Crypto Bridge?

**Los Crypto Bridges o Bridges, son los responsables de que podamos interconectar las distintas blockchain que existen y poder interoperar entre ellas diversificando e incrementando con ello la usabilidad y alcance de las criptomonedas y los ecosistemas que se construyen a su alrededor.**

Un bridge o puente entre cadenas es un servicio (centralizado o descentralizado) que permite crear una conexión entre dos blockchains que normalmente no pueden comunicarse entre sí, para que de esta forma, puedan traspasarse tokens entre ellas.

Esta es una utilidad que se ha convertido en esencial gracias a la llegada de los servicios [**DeFi**](https://academy.bit2me.com/que-es-defi-o-finanzas-descentralizadas/), los cuales han llevado a la comunidad cripto a un salto enorme en el uso de la [**tecnología blockchain**](https://academy.bit2me.com/como-funciona-blockchain-cadena-de-bloques/) y los [**tokens**](https://academy.bit2me.com/que-es-un-token/) que hacen vida en las distintas cadenas de bloques capaces de brindar este tipo de servicios.

![crypto-bridge-bit2me-01](./images/crypto-bridge-bit2me-01.webp)

## ¿Cómo funciona un Bridge?

Un bridge se puede ver como un simple intercambiador de información entre blockchains. Es decir, la principal función de un bridge es permitir el intercambio bidireccional de información entre la blockchain A y la blockchain B, a través de un protocolo que permite esa conexión. Por supuesto esto es una forma fácil de ver cómo funciona un bridge, pero la idea básica es esa y tenerla muy en claro te servirá para entender exactamente cómo se realiza ese intercambio de información.

De hecho, la podemos resumir en cuatro pasos:

1. El bridge se ubica entre la cadena A y B, creando la estructura básica para su funcionamiento.
2. Si deseas pasar un token de A > B, te diriges al bridge, indicas la cantidad de tokens que deseas cambiar en A y proporcionas la dirección de destino en B.
3. Realizas el envío en A y el bridge te bloquea este saldo en un vault, y luego en B se acuña la cantidad exacta de tokens que son enviados a la dirección en B que has proporcionado.
4. Los tokens en A quedan bloqueados como garantía de los tokens en B y únicamente podrás recuperarlos haciendo el proceso contrario.

## Explicado en mayor detalle

Pongamos un ejemplo más práctico para avanzar un poco más en cómo funcionan estos bridges. Imagina que deseas pasar tokens 1.000 USDT desde la red Ethereum a la red Polygon. De forma directa, pese a que las direcciones de [**Ethereum**](https://academy.bit2me.com/que-es-ethereum-eth-criptomoneda/) y [**Polygon**](https://academy.bit2me.com/que-es-polygon-matic/) son idénticas, la realidad es que sus redes blockchain son distintas, por lo que no puedes pasar valor de forma directa entre ambas blockchain. Para ello, debes utilizar un bridge y este se encargará de completar ese proceso.

Dado que Etheruem y Polygon son idénticas a nivel de programación (están basadas en [**EVM**](https://academy.bit2me.com/que-es-ethereum-virtual-machine-evm/), usan Solidity, tienen el mismo modelo de direcciones, pero tienen distintos historiales y protocolo de consenso) crear un bridge es bastante fácil. Para ello, el bridge crea una serie de contratos (en Ethereum y Polygon) que permitirán que ambas redes puedan comunicarse con un lenguaje común a través de un oráculo blockchain. El trabajo del oráculo es dar información precisa a esos contratos de lo que sucede en la otra blockchain y viceversa. De esta forma, creamos el canal de comunicación bidireccional entre Ethereum y Polygon, en este punto la mitad del trabajo está hecho.

Ahora, para enviar ese USDT de ETH a Polygon, deberás interactuar con el bridge del lado de ETH. Este te pedirá dos cosas:

1. Una dirección de recepción para la red Polygon.
2. Que envíes los 1.000 USDT que tienes en ETH a un vault (también en ETH) que será controlado por un smart contract del bridge. Este paso suele ser transparente al usuario.

Al completar estos dos pasos y realizar el envío del lado de ETH, el bridge comienza su trabajo. Lo primero que pasa, es que el oráculo detecta el envío en ETH y lo reporta a los [smart contracts](https://academy.bit2me.com/que-son-los-smart-contracts/) del lado de Polygon. Con este reporte, va la cantidad de tokens cambiados y la dirección destino (la que has dado) para los mismos. Una vez que la operación en ETH se completa, entonces el oráculo informa de esto y los smart contracts del lado de Polygon, comienzan a generar los 1.000 USDT y se envían a la dirección proporcionada.

Los tokens generados del lado de Polygon son los mismos [**USDT**](https://academy.bit2me.com/que-es-usdt-theter-criptomoneda/), la misma cantidad y con el mismo valor, y esto es posible, porque el vault creado sirve de garantía de valor de esos nuevos tokens y estarán bloqueados hasta el momento en que hagas la operación contraria (pasar ese USDT de Polygon a ETH). El bloqueo evita que se generen tokens de la nada, a la vez que mantiene la seguridad y estabilidad económica entre las cadenas y el bridge.

Cuando haces el proceso contrario para recuperar tus USDT en ETH, el bridge toma tus USDT del lado de Polygon, los quema y, una vez quemados, se te entregan los USDT correspondientes del lado de Ethereum. Con eso, termina el trabajo del bridge entre ETH y Polygon.

![crypto-bridge-bit2me-02](./images/crypto-bridge-bit2me-02.webp)

### Tipos de Bridges

Los bridges pueden ser de dos tipos:

#### Centralizado

Un bridge centralizado es aquel cuya gestión recae en una entidad centralizada que toma y libera tokens entre las cadenas soportadas por dicha entidad. Básicamente, funciona como un exchange, solo que en lugar de intercambiar pares, solo se dedica a tomar un token y enviarte el mismo token en la red destino que elijas. Un ejemplo de este tipo de bridges es OKex Bridge.

#### Descentralizado

Un bridge descentralizado es aquel que es completamente controlado por smart contracts y donde el control de los fondos no recae en ninguna entidad central. Un ejemplo de este tipo de bridge es Multichain.

### Principales funciones de un bridge

Entre las principales funciones de los bridges podemos mencionar:

1. Habilitar la interoperaibilidad entre cadenas. De esa forma, los usuarios de Ethereum pueden tomar sus tokens y enviarlos a otras cadenas como BSC, sin tener que pasar por un exchange.
2. Permite que los usuarios puedan pasar entre Layer1 y Layer2. Por ejemplo, los usuarios de Ethereum pueden tomar sus tokens y llevarlos de Layer1 (la red Ethereum) a redes Layer2 como Polygon, Arbitrum, Optimism, xDai, entre otras.
3. Ayuda a minimizar los costes de operación, ya que le permite al usuario buscar redes con mejores comisiones para realizar sus operaciones.
4. Atraer valor de otras redes a redes con mejores oportunidades. Un buen ejemplo de esto es el paso de valor de BTC a Ethereum durante el criptoinvierno. El movimiento estuvo motivado en aprovechar el naciente ecosistema [DeFi](https://academy.bit2me.com/que-es-defi-o-finanzas-descentralizadas/) y generar ganancias en momentos en el BTC mantenía un bajo valor.

## Bibliografía

- https://academy.bit2me.com/que-es-un-crypto-bridge/
- https://launchpad.ripio.com/blog/bridges-para-pasar-tokens-nft-de-una-red-a-otra?utm_source=Mailup&utm_medium=Email&utm_campaign=AR_2022_ABR_CRIPTOFEED-1
- https://launchpad.ripio.com/blog/miniguia-de-staking-para-hacer-crecer-tus-criptomonedas
