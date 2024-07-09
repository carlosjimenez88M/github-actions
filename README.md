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