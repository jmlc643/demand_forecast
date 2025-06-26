import joblib
import pandas as pd
from typing import Dict, Any

class DemandForecastModel:
    def __init__(self):
        """Inicializa el modelo y las características necesarias"""
        try:
            self.model = joblib.load('./models/modelo_demanda.pkl')
            self.features = joblib.load('./models/features.pkl')
            self.categorical_cols = [
                col for col in self.features 
                if col in ['Category', 'PaymentMethod', 'SalesChannel']
            ]
        except FileNotFoundError:
            raise Exception("No se encontraron los archivos del modelo. Asegúrate de haber ejecutado el entrenamiento primero.")

    def _preprocess_input(self, data: Dict[str, Any]) -> pd.DataFrame:
        """Preprocesa los datos de entrada para hacer predicciones"""
        df = pd.DataFrame([data])
        
        for col in ['Country', 'PaymentMethod', 'Category', 'WarehouseLocation']:
            if col in df.columns:
                df[col] = df[col].fillna('Unknown')
        
        df['EffectivePrice'] = df['UnitPrice'] * (1 - df['Discount'])
        df['PriceWithShipping'] = df['EffectivePrice'] + df['ShippingCost']
        
        if 'InvoiceDate' in df.columns:
            df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
            df['IsWeekend'] = (df['InvoiceDate'].dt.dayofweek >= 5).astype(int)
            df = df.drop(columns=['InvoiceDate'])
        else:
            df['IsWeekend'] = 0
            
        for col in self.categorical_cols:
            if col in df.columns:
                df[col], _ = pd.factorize(df[col])
        
        for col in self.features:
            if col not in df.columns:
                df[col] = 0
                
        return df[self.features]

    def predict(self, data: Dict[str, Any]) -> Dict[str, float]:
        """Realiza una predicción a partir de datos de entrada"""
        try:
            processed_data = self._preprocess_input(data)
            
            prediction = self.model.predict(processed_data)[0]
            
            return {
                "predicted_quantity": int(prediction)
            }
        except Exception as e:
            return {"error": str(e)}