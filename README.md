# TerraLoop 2

TerraLoop 2 es una demostración de Human in the Loop usando micro:bit V2 y MakeCode Python.

La idea principal es que el sistema no tome por sí solo una decisión crítica.

## Funcionamiento

- Estado inicial: sistema normal
- Botón A o Shake: detecta una anomalía
- El sistema muestra EVENTO y REVISAR
- Botón B: una persona confirma la situación
- El sistema pasa a ROJO
- Botón B nuevamente: la alerta escala a CRITICO
- Se activa una señal sonora

## Concepto

TerraLoop combina:

sensor → detección → revisión humana → confirmación → escalamiento

El objetivo es mostrar cómo una persona puede permanecer dentro del proceso de decisión cuando existe una situación de riesgo.

## Tecnología

- micro:bit V2
- Microsoft MakeCode
- Python
- Sensores integrados
- Human in the Loop

## Versión

TerraLoop 2 continúa el desarrollo iniciado en TerraLoop 1, incorporando revisión humana y escalamiento de alertas.
> Open this page at [https://errorcheck.github.io/Terraloopv2sonia/](https://errorcheck.github.io/Terraloopv2sonia/)

## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/errorcheck/Terraloopv2sonia** and import

## Edit this project

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/errorcheck/Terraloopv2sonia** and click import

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>
