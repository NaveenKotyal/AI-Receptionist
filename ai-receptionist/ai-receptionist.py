import time
import random
import difflib

# Emergency database with predefined responses
emergency_database = {
    "heart attack": "Chew and swallow an aspirin if available, and sit down and rest.",
    "stroke": "Remember FAST: Face drooping, Arm weakness, Speech difficulty, Time to call emergency services.",
    "severe bleeding": "Apply direct pressure to the wound with a clean cloth or sterile bandage.",
    "allergic reaction": "If you have an EpiPen, use it immediately. Remove any potential allergens.",
    "broken bone": "Don't move the affected area. Apply ice if available to reduce swelling."
}

def simulate_database_call(emergency):
    """Simulate a database call with a delay and return emergency instructions."""
    print("Searching database for emergency information...")
    time.sleep(4)  # Simulated delay for database call
    
    # Try to find the closest match for the emergency in the database
    closest_match = difflib.get_close_matches(emergency.lower(), emergency_database.keys(), n=1, cutoff=0.6)
    if closest_match:
        return emergency_database[closest_match[0]]
    return "Stay calm and wait for the doctor to arrive."

def get_estimated_arrival_time():
    """Generate a random estimated arrival time between 5 and 30 minutes."""
    return random.randint(5, 30)

def ai_receptionist():
    """Handle user interactions for emergency or message scenarios."""
    print("AI Receptionist: Hello! Are you having an emergency or would you like to leave a message for Dr. Adrin?")
    
    while True:
        user_input = input("User: ").lower().strip()
        
        if "emergency" in user_input:
            print("AI Receptionist: I understand this is an emergency. Can you please tell me what the emergency is?")
            emergency = input("User: ").lower().strip()
            
            if not emergency:
                print("AI Receptionist: I didn’t catch that. Can you please tell me what the emergency is?")
                continue

            print("AI Receptionist: I'm looking up information for your emergency. In the meantime, can you please tell me your location?")
            location = input("User: ").strip()
            
            if not location:
                print("AI Receptionist: I didn’t catch that. Could you please tell me your location?")
                location = input("User: ").strip()

            next_steps = simulate_database_call(emergency)
            eta = get_estimated_arrival_time()
            
            print(f"AI Receptionist: Thank you. Dr. Adrin will be coming to your location at {location} immediately. The estimated time of arrival is {eta} minutes.")
            print(f"AI Receptionist: While waiting, please follow these steps: {next_steps}")
            
            user_response = input("User: ").lower().strip()
            if "too late" in user_response or "long" in user_response or "not fast enough" in user_response:
                print(f"AI Receptionist: I understand your concern. Please follow the suggested steps: {next_steps}. Dr. Adrin is on the way and will be there as soon as possible.")
            
            print("AI Receptionist: Don't worry, please follow these steps, Dr. Adrin will be with you shortly.")
            print("Dr. Adrin has arrived at your location. Get well soon.")
            break
        
        elif "message" in user_input:
            while True:
                print("AI Receptionist: Certainly, what message would you like to leave for Dr. Adrin?")
                message = input("User: ").strip()
                if message:
                    print("AI Receptionist: Thanks for the message, we will forward it to Dr. Adrin.")
                    break
                else:
                    print("AI Receptionist: Please leave a meaningful message, thank you!")
            break
        
        elif any(keyword in user_input for keyword in ["help", "assistance", "urgent"]):
            print("AI Receptionist: It sounds like you may need help. Is this an emergency or would you like to leave a message for Dr. Adrin?")
            continue
        
        elif not user_input or user_input in ["", " "]:
            print("AI Receptionist: I didn’t catch that. Could you please clarify?")
            continue
        
        else:
            print("AI Receptionist: I'm sorry, I don't understand. Are you having an emergency or would you like to leave a message for Dr. Adrin?")
            continue

print("This is an interactive AI receptionist simulation. You can type your responses when prompted.")
print("To start, type 'start' and press Enter.")
if input().lower().strip() == 'start':
    ai_receptionist()
else:
    print("Simulation not started. Run the cell again to try.")

print("Simulation completed,I am Ready for your service Anytime,Thank You!")
