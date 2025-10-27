# brain/email_assistant.py - GOVAI EMAIL INTELLIGENCE
class EmailAssistant:
    def __init__(self):
        self.processed_emails = []
        print("✅ Email Assistant Initialized")
    
    def analyze_government_email(self, email_subject, email_body, user_role):
        analysis = {
            "subject": email_subject,
            "urgency": self._check_urgency(email_subject, email_body),
            "category": self._categorize_email(email_subject, email_body),
            "suggested_response": self._generate_response(user_role, email_subject),
            "action_items": self._extract_actions(email_body)
        }
        self.processed_emails.append(analysis)
        return analysis
    
    def _check_urgency(self, subject, body):
        urgent_keywords = ["urgent", "emergency", "asap", "immediate", "deadline"]
        content = (subject + " " + body).lower()
        for keyword in urgent_keywords:
            if keyword in content:
                return "HIGH PRIORITY"
        return "STANDARD PRIORITY"
    
    def _categorize_email(self, subject, body):
        categories = {
            "budget": ["budget", "funding", "financial", "cost"],
            "meeting": ["meeting", "schedule", "calendar", "appointment"],
            "public_concern": ["complaint", "concern", "issue", "problem"],
            "policy": ["policy", "regulation", "rule", "legislation"]
        }
        
        content = (subject + " " + body).lower()
        for category, keywords in categories.items():
            if any(keyword in content for keyword in keywords):
                return category
        return "general"
    
    def _generate_response(self, user_role, subject):
        templates = {
            "City Manager": "I've reviewed this matter and will address it accordingly.",
            "Policy Analyst": "I'll research this issue and provide analysis.", 
            "Permit Processor": "I'll process this request per standard procedures."
        }
        return templates.get(user_role, "Thank you for your message. I'll follow up.")

# Test
if __name__ == "__main__":
    email_ai = EmailAssistant()
    result = email_ai.analyze_government_email(
        "URGENT: Budget Approval Needed",
        "The Q3 budget requires immediate approval due to deadline.",
        "City Manager"
    )
    print("Email Analysis:", result)
