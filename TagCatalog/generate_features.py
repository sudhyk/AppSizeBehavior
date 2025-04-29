import os
import random
from datetime import datetime

def generate_feature_file(feature_number):
    feature_name = f"Feature{feature_number:03d}"
    file_name = f"Catalog+{feature_name}.swift"
    
    # List of major cities with their coordinates
    cities = [
        (37.7749, -122.4194),  # San Francisco
        (40.7128, -74.0060),   # New York
        (51.5074, -0.1278),    # London
        (48.8566, 2.3522),     # Paris
        (35.6762, 139.6503),   # Tokyo
        (52.5200, 13.4050),    # Berlin
        (41.9028, 12.4964),    # Rome
        (55.7558, 37.6173),    # Moscow
        (19.4326, -99.1332),   # Mexico City
        (-33.8688, 151.2093),  # Sydney
    ]
    
    # List of roles
    roles = ["tester", "developer", "admin", "manager", "analyst", "designer", "qa", "support", "consultant", "architect"]
    
    # Generate the file content
    content = f"""import Foundation

extension Catalog {{
    public struct {feature_name}: TagPublishable {{
        var udo: UDO
        
        init(udo: UDO) {{ 
            self.udo = udo 
        }}
        
        public func publish() {{ 
            //do nothing
        }}
"""
    
    # Generate 10 events for each feature
    for event_num in range(1, 11):
        city = random.choice(cities)
        role = random.choice(roles)
        priority = event_num
        accuracy = event_num * 5.0
        
        content += f"""
        public static func event{event_num:02d}() -> {feature_name} {{
            var udo = UDO()
            udo.id = "event{event_num:02d}"
            udo.name = "{feature_name} Event {event_num:02d}"
            udo.description = "Description for {feature_name} Event {event_num:02d}"
            udo.createdAt = Date()
            udo.updatedAt = Date()
            udo.isActive = true
            udo.version = 1
            udo.priority = {priority}.0
            udo.tags = ["{feature_name.lower()}", "event{event_num:02d}"]
            udo.metadata = ["type": "event", "category": "{feature_name.lower()}"]
            udo.userId = "user{event_num:03d}"
            udo.userName = "Test User {event_num}"
            udo.userEmail = "test{event_num}@example.com"
            udo.userPhone = "{random.randint(1000000000, 9999999999)}"
            udo.userAddress = "{random.randint(1, 999)} Test St"
            udo.userCity = "Test City {event_num}"
            udo.userState = "TS{event_num}"
            udo.userCountry = "Test Country {event_num}"
            udo.userZipCode = "{random.randint(10000, 99999)}"
            udo.userRole = "{role}"
            udo.latitude = {city[0]}
            udo.longitude = {city[1]}
            udo.altitude = 0.0
            udo.locationAccuracy = {accuracy}
            udo.locationTimestamp = Date()
            udo.locationProvider = "{random.choice(['gps', 'network', 'fused'])}"
            
            return {feature_name}(udo: udo)
        }}
"""
    
    content += "    }\n}"
    
    # Write the file
    with open(file_name, 'w') as f:
        f.write(content)

def main():
    # Create files for features 002 to 400
    for i in range(2, 401):
        generate_feature_file(i)
        print(f"Generated feature {i:03d}")

if __name__ == "__main__":
    main() 
