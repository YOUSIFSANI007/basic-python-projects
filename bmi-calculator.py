from typing import Tuple, Dict
import sys

class BMICalculator:
    def __init__(self):
        # BMI category ranges
        self.bmi_categories = {
            'severe_underweight': (0, 16),
            'moderate_underweight': (16, 17),
            'mild_underweight': (17, 18.5),
            'normal': (18.5, 25),
            'overweight': (25, 30),
            'obese_class_1': (30, 35),
            'obese_class_2': (35, 40),
            'obese_class_3': (40, float('inf'))
        }
        
        # Detailed health information for each category
        self.health_info = {
            'severe_underweight': {
                'name': 'Severe Underweight',
                'risks': [
                    'Malnutrition',
                    'Weakened immune system',
                    'Osteoporosis',
                    'Anemia'
                ],
                'recommendations': [
                    'Consult a healthcare provider immediately',
                    'Work with a nutritionist to develop a healthy weight gain plan',
                    'Focus on nutrient-dense foods',
                    'Regular health monitoring'
                ]
            },
            'moderate_underweight': {
                'name': 'Moderate Underweight',
                'risks': [
                    'Nutritional deficiencies',
                    'Reduced muscle strength',
                    'Fatigue',
                    'Compromised immune function'
                ],
                'recommendations': [
                    'Consult a healthcare provider',
                    'Increase caloric intake with healthy foods',
                    'Include protein-rich foods in diet',
                    'Regular exercise to build muscle'
                ]
            },
            'mild_underweight': {
                'name': 'Mild Underweight',
                'risks': [
                    'Slightly increased health risks',
                    'Potential nutritional deficiencies',
                    'Reduced energy levels'
                ],
                'recommendations': [
                    'Gradually increase caloric intake',
                    'Include a variety of nutrients in diet',
                    'Monitor weight regularly',
                    'Moderate exercise'
                ]
            },
            'normal': {
                'name': 'Normal Weight',
                'risks': [
                    'Lowest risk for weight-related health issues'
                ],
                'recommendations': [
                    'Maintain current healthy lifestyle',
                    'Regular exercise',
                    'Balanced diet',
                    'Regular health check-ups'
                ]
            },
            'overweight': {
                'name': 'Overweight',
                'risks': [
                    'Increased risk of cardiovascular disease',
                    'Higher risk of type 2 diabetes',
                    'Joint stress',
                    'Sleep issues'
                ],
                'recommendations': [
                    'Gradually increase physical activity',
                    'Focus on portion control',
                    'Choose whole foods over processed foods',
                    'Regular health monitoring'
                ]
            },
            'obese_class_1': {
                'name': 'Class 1 Obesity',
                'risks': [
                    'High risk of cardiovascular disease',
                    'Type 2 diabetes',
                    'High blood pressure',
                    'Sleep apnea'
                ],
                'recommendations': [
                    'Consult healthcare provider',
                    'Develop structured exercise plan',
                    'Work with nutritionist',
                    'Regular health monitoring'
                ]
            },
            'obese_class_2': {
                'name': 'Class 2 Obesity',
                'risks': [
                    'Severe risk of cardiovascular issues',
                    'High risk of diabetes complications',
                    'Severe joint problems',
                    'Multiple health complications'
                ],
                'recommendations': [
                    'Immediate healthcare consultation',
                    'Supervised weight management program',
                    'Regular medical monitoring',
                    'Lifestyle modification support'
                ]
            },
            'obese_class_3': {
                'name': 'Class 3 Obesity',
                'risks': [
                    'Extremely high risk of severe health issues',
                    'Life-threatening complications',
                    'Severe mobility issues',
                    'Multiple organ stress'
                ],
                'recommendations': [
                    'Urgent medical consultation',
                    'Comprehensive medical evaluation',
                    'Supervised weight management',
                    'Consider medical interventions'
                ]
            }
        }

    def get_valid_measurement(self, prompt: str, unit: str) -> float:
        """Get and validate user input for measurements"""
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print(f"Please enter a valid {unit} (must be greater than 0)")
                    continue
                return value
            except ValueError:
                print(f"Please enter a valid number for {unit}")

    def convert_height(self, feet: float, inches: float) -> float:
        """Convert height from feet/inches to meters"""
        total_inches = (feet * 12) + inches
        return total_inches * 0.0254

    def get_height(self, unit_system: str) -> float:
        """Get height input based on unit system"""
        if unit_system == 'metric':
            height = self.get_valid_measurement("Enter height (in meters): ", "height")
        else:
            feet = self.get_valid_measurement("Enter height (feet): ", "feet")
            inches = self.get_valid_measurement("Enter inches: ", "inches")
            height = self.convert_height(feet, inches)
        return height

    def get_weight(self, unit_system: str) -> float:
        """Get weight input based on unit system"""
        if unit_system == 'metric':
            weight = self.get_valid_measurement("Enter weight (in kilograms): ", "weight")
        else:
            pounds = self.get_valid_measurement("Enter weight (in pounds): ", "weight")
            weight = pounds * 0.453592
        return weight

    def calculate_bmi(self, height: float, weight: float) -> float:
        """Calculate BMI from height (m) and weight (kg)"""
        return weight / (height * height)

    def get_bmi_category(self, bmi: float) -> str:
        """Determine BMI category"""
        for category, (lower, upper) in self.bmi_categories.items():
            if lower <= bmi < upper:
                return category
        return 'obese_class_3'  # Default for any BMI above highest range

    def display_results(self, bmi: float, category: str):
        """Display BMI results and health information"""
        info = self.health_info[category]
        
        print("\n=== BMI Results ===")
        print(f"Your BMI: {bmi:.1f}")
        print(f"Category: {info['name']}")
        
        print("\nHealth Risks:")
        for risk in info['risks']:
            print(f"• {risk}")
            
        print("\nRecommendations:")
        for rec in info['recommendations']:
            print(f"• {rec}")

        print("\nNote: BMI is a general indicator and may not be accurate for all body types.")
        print("Please consult healthcare professionals for personalized advice.")

    def run(self):
        """Main program loop"""
        print("Welcome to the BMI Calculator!")
        print("\nChoose unit system:")
        print("1. Metric (meters, kilograms)")
        print("2. Imperial (feet/inches, pounds)")

        while True:
            choice = input("\nEnter choice (1 or 2): ").strip()
            if choice in ['1', '2']:
                break
            print("Invalid choice. Please enter 1 or 2.")

        unit_system = 'metric' if choice == '1' else 'imperial'

        # Get measurements
        height = self.get_height(unit_system)
        weight = self.get_weight(unit_system)

        # Calculate and display results
        bmi = self.calculate_bmi(height, weight)
        category = self.get_bmi_category(bmi)
        self.display_results(bmi, category)

if __name__ == "__main__":
    calculator = BMICalculator()
    try:
        calculator.run()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(0)
