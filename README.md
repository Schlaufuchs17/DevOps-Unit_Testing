# DevOps---Unit-Testing-Tarea-2-

Se pide al alumno extender la aplicación web creada en el anterior ejercicio:

    Se añadirán tests de tipo unitario que nos ayuden a verificar el funcionamiento de nuestros endpoints.

    Se añadirá un script que facilite la provisión del servicio, cuya invocación permite comenzar a hacer peticiones al mismo.

Para saber si nuestra batería de tests es suficiente, se utilizan herramientas de medición de cobertura, que miden qué porcentaje de nuestro código se recorre con los tests que ejecutamos.
Herramientas de medición de cobertura

Se exponen ejemplos de librerías o utilidades comunes de medición de la cobertura de testing (entre otras características) en los tres lenguajes que utilizamos en el curso.

Si el alumno está familiarizado con cualquier otra herramienta que provea la misma funcionalidad, es totalmente válido su uso, siempre y cuando esté documentado cómo conseguir un reporte.
Python

Existe la librería coverage (Enlaces a un sitio externo.), muy sencilla de usar y que funciona con los runners habituales. Un ejemplo con 'py.test':

Java

Se puede emplear JaCoCo (Enlaces a un sitio externo.), fácilmente configurable en Maven y Gradle, que permite elaborar reportes en formato HTML, al igual que la herramienta anterior.
