# brain/meeting_analyzer.py - GOVAI MEETING INTELLIGENCE
class MeetingAnalyzer:
    def __init__(self):
        self.meeting_history = {}
        print("✅ Meeting Analyzer Initialized")
    
    def analyze_meeting_transcript(self, transcript, meeting_type, attendees):
        """Analyze meeting content and extract key information"""
        analysis = {
            "meeting_type": meeting_type,
            "attendees": attendees,
            "key_decisions": self._extract_decisions(transcript),
            "action_items": self._extract_actions(transcript, attendees),
            "discussion_topics": self._identify_topics(transcript),
            "meeting_summary": self._generate_summary(transcript),
            "follow_up_required": self._check_follow_up(transcript)
        }
        
        meeting_id = f"meeting_{len(self.meeting_history) + 1}"
        self.meeting_history[meeting_id] = analysis
        
        return analysis
    
    def _extract_decisions(self, transcript):
        """Extract decisions made during meeting"""
        decision_keywords = ["decided", "agreed", "approved", "resolved", "will proceed"]
        decisions = []
        
        lines = transcript.split('.')
        for line in lines:
            if any(keyword in line.lower() for keyword in decision_keywords):
                decisions.append(line.strip())
        
        return decisions if decisions else ["No formal decisions recorded"]
    
    def _extract_actions(self, transcript, attendees):
        """Extract action items and assign to attendees"""
        action_patterns = ["will", "to do", "action", "follow up", "responsible for"]
        actions = []
        
        lines = transcript.split('.')
        for line in lines:
            if any(pattern in line.lower() for pattern in action_patterns):
                # Try to assign to specific person
                assigned_to = "TBD"
                for attendee in attendees:
                    if attendee.lower() in line.lower():
                        assigned_to = attendee
                        break
                
                actions.append({
                    "action": line.strip(),
                    "assigned_to": assigned_to,
                    "deadline": "TBD"
                })
        
        return actions if actions else [{"action": "No specific actions recorded", "assigned_to": "N/A", "deadline": "N/A"}]
    
    def _identify_topics(self, transcript):
        """Identify main discussion topics"""
        topics = {
            "budget": ["budget", "funding", "financial", "cost", "money"],
            "policy": ["policy", "regulation", "law", "rule", "legislation"],
            "operations": ["operations", "process", "procedure", "workflow"],
            "personnel": ["staff", "hiring", "training", "personnel", "employees"]
        }
        
        found_topics = []
        for topic, keywords in topics.items():
            if any(keyword in transcript.lower() for keyword in keywords):
                found_topics.append(topic)
        
        return found_topics if found_topics else ["General discussion"]
    
    def _generate_summary(self, transcript):
        """Generate executive summary of meeting"""
        # Simple summary - would use AI in real implementation
        lines = transcript.split('.')
        key_points = [line.strip() for line in lines if len(line.strip()) > 20][:3]
        
        if key_points:
            return "Meeting focused on: " + "; ".join(key_points)
        else:
            return "Brief discussion covering various topics."
    
    def _check_follow_up(self, transcript):
        """Check if follow-up meeting is needed"""
        follow_up_indicators = ["follow up", "next meeting", "continue discussion", "reconvene"]
        return any(indicator in transcript.lower() for indicator in follow_up_indicators)

# Test
if __name__ == "__main__":
    meeting_ai = MeetingAnalyzer()
    
    sample_transcript = """
    The city council meeting discussed the budget shortfall. We decided to cut non-essential spending by 10%. 
    Sarah will follow up with department heads. Mike will prepare a revised budget proposal. 
    We agreed to meet again next week to review the changes.
    """
    
    analysis = meeting_ai.analyze_meeting_transcript(
        sample_transcript,
        "City Council Budget Meeting",
        ["Sarah Chen", "Mike Rodriguez", "Council Members"]
    )
    
    print("Meeting Analysis:", analysis)
