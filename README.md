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