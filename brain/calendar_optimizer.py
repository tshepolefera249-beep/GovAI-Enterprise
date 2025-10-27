# brain/calendar_optimizer.py - GOVAI CALENDAR INTELLIGENCE
class CalendarOptimizer:
    def __init__(self):
        self.user_calendars = {}
        print("✅ Calendar Optimizer Initialized")
    
    def analyze_user_calendar(self, user_id, calendar_events, user_role):
        """Analyze calendar and provide optimization recommendations"""
        analysis = {
            "user_id": user_id,
            "role": user_role,
            "total_meetings": len(calendar_events),
            "meeting_hours_per_week": self._calculate_meeting_hours(calendar_events),
            "focus_time_available": self._calculate_focus_time(calendar_events),
            "optimization_recommendations": self._generate_recommendations(calendar_events, user_role),
            "conflicts_detected": self._find_scheduling_conflicts(calendar_events),
            "ideal_meeting_times": self._suggest_optimal_times(calendar_events, user_role)
        }
        
        self.user_calendars[user_id] = analysis
        return analysis
    
    def _calculate_meeting_hours(self, events):
        """Calculate total meeting hours per week"""
        total_hours = 0
        for event in events:
            if "duration" in event:
                total_hours += event["duration"]
            elif "hours" in event:
                total_hours += event["hours"]
        return total_hours
    
    def _calculate_focus_time(self, events):
        """Calculate available focus time (gaps between meetings)"""
        # Simple calculation - in real system would analyze schedule gaps
        total_meeting_hours = self._calculate_meeting_hours(events)
        total_work_hours = 40  # Standard work week
        return max(0, total_work_hours - total_meeting_hours)
    
    def _generate_recommendations(self, events, user_role):
        """Generate calendar optimization recommendations"""
        recommendations = []
        total_meetings = len(events)
        
        if total_meetings > 20:
            recommendations.append("🚨 Meeting overload: Consider consolidating or delegating meetings")
        
        if self._calculate_meeting_hours(events) > 25:
            recommendations.append("📅 High meeting hours: Protect 2+ hours daily for focused work")
        
        if user_role == "City Manager":
            recommendations.extend([
                "🏛️ Block time for strategic planning (2 hours weekly)",
                "🤝 Reserve open office hours for staff (1 hour daily)",
                "📊 Schedule budget review sessions (1 hour weekly)"
            ])
        
        return recommendations if recommendations else ["Calendar is well-balanced"]
    
    def _find_scheduling_conflicts(self, events):
        """Identify potential scheduling conflicts"""
        conflicts = []
        
        # Simple conflict detection - would be more sophisticated in real system
        meeting_times = []
        for event in events:
            if "time" in event:
                meeting_times.append(event["time"])
        
        # Check for duplicate times (simplified)
        if len(meeting_times) != len(set(meeting_times)):
            conflicts.append("Potential double-booking detected")
        
        return conflicts
    
    def _suggest_optimal_times(self, events, user_role):
        """Suggest optimal meeting times based on role patterns"""
        optimal_times = {
            "City Manager": ["Tuesday 10AM-12PM", "Thursday 2PM-4PM"],
            "Policy Analyst": ["Monday 1PM-3PM", "Wednesday 9AM-11AM"],
            "Department Head": ["Tuesday 2PM-4PM", "Friday 10AM-12PM"]
        }
        
        return optimal_times.get(user_role, ["Morning hours generally most productive"])

# Test
if __name__ == "__main__":
    calendar_ai = CalendarOptimizer()
    
    sample_events = [
        {"name": "Budget Meeting", "duration": 2, "time": "Monday 9AM"},
        {"name": "Staff Review", "duration": 1, "time": "Monday 2PM"},
        {"name": "Council Prep", "duration": 1.5, "time": "Tuesday 10AM"}
    ]
    
    analysis = calendar_ai.analyze_user_calendar(
        "city_mgr_1", sample_events, "City Manager"
    )
    
    print("Calendar Analysis:", analysis)
