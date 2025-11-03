# server/api.py – GOVAI FastAPI Backend
from fastapi import FastAPI
from pydantic import BaseModel
from brain.user_profiler import UserProfiler
from brain.email_assistant import EmailAssistant
from connectors.system_connector import SystemConnector
from security.compliance import ComplianceChecker

app = FastAPI(title="GovAI Enterprise API", version="1.0")

profiler = UserProfiler()
email_ai = EmailAssistant()
connector = SystemConnector()
compliance = ComplianceChecker()

class UserRequest(BaseModel):
    user_id: str
    role: str
    department: str
    challenges: list

class EmailRequest(BaseModel):
    subject: str
    body: str
    user_role: str

@app.get("/")
def root():
    return {"message": "🚀 GOVAI Enterprise API is live!"}

@app.post("/create-profile/")
def create_profile(req: UserRequest):
    profile = profiler.create_government_profile(
        req.user_id, req.role, req.department, req.challenges
    )
    return {"status": "success", "profile": profile}

@app.post("/analyze-email/")
def analyze_email(req: EmailRequest):
    analysis = email_ai.analyze_government_email(
        req.subject, req.body, req.user_role
    )
    return {"status": "success", "analysis": analysis}

@app.get("/check-compliance/{operation}/{role}")
def check_compliance(operation: str, role: str):
    result = compliance.check_operation(operation, role)
    return {"status": "success", "compliance_report": result}

@app.post("/connect-system/")
def connect_system(system_name: str, system_type: str, api_key: str):
    connection = connector.connect_government_system(system_name, system_type, api_key)
    return {"status": "success", "message": connection}
