# My Guide:

Aplicación 'fully responsive' en dos fases: Usuario y Cliente. 
El Usuario será capaz de filtrar el tipo de contenido (anuncios) que desea y consultar toda la información vertida en ellos.
El Cliente podrá crear, actualizar, mejorar y eliminar contenido/"space" (anuncios) en su dashboard. Para ello deberá crear su cuenta como "cliente", introduciendo sus credenciales, las cuales quedarán almacenadas en nuestra base de datos, para autorizar, mediante la creación de cookies, el acceso del "cliente" a la página. El cliente será la fuente del contenido de nuestra aplicación, llenando de texto, imágenes y ubicaciones su "space".

## Cómo usar "My guide":

1. Clone repository from my github:

$ https://github.com/DaniestBP/PFM.git

2. Crea el entorno virtial:   python3 -m venv .venv

3. Activa el venv: source venv/bin/activate

4. instala los requerimientos:

$ pip3 install -r Requirements.txt

5. Ejecuta el main.py: python3 main.py


### nota: Quería encriptar las passwords de los "clientes", por supuesto llevar el proyecto a Blueprints y subirlo a pythonanywhere, pero no calculé la carga de trabajo debidamente. Dejé estas 3 mejoras para el final pero no me ha sido posible cerrarlas. Aún así yo lo he disfrutado y quedé satisfecho. Espero que te guste. 
