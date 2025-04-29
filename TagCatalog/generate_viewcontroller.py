import os

def generate_viewcontroller():
    # Start with the base template
    content = """import UIKit
import TagCatalog

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        
"""
    
    # Generate all 400 features
    for feature_num in range(1, 401):
        feature_name = f"Feature{feature_num:03d}"
        content += f"        // Feature {feature_num:03d}\n"
        for event_num in range(1, 11):
            event_name = f"event{event_num:02d}"
            content += f"        Catalog.{feature_name}.{event_name}().publish()\n"
        content += "\n"
    
    # Close the class
    content += "    }\n}"
    
    # Write to file in the AppSizeBehavior directory
    with open("/Volumes/Data/MyCode.nosync/AppSizeBehavior/AppSizeBehavior/ViewController.swift", "w") as f:
        f.write(content)

if __name__ == "__main__":
    generate_viewcontroller()
    print("ViewController.swift has been generated with all 400 features.") 