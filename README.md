# practia_gaston_ferreyra
## SETUP ##
PYTHON: 3.13.7  
PIP: 25.2  
ALLURE : 2.36.0  
## Instalación  
Ir al directorio Local con bash  
bash: git clone git@github.com:kIOOnes/practia_gaston_ferreyra.git  
## Crear y activar entorno virtual  
En la raíz del repositorio:  
bash: python -m venv venv  
bash: venv\Scripts\activate    # Windows  
## Instalar dependencias  
pip install -r requirements.txt  
## Correr tests  
pytest -s --alluredir=allure-results  
## Visualizar reporte de Allure  
allure serve allure-results  
## Documentacion - Definiciones de Estructura y patrones. Convenciones.
S.O.L.I.D ----> Estructura usada en la codificación orientada a objetos.    
Page Objects -> Patron de diseño para ordenar localizadores, elementos de pantalla, acciones.    
A.A.A -------->(Arranque , Acción, Aserción)-> Patron de diseño para armar los test.  
PEP 8 --------> Nomenclatura del proyecto en python.  
Convencion de idioma: Ingles.  
## Documentacion - Estructura
├── pages/ ->Carpeta de hasta 3 niveles maximo. Agrupada por funcionalidad.  
├── tests/  
├── core/  #Aquí la codificación de los métodos que usaran los pages objects. 
├── reports/-> Aqui iran los reportes de Allure que se vayan generando  
├── venv/ -> entorno virtual.   
└── README.md  
Conftest.py          # Archivo de configuración del driver. Setup, Teardown, Screenshoot.


