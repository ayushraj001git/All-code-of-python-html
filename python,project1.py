import datetime

def validate_date(date_str):
    """
    Validates if the provided string is a valid date in DD-MM-YYYY format.
    """
    try:
        datetime.datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def validate_time(time_str):
    """
    Validates if the provided string is a valid time in HH:MM format.
    Ensures the time is between 09:00 and 16:30 and falls exactly on a 30-minute interval.
    """
    try:
        t = datetime.datetime.strptime(time_str, "%H:%M").time()
        
        # Define clinic hours
        start_time = datetime.time(9, 0)
        end_time = datetime.time(16, 30)
        
        # Check if the time falls within operating hours
        if not (start_time <= t <= end_time):
            return False
            
        # Check if the time is strictly on a 30-minute slot (e.g., :00 or :30)
        if t.minute not in (0, 30):
            return False
            
        return True
    except ValueError:
        return False

def is_slot_available(doctor, date_str, time_str, appointments, exclude_id=None):
    """
    Checks if the doctor is available for the specified date and time.
    The exclude_id parameter is used during rescheduling to ignore the 
    current appointment's old slot.
    """
    for apt_id, details in appointments.items():
        if exclude_id and apt_id == exclude_id:
            continue
        if (details['doctor'] == doctor and 
            details['date'] == date_str and 
            details['time'] == time_str):
            return False
    return True

def book_appointment(appointments, state):
    """Handles the logic for booking a new appointment."""
    patient = input("Patient: ")
    doctor = input("Doctor: ")
    
    # Validate doctor constraint
    if doctor not in ["Dr. Mehta", "Dr. Rao"]:
        print("Error: Invalid doctor. Only Dr. Mehta and Dr. Rao are available.")
        return
        
    date_str = input("Date: ")
    if not validate_date(date_str):
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return
        
    time_str = input("Time: ")
    if not validate_time(time_str):
        print("Invalid time. Slots are 30-minute intervals between 09:00 and 16:30.")
        return
        
    # Check for scheduling conflicts
    if not is_slot_available(doctor, date_str, time_str, appointments):
        print(f"Slot unavailable: {doctor} already has an appointment on {date_str} at {time_str}.")
        return
        
    # Generate the auto-incremented ID
    apt_id = f"A{state['next_id']}"
    state['next_id'] += 1
    
    # Store appointment in the dictionary
    appointments[apt_id] = {
        'patient': patient,
        'doctor': doctor,
        'date': date_str,
        'time': time_str
    }
    
    print(f"Appointment booked. ID: {apt_id} | {patient} | {doctor} | {date_str} {time_str}")

def view_appointments(appointments):
    """Displays all current appointments and the total count."""
    if not appointments:
        print("No appointments scheduled.")
        return
        
    for apt_id, details in appointments.items():
        print(f"{apt_id} | {details['patient']} | {details['doctor']} | {details['date']} {details['time']}")
    print(f"Total appointments: {len(appointments)}")

def reschedule_appointment(appointments):
    """Handles rescheduling an existing appointment."""
    apt_id = input("ID: ")
    if apt_id not in appointments:
        print("Error: Appointment ID not found.")
        return
        
    new_date = input("New Date: ")
    if not validate_date(new_date):
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return
        
    new_time = input("New Time: ")
    if not validate_time(new_time):
        print("Invalid time. Slots are 30-minute intervals between 09:00 and 16:30.")
        return
        
    doctor = appointments[apt_id]['doctor']
    
    # Check if the new slot conflicts with OTHER appointments
    if not is_slot_available(doctor, new_date, new_time, appointments, exclude_id=apt_id):
        print(f"Slot unavailable: {doctor} already has an appointment on {new_date} at {new_time}.")
        return
        
    # Update the dictionary
    appointments[apt_id]['date'] = new_date
    appointments[apt_id]['time'] = new_time
    print(f"Appointment {apt_id} rescheduled to {new_date} {new_time}.")

def cancel_appointment(appointments):
    """Handles cancelling and deleting an appointment."""
    apt_id = input("ID: ")
    if apt_id in appointments:
        del appointments[apt_id]
        print(f"Appointment {apt_id} cancelled.")
    else:
        print("Error: Appointment ID not found.")

def main():
    """Main function to drive the continuous menu loop."""
    appointments = {}
    state = {'next_id': 101} # Starts ID sequence at A101
    
    while True:
        print("\n--- Hospital Appointment Scheduler ---")
        print("1. Book Appointment")
        print("2. View All Appointments")
        print("3. Reschedule Appointment")
        print("4. Cancel Appointment")
        print("5. Exit")
        
        try:
            choice = input("Menu option: ")
        except KeyboardInterrupt:
            print("\nExiting program gracefully...")
            break
            
        if choice == '1':
            book_appointment(appointments, state)
        elif choice == '2':
            view_appointments(appointments)
        elif choice == '3':
            reschedule_appointment(appointments)
        elif choice == '4':
            cancel_appointment(appointments)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid menu option (1-5).")

if __name__ == "__main__":
    main()