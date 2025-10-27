# deployment/performance_monitor.py - GOVAI PERFORMANCE MONITORING
class PerformanceMonitor:
    def __init__(self):
        self.performance_metrics = {}
        self.alert_thresholds = {
            "response_time_ms": 1000,  # 1 second
            "cpu_usage_percent": 80,
            "memory_usage_percent": 85,
            "error_rate_percent": 5
        }
        print("✅ Performance Monitor Initialized")
    
    def track_system_performance(self, component, metrics):
        """Track and analyze system performance metrics"""
        performance_data = {
            "component": component,
            "timestamp": "2024-01-01 10:00:00",
            "metrics": metrics,
            "health_status": self._assess_health(metrics),
            "alerts": self._check_alerts(metrics),
            "recommendations": self._generate_recommendations(metrics)
        }
        
        if component not in self.performance_metrics:
            self.performance_metrics[component] = []
        
        self.performance_metrics[component].append(performance_data)
        return performance_data
    
    def _assess_health(self, metrics):
        """Assess overall system health"""
        health_score = 100
        
        # Deduct points for performance issues
        if metrics.get("response_time_ms", 0) > self.alert_thresholds["response_time_ms"]:
            health_score -= 20
        
        if metrics.get("cpu_usage_percent", 0) > self.alert_thresholds["cpu_usage_percent"]:
            health_score -= 25
        
        if metrics.get("memory_usage_percent", 0) > self.alert_thresholds["memory_usage_percent"]:
            health_score -= 25
        
        if metrics.get("error_rate_percent", 0) > self.alert_thresholds["error_rate_percent"]:
            health_score -= 30
        
        # Determine health status
        if health_score >= 90:
            return "EXCELLENT"
        elif health_score >= 75:
            return "GOOD"
        elif health_score >= 60:
            return "FAIR"
        else:
            return "POOR"
    
    def _check_alerts(self, metrics):
        """Check for performance alerts"""
        alerts = []
        
        if metrics.get("response_time_ms", 0) > self.alert_thresholds["response_time_ms"]:
            alerts.append("🚨 High response time - users may experience delays")
        
        if metrics.get("cpu_usage_percent", 0) > self.alert_thresholds["cpu_usage_percent"]:
            alerts.append("🚨 High CPU usage - consider scaling resources")
        
        if metrics.get("memory_usage_percent", 0) > self.alert_thresholds["memory_usage_percent"]:
            alerts.append("🚨 High memory usage - potential memory leak")
        
        if metrics.get("error_rate_percent", 0) > self.alert_thresholds["error_rate_percent"]:
            alerts.append("🚨 High error rate - investigate system stability")
        
        return alerts if alerts else ["✅ All systems normal"]
    
    def _generate_recommendations(self, metrics):
        """Generate performance optimization recommendations"""
        recommendations = []
        
        if metrics.get("response_time_ms", 0) > 500:
            recommendations.append("⚡ Optimize database queries for faster response")
        
        if metrics.get("cpu_usage_percent", 0) > 70:
            recommendations.append("🔄 Implement caching to reduce CPU load")
        
        if metrics.get("memory_usage_percent", 0) > 75:
            recommendations.append("🗑️ Review memory allocation and garbage collection")
        
        if metrics.get("active_users", 0) > 100:
            recommendations.append("📈 Consider horizontal scaling for user load")
        
        return recommendations if recommendations else ["✅ Current performance is optimal"]
    
    def generate_performance_report(self):
        """Generate comprehensive performance report"""
        total_components = len(self.performance_metrics)
        excellent_health = 0
        alerts_count = 0
        
        for component, data in self.performance_metrics.items():
            latest = data[-1] if data else {}
            if latest.get("health_status") == "EXCELLENT":
                excellent_health += 1
            
            alerts = latest.get("alerts", [])
            if alerts and "🚨" in str(alerts):
                alerts_count += 1
        
        return {
            "total_monitored_components": total_components,
            "components_excellent_health": excellent_health,
            "active_alerts": alerts_count,
            "overall_system_health": "EXCELLENT" if (excellent_health / total_components) > 0.8 else "GOOD",
            "recommendations": self._get_system_recommendations()
        }
    
    def _get_system_recommendations(self):
        """Get system-wide recommendations"""
        return [
            "📊 Implement continuous performance monitoring",
            "🔧 Regular system maintenance and updates",
            "📈 Scale resources based on usage patterns",
            "🛡️ Regular security and performance audits"
        ]

# Test
if __name__ == "__main__":
    monitor = PerformanceMonitor()
    
    # Simulate performance metrics
    metrics = {
        "response_time_ms": 150,
        "cpu_usage_percent": 65,
        "memory_usage_percent": 70,
        "error_rate_percent": 1,
        "active_users": 50
    }
    
    performance = monitor.track_system_performance("main_api", metrics)
    print("Performance Data:", performance)
    
    report = monitor.generate_performance_report()
    print("Performance Report:", report)
