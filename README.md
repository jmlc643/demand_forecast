# Demand Forecasting API

Una API REST desarrollada con FastAPI para predecir la cantidad de ventas de productos basándose en características específicas como precio unitario, descuento, categoría del producto, método de pago, canal de ventas y fecha de facturación.

## 🚀 Características

- **API RESTful** construida con FastAPI
- **Predicción de demanda** usando Machine Learning
- **Validación automática** de datos de entrada con Pydantic
- **Documentación interactiva** automática con Swagger UI
- **Modelo pre-entrenado** para predicciones rápidas

## 📋 Requisitos

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic
- Scikit-learn
- Pandas
- Numpy

## 🛠️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/jmlc643/demand_forecast.git
cd proyecto-prediccion-ventas
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
python back.py
```

La API estará disponible en: `http://127.0.0.1:8000`

## 📊 Modelo de Datos

El modelo acepta los siguientes parámetros de entrada:

```python
class PredictionInput(BaseModel):
    UnitPrice: float          # Precio unitario del producto
    Discount: float           # Descuento aplicado (0.0 - 1.0)
    ShippingCost: float       # Costo de envío
    Category: str             # Categoría del producto
    PaymentMethod: str        # Método de pago
    SalesChannel: str         # Canal de ventas
    InvoiceDate: str          # Fecha de facturación
```

## 🔧 Endpoints

### 1. Página Principal
- **URL**: `/`
- **Método**: GET
- **Descripción**: Mensaje de bienvenida de la API

### 2. Predicción de Demanda
- **URL**: `/predict`
- **Método**: POST
- **Descripción**: Predice la cantidad de ventas basándose en los datos proporcionados

## 📝 Ejemplo de Uso

### Realizar una Predicción

**Endpoint**: `POST /predict`

**Cuerpo de la petición**:
```json
{
  "UnitPrice": 55.0,
  "Discount": 0.10,
  "ShippingCost": 12.5,
  "Category": "Electronics",
  "PaymentMethod": "Credit Card",
  "SalesChannel": "Online",
  "InvoiceDate": "2020-05-11 14:00"
}
```

**Respuesta esperada**:
```json
{
  "predicted_quantity": 24
}
```

### Ejemplo con cURL

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "UnitPrice": 55.0,
       "Discount": 0.10,
       "ShippingCost": 12.5,
       "Category": "Electronics",
       "PaymentMethod": "Credit Card",
       "SalesChannel": "Online",
       "InvoiceDate": "2020-05-11 14:00"
     }'
```

### Ejemplo con Python

```python
import requests
import json

url = "http://localhost:8000/predict"
data = {
    "UnitPrice": 55.0,
    "Discount": 0.10,
    "ShippingCost": 12.5,
    "Category": "Electronics",
    "PaymentMethod": "Credit Card",
    "SalesChannel": "Online",
    "InvoiceDate": "2020-05-11 14:00"
}

response = requests.post(url, json=data)
print(response.json())
```

## 📖 Documentación de la API

Una vez que la aplicación esté ejecutándose, puedes acceder a la documentación interactiva:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🐳 Docker

Para ejecutar la aplicación usando Docker:

```bash
# Construir la imagen
docker build -t demand-forecast-api .

# Ejecutar el contenedor
docker run -p 8000:8000 demand-forecast-api
```

## 📁 Estructura del Proyecto

```
├── back.py                 # Aplicación principal FastAPI
├── model.py               # Modelo de Machine Learning
├── requirements.txt       # Dependencias del proyecto
├── Dockerfile            # Configuración de Docker
├── README.md             # Documentación del proyecto
├── MODELO_6.0.ipynb      # Notebook de desarrollo del modelo
└── models/               # Modelos entrenados
    ├── features.pkl      # Features del modelo
    └── modelo_demanda.pkl # Modelo serializado
```

## 🧪 Testing

Para probar la API puedes usar herramientas como:

- **Postman**: Importa la colección desde `http://localhost:8000/openapi.json`
- **Thunder Client** (extensión de VS Code)
- **cURL** (ejemplos proporcionados arriba)
- **Python requests** (ejemplo proporcionado arriba)

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📜 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Autores

- Tu nombre - [@tu-usuario](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- UPAO - Universidad Privada Antenor Orrego
- Curso de Machine Learning - Ciclo IX