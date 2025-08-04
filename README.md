🎯 Objetivo:

Desarrollar un sistema de **gestión de inventarios** para una cafetería 🍔 en Campuslands, que permita:

1. Registrar, gestionar y actualizar **ingredientes**, **categorías de hamburguesas**, **chefs** y **hamburguesas**.
2. Generar **reportes** útiles para la operación eficiente del negocio.

---

🍅 **Módulo de Ingredientes**:

* **Operaciones CRUD** (Crear, Leer, Actualizar, Eliminar) sobre los ingredientes (nombre, descripción, precio, stock).
* **Seguimiento** de ingredientes utilizados para evitar desperdicio.

🍔 **Módulo de Categorías**:

 **Operaciones CRUD** sobre las categorías de hamburguesas (nombre, descripción).

👨‍🍳 **Módulo de Chefs**:

* **Operaciones CRUD** sobre los chefs (nombre, especialidad).

🍴 **Módulo de Hamburguesas**:

* **Operaciones CRUD** sobre las hamburguesas (nombre, categoría, ingredientes, precio, chef).

📊 **Módulo de Reportes**:

* Consultas para obtener información sobre:

  1. Ingredientes con stock menor a **400** unidades.
  2. Hamburguesas de la categoría "**Vegetariana**".
  3. Chefs especializados en **“Carnes”**.
  4. Aumento del precio de todos los ingredientes en **1.5**.
  5. Hamburguesas preparadas por un chef específico (p.ej. **ChefB**).
  6. Información de todas las **categorías**.
  7. Eliminar ingredientes con **stock 0**.
  8. Modificaciones en hamburguesas (agregar ingredientes, cambios de especialidades de chefs).
  9. Listar hamburguesas en orden ascendente por **precio**.
  10. Buscar hamburguesas que **no contienen** ciertos ingredientes.
  11. **Incrementar stock** de un ingrediente (p.ej. **Pan**).
  12. Eliminar hamburguesas con **menos de 5 ingredientes**.

---

⚙️ **Requisitos del Sistema**:

1. **JSON**: Los datos de ingredientes, categorías, hamburguesas y chefs deben estar almacenados en **archivos JSON**.
2. **Python**: El sistema debe estar implementado en **Python**, con el código modularizado y operaciones CRUD efectivas para manejar los datos.

   * **Código modularizado**.
   * **Archivos JSON** que contengan la base de datos.


📂 **Archivos JSON Ejemplares**:

* **Ingredientes**: Lista de ingredientes con su nombre, descripción, precio y stock.
* **Categorías**: Lista de categorías de hamburguesas (Clásica, Vegetariana, Gourmet).
* **Hamburguesas**: Lista de hamburguesas con sus respectivos ingredientes, precios y chefs responsables.
* **Chefs**: Información sobre los chefs y su especialidad.



¿Necesitas ayuda con la **estructura de archivos**, el **diseño de funciones**, o el **código** para alguna de las funcionalidades? ¡Estoy aquí para ayudarte! 😊
