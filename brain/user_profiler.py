# brain/user_profiler.py - GOVAI USER INTELLIGENCE
class UserProfiler:
    def __init__(self):
        self.profiles = {}
        print("✅ User Profiler Initialized")
    
    def create_government_profile(self, user_id, role, department, challenges):
        profile = {
            "user_id": user_id,
            "role": role,
            "department": department,
            "challenges": challenges,
            "ai_recommendations": self._get_recommendations(role, challenges),
            "personalized_features": self._get_features(role)
        }
        self.profiles[user_id] = profile
        return profile
    
    def _get_recommendations(self, role, challenges):
        recommendations = []
        
        if "too many meetings" in challenges:
            recommendations.append("Use AI meeting summarizer to save 2+ hours daily")
        
        if "email overload" in challenges:
            recommendations.append("Enable AI email prioritization and auto-drafting")
        
        if role == "City Manager":
            recommendations.extend([
                "Budget analysis automation",
                "Council meeting preparation assistant", 
                "Stakeholder management tools"
            ])
        
        return recommendations
    
    def _get_features(self, role):
        features = {
            "City Manager": ["budget_analysis", "meeting_prep", "stakeholder_tracking"],
            "Policy Analyst": ["research_assistant", "data_analysis", "report_generation"],
            "Permit Processor": ["regulation_checker", "application_review", "customer_comms"]
        }
        return features.get(role, ["general_assistance"])

# Test
if __name__ == "__main__":
    profiler = UserProfiler()
    profile = profiler.create_government_profile(
        "test_1", "City Manager", "Administration", 
        ["too many meetings", "email overload"]
    )
    print("User Profile:", profile)
