
import sys
import re

# Offline Socratic Rule Base for STEM & WAEC Topics
SOCRATIC_KNOWLEDGE_BASE = {
    "ohm": {
        "concept": "Ohm's Law (V = IR)",
        "prompts": [
            "Ohm's Law links Voltage (V), Current (I), and Resistance (R). If you increase resistance while keeping voltage the same, what happens to the current flowing through the circuit?",
            "Think about a water pipe: Voltage is water pressure, Current is water flow, and Resistance is a narrow pipe section. What happens to the water flow if the pipe gets narrower?",
            "Correct! Current decreases as resistance increases. The equation is V = I × R. If V = 12V and R = 4 Ohms, can you calculate Current (I)?"
        ]
    },
    "photosynthesis": {
        "concept": "Photosynthesis",
        "prompts": [
            "Photosynthesis is how green plants make their own food. Do you remember what three key inputs plants need from their environment to do this?",
            "Spot on! Sunlight, Water (H2O), and Carbon Dioxide (CO2). What gas do plants release into the air as a byproduct?",
            "Exactly, Oxygen! The chemical formula is 6CO2 + 6H2O + Light → C6H12O6 + 6O2. What is that produced sugar (C6H12O6) used for by the plant?"
        ]
    },
    "velocity": {
        "concept": "Velocity and Acceleration",
        "prompts": [
            "Speed is how fast something moves. What makes Velocity different from regular speed?",
            "Great! Velocity includes Direction. If a car changes direction while moving at a steady 60 km/h, is its velocity changing?",
            "Yes! Because direction changed. And any change in velocity over time is called Acceleration (a = (v - u) / t)."
        ]
    }
}

DEFAULT_RESPONSES = [
    "That's an interesting question! Before we dive in, what do you already know about this topic?",
    "To help you master this step-by-step: what key variables or definitions do you see in this problem?",
    "Let's break this down together. What is the main goal or outcome you are trying to find?"
]

def analyze_query(query):
    query_clean = query.lower()
   
    # Check for keyword matches in knowledge base
    for key, data in SOCRATIC_KNOWLEDGE_BASE.items():
        if key in query_clean:
            return f"[{data['concept']}] Ọ̀yẹ́: {data['prompts'][0]}"
           
    # Default Socratic prompt if keyword isn't indexed yet
    return f"Ọ̀yẹ́: {DEFAULT_RESPONSES[0]}"

if __name__ == "__main__":
    print("--------------------------------------------------")
    print("  🧠 Ọ̀yẹ́ Socratic Engine v1.0 (Project Ìmọ̀ Offline)  ")
    print("  Type 'exit' to quit.                            ")
    print("--------------------------------------------------\n")
   
    while True:
        try:
            user_input = input("Student > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("Ọ̀yẹ́: Ó d'àbọ̀! Keep learning.")
                break
               
            response = analyze_query(user_input)
            print(f"\n{response}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nỌ̀yẹ́: Exiting engine.")
            break
