# Billetera Virtual

## Descripción
Aplicación para gestionar una billetera virtual donde los usuarios pueden crear cuentas, consultar balances, hacer transacciones (depósitos/retiros) y ver su historial de transacciones.

## Tecnologías
- **Backend**: FastAPI
- **Frontend**: React
- **Base de Datos**: SQLite (para simplificar)
- **Dockerización**: Docker y Docker Compose

## Instrucciones

### Ejecutar Localmente
1. Clonar el repositorio.
2. Crear un entorno virtual e instalar las dependencias:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app.main:app --reload
