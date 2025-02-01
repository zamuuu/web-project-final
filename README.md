# Web Blog

### Samuel Correa


## Description
Esta es una pagina web desarrolada en Django, con multiples funciones. Es una pagina de practica personal, implementando funciones como el registro de usuarios, el login, logout, edicion de perfil con imagen. Permite crear blogs con un imagenes, en ellos esta la implemetnacion de CKEditor, entre otros campos. Tambien permite eliminar los blogs, editar los blogs y ver un apartado de mas informacion, donde se muestra la informacion completa de paga atriculo (blog).


## Pasos para iniciar la web localmente

1. Tener instalado Git en tu maquina

2. Ejecutar en la consola ```Git clone https://github.com/zamuuu/web-project-final.git```

3. Ir a la carpeta del proyecto ```cd .../web-project-final/```

4. Instalar **virtualenv** para crear el entorno virtual donde se instalaran los paquetes y librerias necesarias ```pip install virtualenv```

4. Crear el entorno virtual (mejor practica que hacer la instalacion de los paquetes localmente) ```virtualenv <nombre del virtualenv>```

5. Activar el entorno virtual; En windows -> ```source venv/Scripts/activate``` || En linux/mac -> ```source venv/bin/activate```

6. Asegurandose de que el entorno virtual esta activado pasar a ejecutar tranquilamente ```pip install requirements.txt```

7. Ejecutar la migracion de los modelos de la DB ```python manage.py migrate```

8. Inicar la pagina para poder verla -> ```python manage.py runserver``` y hacer click en la IP proporcionada Y LISTO!

## Visual
### Un pequeño vistaso a la pagina de inicio
![image](https://user-images.githubusercontent.com/77868387/164942949-5c89dd8d-99db-4c35-ad7e-911e7c8aafbc.png)
### Video explicativo sobre la pagina
https://youtu.be/jhof4cHQjoI

## ⚠️ Advertencia de Seguridad  

Este proyecto está diseñado únicamente para ejecutarse de manera **local** y **no debe ser desplegado en internet!!**.  

⚠️ **Riesgos de seguridad si se sube a un servidor:**  
- La `SECRET_KEY` de Django está expuesta en el código, lo que puede comprometer la seguridad de sesiones y autenticaciones.  
- No se han aplicado configuraciones de seguridad necesarias para un entorno de producción.  

🔹 **Si deseas usar este código en un entorno público, es tu responsabilidad:**
🔹 No lo recomiendo ya que el riesgo es muy alto.
