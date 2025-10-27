# brain/document_processor.py - GOVAI DOCUMENT INTELLIGENCE
class DocumentProcessor:
    def __init__(self):
        self.processed_documents = {}
        print("✅ Document Processor Initialized")
    
    def analyze_government_document(self, document_text, doc_type, user_role):
        """Analyze government documents and extract key information"""
        analysis = {
            "document_type": doc_type,
            "key_findings": self._extract_key_findings(document_text),
            "recommendations": self._extract_recommendations(document_text),
            "action_required": self._check_actions_required(document_text),
            "summary": self._generate_document_summary(document_text, doc_type),
            "compliance_check": self._check_compliance_issues(document_text)
        }
        
        doc_id = f"doc_{len(self.processed_documents) + 1}"
        self.processed_documents[doc_id] = analysis
        
        return analysis
    
    def _extract_key_findings(self, text):
        """Extract key findings from document"""
        # Look for patterns like "finding:", "result:", "conclusion:"
        findings = []
        lines = text.split('\n')
        
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in ["finding:", "result:", "conclusion:", "determined that"]):
                findings.append(line.strip())
        
        return findings if findings else ["Key findings not explicitly stated"]
    
    def _extract_recommendations(self, text):
        """Extract recommendations from document"""
        recommendations = []
        lines = text.split('\n')
        
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in ["recommend", "suggest", "propose", "should", "advise"]):
                recommendations.append(line.strip())
        
        return recommendations if recommendations else ["No specific recommendations found"]
    
    def _check_actions_required(self, text):
        """Check if document requires specific actions"""
        action_indicators = ["action required", "must", "shall", "will implement", "to be completed by"]
        return any(indicator in text.lower() for indicator in action_indicators)
    
    def _generate_document_summary(self, text, doc_type):
        """Generate document summary based on type"""
        if doc_type == "budget":
            return self._summarize_budget_document(text)
        elif doc_type == "policy":
            return self._summarize_policy_document(text)
        elif doc_type == "report":
            return self._summarize_report_document(text)
        else:
            return "Document summary: " + text[:200] + "..."
    
    def _summarize_budget_document(self, text):
        """Specialized summary for budget documents"""
        budget_indicators = ["total budget", "revenue", "expenditure", "allocation", "shortfall"]
        found = [indicator for indicator in budget_indicators if indicator in text.lower()]
        
        if found:
            return f"Budget document discussing: {', '.join(found)}"
        else:
            return "Financial document requiring review"
    
    def _summarize_policy_document(self, text):
        """Specialized summary for policy documents"""
        policy_indicators = ["policy", "regulation", "compliance", "requirement", "standard"]
        found = [indicator for indicator in policy_indicators if indicator in text.lower()]
        
        if found:
            return f"Policy document covering: {', '.join(found)}"
        else:
            return "Policy document requiring analysis"
    
    def _summarize_report_document(self, text):
        """Specialized summary for reports"""
        return "Report document - review findings and recommendations"
    
    def _check_compliance_issues(self, text):
        """Check for potential compliance issues"""
        compliance_red_flags = ["non-compliant", "violation", "breach", "unauthorized", "against policy"]
        issues = [flag for flag in compliance_red_flags if flag in text.lower()]
        
        return {
            "has_issues": len(issues) > 0,
            "potential_issues": issues
        }

# Test
if __name__ == "__main__":
    doc_ai = DocumentProcessor()
    
    sample_document = """
    Quarterly Budget Report
    Findings: The city is facing a 15% budget shortfall due to reduced tax revenue.
    Recommendations: We recommend cutting non-essential services by 10% and implementing a hiring freeze.
    Action Required: Department heads must submit revised budgets by Friday.
    """
    
    analysis = doc_ai.analyze_government_document(
        sample_document,
        "budget",
        "City Manager"
    )
    
    print("Document Analysis:", analysis)
