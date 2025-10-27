# brain/decision_support.py - GOVAI DECISION INTELLIGENCE
class DecisionSupport:
    def __init__(self):
        self.decision_history = {}
        print("✅ Decision Support System Initialized")
    
    def analyze_decision(self, decision_context, options, user_role):
        """Provide AI-powered decision support for government choices"""
        analysis = {
            "decision_context": decision_context,
            "options_evaluated": len(options),
            "risk_assessment": self._assess_risks(options, user_role),
            "stakeholder_impact": self._analyze_stakeholder_impact(options),
            "recommended_option": self._recommend_best_option(options, decision_context, user_role),
            "implementation_timeline": self._estimate_timeline(options),
            "success_metrics": self._define_success_metrics(decision_context)
        }
        
        decision_id = f"decision_{len(self.decision_history) + 1}"
        self.decision_history[decision_id] = analysis
        
        return analysis
    
    def _assess_risks(self, options, user_role):
        """Assess risks for each decision option"""
        risks = {}
        
        for i, option in enumerate(options):
            option_risks = []
            
            # Financial risks
            if "cost" in option and option["cost"] > 100000:
                option_risks.append("High financial commitment")
            
            # Political risks for senior roles
            if user_role in ["City Manager", "Department Head"]:
                if "public_impact" in option and option["public_impact"] == "high":
                    option_risks.append("High public visibility - political risk")
            
            # Operational risks
            if "complexity" in option and option["complexity"] == "high":
                option_risks.append("High implementation complexity")
            
            risks[f"option_{i+1}"] = option_risks if option_risks else ["Low to moderate risk"]
        
        return risks
    
    def _analyze_stakeholder_impact(self, options):
        """Analyze impact on different stakeholder groups"""
        stakeholder_groups = ["public", "employees", "elected_officials", "businesses"]
        
        impacts = {}
        for i, option in enumerate(options):
            option_impacts = {}
            
            for group in stakeholder_groups:
                # Simplified impact assessment
                if group in option.get("impact", {}):
                    impact_level = option["impact"][group]
                    option_impacts[group] = impact_level
                else:
                    option_impacts[group] = "neutral"
            
            impacts[f"option_{i+1}"] = option_impacts
        
        return impacts
    
    def _recommend_best_option(self, options, context, user_role):
        """Recommend the best option based on multiple factors"""
        if not options:
            return "No options provided for analysis"
        
        # Simple scoring system
        scores = []
        for i, option in enumerate(options):
            score = 0
            
            # Cost efficiency (lower cost = higher score)
            if "cost" in option:
                score += max(0, 10 - (option["cost"] / 10000))
            
            # Implementation speed (faster = higher score)
            if "timeline" in option and option["timeline"] == "short":
                score += 3
            
            # Public benefit (higher benefit = higher score)
            if "public_benefit" in option and option["public_benefit"] == "high":
                score += 5
            
            scores.append((i, score))
        
        # Find highest scoring option
        best_option_index = max(scores, key=lambda x: x[1])[0]
        
        return {
            "option": options[best_option_index],
            "reasoning": "Balanced approach considering cost, timeline, and public benefit",
            "confidence_score": "High"
        }
    
    def _estimate_timeline(self, options):
        """Estimate implementation timeline for options"""
        timelines = {}
        
        for i, option in enumerate(options):
            if "timeline" in option:
                timelines[f"option_{i+1}"] = option["timeline"]
            else:
                # Default estimates based on option complexity
                if "complexity" in option and option["complexity"] == "high":
                    timelines[f"option_{i+1}"] = "6-12 months"
                else:
                    timelines[f"option_{i+1}"] = "3-6 months"
        
        return timelines
    
    def _define_success_metrics(self, context):
        """Define metrics to measure decision success"""
        metrics_templates = {
            "budget": ["Cost savings", "On-time delivery", "Budget adherence"],
            "policy": ["Public satisfaction", "Compliance rate", "Implementation speed"],
            "operations": ["Efficiency gain", "Error reduction", "Employee satisfaction"]
        }
        
        for key in metrics_templates:
            if key in context.lower():
                return metrics_templates[key]
        
        return ["Goal achievement", "Stakeholder satisfaction", "Timeline adherence"]

# Test
if __name__ == "__main__":
    decision_ai = DecisionSupport()
    
    sample_options = [
        {
            "name": "Option A - Full Implementation",
            "cost": 150000,
            "timeline": "long",
            "public_benefit": "high",
            "complexity": "high"
        },
        {
            "name": "Option B - Phased Approach", 
            "cost": 80000,
            "timeline": "medium",
            "public_benefit": "medium",
            "complexity": "medium"
        }
    ]
    
    analysis = decision_ai.analyze_decision(
        "Budget allocation for park renovation",
        sample_options,
        "City Manager"
    )
    
    print("Decision Analysis:", analysis)
    
