# api/schemas.py

from pydantic import BaseModel


class CustomerInput(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float

    gender_Male: int
    SeniorCitizen: int
    Partner_Yes: int
    Dependents_Yes: int

    PhoneService_Yes: int
    MultipleLines_Yes: int
    InternetService_Fiber_optic: int
    OnlineSecurity_Yes: int
    OnlineBackup_Yes: int
    DeviceProtection_Yes: int
    TechSupport_Yes: int
    StreamingTV_Yes: int
    StreamingMovies_Yes: int

    Contract_One_year: int
    Contract_Two_year: int
    PaperlessBilling_Yes: int
    PaymentMethod_Electronic_check: int
