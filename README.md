# Para correr el proyecto:

```bash
#Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
venv\Scripts\activate  # En Windows
# source venv/bin/activate  # En macOS/Linux

# Instalar las dependencias
pip install -r requirements.txt

# Correr el proyecto
python manage.py runserver

# Docs: http://127.0.0.1:8000/docs/
```

# Para correr las pruebas unitarias:
```bash
# Solo es necesario ejecutar: 
python -m venv venv
# en la raíz del proyecto
```


# Para correr los tests de rendimiento:

```bash
# Instalar locust si no esta instalado
pip install locust

# Crear una variable de entorno con el host de la API
export API_HOST=http://localhost:8000

# Correr las pruebas de rendimiento
locust -f performance_test.py --headless \
                      --users 100 --spawn-rate 10 \
                      --run-time 1m --host $API_HOST
```

# Jenkins Pipeline Script

Este repositorio contiene el script de Jenkins para la ejecución de pruebas automatizadas en un proyecto Django, incluyendo análisis estático con SonarQube, pruebas de seguridad con ZAP, pruebas de rendimiento con Locust, y ejecución de pruebas unitarias con pytest.

El script completo se encuentra en el archivo `pipeline_script.txt`.

## Dependencias

Para ejecutar el pipeline, asegúrate de tener instaladas las siguientes dependencias y herramientas:

### Dependencias de Python

Este pipeline usa herramientas y dependencias de Python, las cuales deben ser instaladas en el entorno virtual.

1. **Newman**: Para ejecutar las colecciones de Postman desde la línea de comandos.
    ```bash
    pip install newman
    ```

2. **Locust**: Para ejecutar pruebas de rendimiento.
    ```bash
    pip install locust
    ```

3. **pytest**: Para ejecutar pruebas unitarias.
    ```bash
    pip install pytest
    ```

### Herramientas Externas

Este pipeline también requiere las siguientes herramientas externas para funcionar correctamente:

1. **SonarQube** (Análisis Estático):
    - Se necesita un servidor SonarQube en funcionamiento para ejecutar el análisis estático de código.
    - Se recomienda instalar la versión [SonarQube 9.9.7 LTA Community Edition](https://www.sonarsource.com/products/sonarqube/downloads/).
    - Para configurar SonarQube en tu máquina local, puedes seguir este [tutorial](https://soshace.com/2023/04/30/how-to-setup-sonarqube-in-a-project-on-local-machine/).

2. **ZAP** (Pruebas de Seguridad):
    - [Zed Attack Proxy (ZAP)](https://www.zaproxy.org/) es utilizado para realizar un análisis de seguridad en la aplicación Django. Asegúrate de tener instalada la versión compatible y configurada en el entorno.
    - El script espera la ruta del archivo `zap-2.15.0.jar`, el cual se usa para ejecutar un escaneo rápido de la aplicación.

3. **Java** (para ejecutar ZAP):
    - Asegúrate de tener instalada una versión compatible de Java. La versión recomendada para ZAP es Java 8 o superior.
    - Verifica que la variable de entorno `JAVA_HOME` esté correctamente configurada.

4. **Locust** (Pruebas de rendimiento):
    - Asegúrate de tener Locust instalado para realizar pruebas de rendimiento en la aplicación.

## Uso del Pipeline

El pipeline de Jenkins está estructurado en varias etapas, cada una con una función específica. A continuación se describen las etapas y su funcionamiento:

1. **Git Checkout**
   - Se realiza un `git checkout` del branch `develop` desde el repositorio de GitHub para obtener la última versión del código.

2. **SonarQube Static Analysis**
   - Ejecuta el análisis estático de código utilizando SonarQube, configurado para analizar el proyecto Python en el entorno.

3. **Setup and Install Dependencies**
   - Configura un entorno virtual de Python y instala las dependencias necesarias definidas en el archivo `requirements.txt`.

4. **Check Django Installation**
   - Verifica si Django está instalado correctamente en el entorno virtual.

5. **Start Django Server**
   - Inicia el servidor de Django para realizar las pruebas de funcionalidad.

6. **Wait for Django Server**
   - El pipeline espera a que el servidor de Django esté completamente disponible antes de continuar.

7. **Run Postman Tests**
   - Ejecuta pruebas de API utilizando Newman y colecciones de Postman para las funcionalidades de "Quejas", "Reclamos" y "Solicitudes".

8. **ZAP Security Scan**
   - Realiza un escaneo de seguridad en la aplicación utilizando ZAP (Zed Attack Proxy) y genera un reporte de seguridad.

9. **Performance Test and Archive Results**
   - Ejecuta pruebas de rendimiento utilizando Locust y guarda los resultados generados en archivos CSV.

10. **Stop Django Server**
   - Detiene el servidor de Django al finalizar las pruebas.

11. **Unit Tests**
   - Ejecuta las pruebas unitarias utilizando pytest.

12. **Post Actions**
   - Archiva los resultados de las pruebas y limpia el entorno de trabajo.

## Personalización del Pipeline

El script de Jenkins es altamente **personalizable** y permite ajustar diversas configuraciones para adaptarlo a tus necesidades específicas. A continuación se describe cómo personalizar algunas de las variables clave:
1. **SONAR_TOKEN**: Token de autenticación para SonarQube.
```groovy
SONAR_TOKEN = 'su_token_sonar'  // Se puede crear en Administration > Security > Users 
```
Este token es necesario para autenticar el análisis de código en SonarQube. Asegúrate de crear un token en la sección correspondiente de SonarQube y reemplazar el valor de la variable.

2. **ZAP_JAR_PATH**: Ruta del archivo JAR de ZAP (Zed Attack Proxy).
```groovy
ZAP_JAR_PATH = "${env.ZAP_HOME}\\zap-2.15.0.jar"  // Ruta configurable
```
Si ZAP está instalado en una ubicación diferente, asegúrate de actualizar esta ruta con la ubicación correcta del archivo zap-2.15.0.jar en tu sistema.

3. **ZAP_API_KEY**: Clave API de ZAP.
```groovy
ZAP_API_KEY = 'su_token_zap'  // Se puede encontrar en Tools > Options > API
```
Este es el token de API que ZAP usa para realizar el escaneo de seguridad. Puedes generar o copiar este token desde la interfaz de ZAP en la sección de opciones de API.

4. **PYTHON_PATH**: Ruta donde Python está instalado en tu sistema.
```groovy
PYTHON_PATH = "ruta_python"  // Ruta configurable para Python
```
Si tienes Python instalado en una ubicación diferente, modifica esta ruta para reflejar la instalación correcta en tu máquina.

5. **DJANGO_MANAGE_PATH**: Ruta al script de activación del entorno virtual de Django.
```groovy
DJANGO_MANAGE_PATH = "${env.PYTHON_PATH}\\Scripts\\activate.bat"
```
Asegúrate de que esta ruta apunte correctamente al archivo de activación del entorno virtual de Python que usas para tu proyecto Django.

### Notas de Personalización

    Si alguna de las rutas o variables de entorno no está configurada correctamente, el pipeline fallará en la etapa correspondiente, por lo que es importante verificar cada variable antes de ejecutar el pipeline.
    Este script está diseñado para ser compatible tanto con sistemas operativos Windows como Linux. Si estás utilizando un sistema operativo diferente, asegúrate de ajustar las rutas y configuraciones de acuerdo con el sistema operativo que estás usando.

## Conclusión

Este pipeline es completamente personalizable para que se ajuste a las necesidades específicas de tu proyecto Django. No dudes en modificar las rutas, los tokens y las configuraciones de herramientas según tu entorno y flujo de trabajo.
Archivos Generados

El pipeline genera los siguientes archivos durante su ejecución:

    Resultados de las pruebas de Postman en formato HTML.
    Reportes de seguridad generados por ZAP en formato HTML.
    Resultados de pruebas de rendimiento de Locust en formato CSV.
	Resultados de las pruebas de Locust en formato CSV.
