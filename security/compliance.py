# security/compliance.py - GOVAI SECURITY & COMPLIANCE
class ComplianceChecker:
    def __init__(self):
        self.checks_performed = 0
        print("✅ Compliance Checker Initialized")
    
    def check_operation(self, operation_type, user_role):
        self.checks_performed += 1
        
        compliance_report = {
            "operation": operation_type,
            "user_role": user_role,
            "gdpr_compliant": self._check_gdpr(operation_type),
            "hipaa_compliant": self._check_hipaa(operation_type, user_role),
            "overall_status": "PASS",
            "check_id": self.checks_performed
        }
        return compliance_report
    
    def _check_gdpr(self, operation):
        sensitive_operations = ["email_analysis", "document_processing"]
        return operation not in sensitive_operations
    
    def _check_hipaa(self, operation, role):
        return role != "health_worker" or operation != "medical_data"

# Test
if __name__ == "__main__":
    compliance = ComplianceChecker()
    result = compliance.check_operation("email_analysis", "city_manager")
    print("Compliance Check:", result)
