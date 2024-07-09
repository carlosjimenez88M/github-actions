# Github Actions 

## Qué es Github ?

Es un entorno colaborativo para desarrollar código



### Configuración Inicial
- **Configurar nombre de usuario:**
  ```bash
  git config --global user.name "Tu Nombre"
  ```
- **Configurar correo electrónico:**
  ```bash
  git config --global user.email "tuemail@example.com"
  ```

### Crear y Clonar Repositorios
- **Crear un nuevo repositorio:**
  ```bash
  git init
  ```
- **Clonar un repositorio existente:**
  ```bash
  git clone https://github.com/usuario/repositorio.git
  ```

### Trabajando con Archivos
- **Añadir archivos al área de preparación (staging area):**
  ```bash
  git add nombre_del_archivo
  ```
  - Para añadir todos los archivos modificados:
    ```bash
    git add .
    ```

- **Confirmar los cambios (commit):**
  ```bash
  git commit -m "Mensaje descriptivo del cambio"
  ```

### Trabajando con Ramas
- **Crear una nueva rama:**
  ```bash
  git branch nombre_de_la_rama
  ```
- **Cambiar a una rama existente:**
  ```bash
  git checkout nombre_de_la_rama
  ```
- **Crear y cambiar a una nueva rama:**
  ```bash
  git checkout -b nombre_de_la_nueva_rama
  ```

### Sincronización con GitHub
- **Verificar el estado de los archivos:**
  ```bash
  git status
  ```
- **Verificar los cambios:**
  ```bash
  git diff
  ```
- **Enviar cambios al repositorio remoto (push):**
  ```bash
  git push origin nombre_de_la_rama
  ```
- **Obtener cambios del repositorio remoto (pull):**
  ```bash
  git pull origin nombre_de_la_rama
  ```

### Colaboración
- **Fusionar (merge) una rama a la rama actual:**
  ```bash
  git merge nombre_de_la_rama
  ```
- **Resolver conflictos de fusión:**
  - Edita los archivos con conflictos.
  - Añade los archivos resueltos:
    ```bash
    git add nombre_del_archivo_resuelto
    ```
  - Confirma la resolución del conflicto:
    ```bash
    git commit -m "Resuelto conflicto en nombre_del_archivo"
    ```

### Trabajo Remoto
- **Agregar un repositorio remoto:**
  ```bash
  git remote add origin https://github.com/usuario/repositorio.git
  ```
- **Verificar repositorios remotos:**
  ```bash
  git remote -v
  ```
- **Eliminar un repositorio remoto:**
  ```bash
  git remote remove nombre_del_remoto
  ```

### Buenas Prácticas
- **Actualizar la rama principal antes de trabajar en una nueva característica:**
  ```bash
  git pull origin main
  ```
- **Trabajar en ramas para nuevas características o correcciones:**
  - Crea una nueva rama para cada característica o corrección:
    ```bash
    git checkout -b nombre_de_la_caracteristica
    ```
- **Hacer commits frecuentes con mensajes claros:**
  - Es importante realizar commits frecuentemente para mantener un historial claro y detallado.

- **Sincronizar regularmente con el repositorio remoto:**
  ```bash
  git fetch origin
  git pull origin main
  ```

Estos comandos y prácticas deberían ayudarte a comenzar a colaborar efectivamente en proyectos usando Git y GitHub.

### ¿Qué es GitHub Actions?
- **GitHub Actions** es una herramienta de automatización dentro de GitHub.
- Permite automatizar flujos de trabajo de desarrollo de software directamente en tu repositorio de GitHub.
- Puedes utilizar GitHub Actions para compilar, probar, empaquetar, lanzar, o desplegar cualquier proyecto en GitHub.

### Principales conceptos de GitHub Actions:
- **Workflows (Flujos de trabajo):**
  - Son configuraciones de automatización definidas en archivos YAML dentro del directorio `.github/workflows` de tu repositorio.
  - Se pueden ejecutar en respuesta a eventos específicos como `push`, `pull request`, o en horarios programados.

- **Events (Eventos):**
  - Son las acciones que desencadenan la ejecución de un flujo de trabajo.
  - Ejemplos de eventos son `push`, `pull_request`, `issue`, `schedule` (cron jobs).

- **Jobs (Tareas):**
  - Son unidades de trabajo dentro de un flujo de trabajo.
  - Un flujo de trabajo puede tener múltiples tareas que se ejecutan en paralelo o en secuencia.

- **Steps (Pasos):**
  - Son los comandos individuales dentro de una tarea.
  - Cada paso ejecuta una acción específica, como ejecutar un script o instalar dependencias.

- **Actions (Acciones):**
  - Son comandos reutilizables que se pueden ejecutar en un paso de un trabajo.
  - Puedes usar acciones predefinidas desde el Marketplace de GitHub o crear las tuyas propias.

### Principales cosas a tener en cuenta al usar GitHub Actions:
- **Archivos de configuración:**
  - Los flujos de trabajo se definen en archivos YAML dentro del directorio `.github/workflows`.
  - Asegúrate de que los nombres de los archivos YAML sean descriptivos de los flujos de trabajo que representan.

- **Permisos:**
  - Configura correctamente los permisos de acceso para que GitHub Actions pueda interactuar con tu repositorio y otros servicios.
  
- **Variables de entorno y secretos:**
  - Utiliza `secrets` de GitHub para manejar información sensible, como tokens de acceso o claves API.
  - Configura variables de entorno para parametrizar tus flujos de trabajo.

- **Matrix builds:**
  - Usa matrices para ejecutar trabajos en diferentes combinaciones de variables, por ejemplo, diferentes versiones de lenguajes de programación o sistemas operativos.

- **Caching:**
  - Implementa caché para acelerar tus flujos de trabajo guardando dependencias o archivos de compilación entre ejecuciones.

### ¿Qué es CI/CD?
- **CI (Continuous Integration) - Integración Continua:**
  - Práctica de automatizar la integración del código de varios desarrolladores en un repositorio compartido varias veces al día.
  - Cada integración es verificada mediante la ejecución automática de pruebas para detectar errores rápidamente.

- **CD (Continuous Delivery/Deployment) - Entrega/Despliegue Continuo:**
  - **Continuous Delivery (Entrega Continua):**
    - Extiende la CI asegurando que el código que pasa las pruebas esté siempre en un estado desplegable.
    - Aunque el despliegue en producción no es automático, el equipo puede desplegar en cualquier momento con un clic.
  - **Continuous Deployment (Despliegue Continuo):**
    - Lleva la entrega continua un paso más allá al automatizar el despliegue del código en producción después de pasar las pruebas.

### Beneficios de CI/CD:
- **Automatización:**
  - Reduce la carga de tareas repetitivas y aumenta la eficiencia.
  
- **Detección temprana de errores:**
  - Detecta y corrige errores rápidamente al integrar y probar frecuentemente.
  
- **Entrega rápida:**
  - Acelera el proceso de entrega de nuevas funcionalidades a los usuarios.

- **Mejora de la calidad:**
  - Asegura que cada cambio pase por un conjunto riguroso de pruebas antes de ser desplegado.

### Pasos básicos para implementar CI/CD con GitHub Actions:
1. **Crear un archivo de flujo de trabajo YAML en `.github/workflows`:**
   ```yaml
   name: CI

   on: [push, pull_request]

   jobs:
     build:
       runs-on: ubuntu-latest

       steps:
         - uses: actions/checkout@v2
         - name: Set up Node.js
           uses: actions/setup-node@v2
           with:
             node-version: '14'
         - run: npm install
         - run: npm test
   ```

2. **Configurar eventos de activación:**
   - Define cuándo se debe ejecutar el flujo de trabajo (por ejemplo, `push`, `pull_request`, `schedule`).

3. **Definir trabajos y pasos:**
   - Divide tu flujo de trabajo en tareas y pasos claros, indicando qué acciones deben realizarse.

4. **Agregar acciones y comandos:**
   - Utiliza acciones del Marketplace o crea las tuyas propias para realizar tareas específicas.

5. **Probar y ajustar:**
   - Monitorea la ejecución de tus flujos de trabajo, revisa los logs y ajusta según sea necesario.

### Steps en Github actions

* Workflow: 
  * Proceoso que ejecuta uno o más jobs
  * recuerde que este se configura en ```.github/workflows```
* job : Pasos que corren en un servidor
* step: Comando o scr que se ejecuta
* Action: Acciones personaliozadas que realizan tareas que tienen continuidad y repetición


### Evento 
Es una acción que se va arrojar en github action

### Runner

Un servidor donde corren los pasos que se definen en ci-cd




### Eventos o Triggers

* **push**
* **pull_request**
* **issues**
* **issue_comment**
* **workflow_dispatch**
* **schedule**

### Explicación de los eventos

#### **push**
El evento `push` se desencadena cada vez que se realiza un `push` a la rama especificada del repositorio.

```yaml
on:
  push:
    branches:
      - 'main'       # El flujo de trabajo se ejecutará solo cuando se haga push a la rama 'main'
    paths:
      - '**.py'      # El flujo de trabajo se ejecutará solo cuando se modifiquen archivos con la extensión .py
```

#### **pull_request**
El evento `pull_request` se desencadena cada vez que se abre o etiqueta una solicitud de extracción (PR) hacia la rama especificada del repositorio.

```yaml
on:
  pull_request:
    types:
      - [opened, labeled]  # El flujo de trabajo se ejecutará cuando se abra o etiquete una PR
    branches:
      - 'main'             # La PR debe apuntar a la rama 'main'
    paths:
      - '**.py'            # El flujo de trabajo se ejecutará solo si la PR modifica archivos con la extensión .py
```

#### **issues**
El evento `issues` se desencadena cada vez que se crea o modifica un problema (issue) en el repositorio.

```yaml
on:
  issues:
    types:
      - [opened, edited]  # El flujo de trabajo se ejecutará cuando se abra o edite un issue
```

#### **issue_comment**
El evento `issue_comment` se desencadena cada vez que se añade un comentario a un problema (issue) o una solicitud de extracción (PR).

```yaml
on:
  issue_comment:
    types:
      - created           # El flujo de trabajo se ejecutará cuando se cree un nuevo comentario
```

#### **workflow_dispatch**
El evento `workflow_dispatch` permite que un flujo de trabajo sea iniciado manualmente desde la interfaz de GitHub.

```yaml
on:
  workflow_dispatch:
    inputs:
      logLevel:
        description: 'Log level'
        required: true
        default: 'warning'
```

#### **schedule**
El evento `schedule` permite que un flujo de trabajo sea ejecutado en horarios programados utilizando cron syntax.

```yaml
on:
  schedule:
    - cron: '0 0 * * *'    # El flujo de trabajo se ejecutará todos los días a la medianoche UTC
```

### Ejemplo Completo de Archivo YAML

Combina múltiples eventos en un solo flujo de trabajo para mayor flexibilidad:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - 'main'
    paths:
      - '**.py'
  pull_request:
    types:
      - [opened, labeled]
    branches:
      - 'main'
    paths:
      - '**.py'
  issues:
    types:
      - [opened, edited]
  issue_comment:
    types:
      - created
  workflow_dispatch:
  schedule:
    - cron: '0 0 * * *'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: python -m unittest discover -s tests
```

### Explicación del Ejemplo Completo

- **push**: Ejecuta el flujo de trabajo cuando se hace push a la rama `main` y se modifican archivos `.py`.
- **pull_request**: Ejecuta el flujo de trabajo cuando se abre o etiqueta una PR hacia la rama `main` y se modifican archivos `.py`.
- **issues**: Ejecuta el flujo de trabajo cuando se abre o edita un issue.
- **issue_comment**: Ejecuta el flujo de trabajo cuando se crea un nuevo comentario en un issue o PR.
- **workflow_dispatch**: Permite iniciar el flujo de trabajo manualmente desde la interfaz de GitHub.
- **schedule**: Ejecuta el flujo de trabajo todos los días a la medianoche UTC.

### Jobs y Steps

- **jobs**: Define los trabajos que se ejecutarán. En este caso, solo hay un trabajo llamado `build`.
- **steps**: Define los pasos dentro del trabajo `build`.
  - **Checkout code**: Clona el repositorio.
  - **Set up Python**: Configura Python 3.8.
  - **Install dependencies**: Instala las dependencias del proyecto desde el archivo `requirements.txt`.
  - **Run tests**: Ejecuta las pruebas unitarias en el directorio `tests`.




### ¿Qué es Cron?
Cron es un sistema de programación de tareas que permite ejecutar comandos o scripts en momentos específicos, de manera repetitiva. Utiliza una sintaxis específica para definir la frecuencia de ejecución.

### Sintaxis de Cron
La sintaxis de cron está compuesta por cinco campos que representan diferentes unidades de tiempo:
1. **Minuto** (0 - 59)
2. **Hora** (0 - 23)
3. **Día del mes** (1 - 31)
4. **Mes** (1 - 12)
5. **Día de la semana** (0 - 7) (0 y 7 representan el domingo)

Cada campo puede tener valores específicos, rangos de valores, listas de valores separados por comas, o valores de paso. Aquí tienes algunos ejemplos de cron:

- `* * * * *`: Se ejecuta cada minuto.
- `0 * * * *`: Se ejecuta cada hora (a la hora en punto).
- `0 0 * * *`: Se ejecuta diariamente a medianoche.
- `0 0 1 * *`: Se ejecuta mensualmente, el primer día del mes a medianoche.
- `0 0 * * 0`: Se ejecuta semanalmente, todos los domingos a medianoche.

### Usar Cron en GitHub Actions
Para utilizar cron en GitHub Actions, debes definir el evento `schedule` en tu archivo YAML con la expresión cron deseada.

### Ejemplo Simple
Vamos a ver cómo configurar un flujo de trabajo para que se ejecute diariamente a medianoche:

```yaml
name: Scheduled CI

on:
  schedule:
    - cron: '0 0 * * *'  # Se ejecuta todos los días a medianoche UTC

jobs:
  scheduled-job:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: python -m unittest discover -s tests
```

### Explicación del Ejemplo
- **on:**
  - **schedule:** Define que el flujo de trabajo se ejecutará en un horario programado.
  - **cron:** `0 0 * * *` indica que el flujo de trabajo se ejecutará todos los días a medianoche UTC.

- **jobs:** Define un trabajo llamado `scheduled-job` que se ejecuta en una máquina `ubuntu-latest`.

- **steps:** Define los pasos que se ejecutarán dentro del trabajo `scheduled-job`:
  - **Checkout code:** Clona el repositorio.
  - **Set up Python:** Configura Python 3.8.
  - **Install dependencies:** Instala las dependencias del proyecto.
  - **Run tests:** Ejecuta las pruebas unitarias.

### Más Ejemplos de Cron
- Ejecutar cada hora:
  ```yaml
  on:
    schedule:
      - cron: '0 * * * *'
  ```
- Ejecutar todos los lunes a las 8 AM:
  ```yaml
  on:
    schedule:
      - cron: '0 8 * * 1'
  ```
- Ejecutar el primer día de cada mes a las 6 AM:
  ```yaml
  on:
    schedule:
      - cron: '0 6 1 * *'
  ```

### Notas Importantes
- **UTC:** La programación cron en GitHub Actions utiliza el Tiempo Universal Coordinado (UTC). Asegúrate de convertir tu horario local a UTC si es necesario.
- **Pruebas:** Puedes usar herramientas como [crontab.guru](https://crontab.guru/) para verificar y probar tus expresiones cron.

Usar cron en GitHub Actions te permite automatizar tareas que necesitan ejecutarse en horarios específicos, lo que es útil para tareas de mantenimiento, actualizaciones, backups, y mucho más.
