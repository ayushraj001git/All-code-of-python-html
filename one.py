# Hospital Appointment Scheduler (simple version)
# Name: Ayush Raj
# Course: B.Tech CSE - First Semester

from datetime import datetime

# All appointments are stored in this dictionary.
# Key = appointment ID (like "A101"), Value = details of that appointment.
appt_list = {}

# The next appointment number. The first ID will be A101.
next_id = 101

# The two doctors in the clinic.
DOCTORS = ["Dr. Mehta", "Dr. Rao"]


def show_menu():
    print("\n===== HOSPITAL APPOINTMENT SCHEDULER =====")
    print("1. Book Appointment")
    print("2. View All Appointments")
    print("3. Reschedule Appointment")
    print("4. Cancel Appointment")
    print("5. Exit")


def check_date_and_time(date_text, time_text):
    # This function checks the date and the time.
    # It gives back True if both are correct, otherwise False.

    # Step 1: check the date (DD-MM-YYYY). A wrong date like 31-11-2026
    # makes strptime fail, so the program goes to "except".
    try:
        datetime.strptime(date_text, "%d-%m-%Y")
        if len(date_text) != 10:      # forces the form 05-01-2026
            raise ValueError
    except ValueError:
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return False

    # Step 2: check the time (HH:MM).
    try:
        time_value = datetime.strptime(time_text, "%H:%M")
        if len(time_text) != 5:       # forces the form 09:00
            raise ValueError
    except ValueError:
        print("Invalid time. Please enter the time as HH:MM.")
        return False

    # Step 3: time must be from 09:00 to 16:30.
    if time_value.hour < 9 or time_value.hour > 16:
        print("Invalid slot. Appointments are available from 09:00 to 16:30.")
        return False
    if time_value.hour == 16 and time_value.minute > 30:
        print("Invalid slot. Appointments are available from 09:00 to 16:30.")
        return False

    # Step 4: slots are 30 minutes, so minutes must be 00 or 30.
    if time_value.minute != 0 and time_value.minute != 30:
        print("Invalid slot. Please choose a 30-minute slot.")
        return False

    return True


def find_conflict(doctor, date_text, time_text, ignore_id=""):
    # This function checks if the same doctor already has this date and time.
    # It gives back True if there is a clash, otherwise False.
    for appt_id in appt_list:
        if appt_id == ignore_id:      # skip the appointment we are changing
            continue

        a = appt_list[appt_id]
        if a["doctor"] == doctor and a["date"] == date_text and a["time"] == time_text:
            return True

    return False


def book_appointment():
    global next_id        # we change next_id, which is outside this function

    print("\n--- Book Appointment ---")
    patient = input("Patient name: ").strip()
    doctor = input("Doctor (Dr. Mehta / Dr. Rao): ").strip()

    if patient == "":
        print("Patient name cannot be empty.")
        return

    if doctor not in DOCTORS:
        print("Invalid doctor. Please choose Dr. Mehta or Dr. Rao.")
        return

    date_text = input("Date (DD-MM-YYYY): ").strip()
    time_text = input("Time (HH:MM): ").strip()

    if check_date_and_time(date_text, time_text) == False:
        return

    if find_conflict(doctor, date_text, time_text):
        print("Slot unavailable: " + doctor + " already has an appointment on "
              + date_text + " at " + time_text + ".")
        return

    # Everything is correct, so save the appointment.
    appt_id = "A" + str(next_id)
    appt_list[appt_id] = {
        "patient": patient,
        "doctor": doctor,
        "date": date_text,
        "time": time_text
    }
    next_id = next_id + 1

    print("Appointment booked. ID: " + appt_id + " | " + patient + " | "
          + doctor + " | " + date_text + " " + time_text)


def view_appointments():
    print("\n--- All Appointments ---")

    if len(appt_list) == 0:
        print("No appointments found.")
    else:
        for appt_id in appt_list:
            a = appt_list[appt_id]
            print(appt_id + " | " + a["patient"] + " | " + a["doctor"]
                  + " | " + a["date"] + " | " + a["time"])

    print("Total appointments: " + str(len(appt_list)))


def reschedule_appointment():
    print("\n--- Reschedule Appointment ---")
    appt_id = input("Enter appointment ID: ").strip().upper()

    if appt_id not in appt_list:
        print("Appointment ID not found.")
        return

    date_text = input("New date (DD-MM-YYYY): ").strip()
    time_text = input("New time (HH:MM): ").strip()

    if check_date_and_time(date_text, time_text) == False:
        return

    doctor = appt_list[appt_id]["doctor"]

    # ignore_id = appt_id, so the appointment does not clash with itself.
    if find_conflict(doctor, date_text, time_text, appt_id):
        print("Slot unavailable: " + doctor + " already has an appointment on "
              + date_text + " at " + time_text + ".")
        return

    appt_list[appt_id]["date"] = date_text
    appt_list[appt_id]["time"] = time_text
    print("Appointment " + appt_id + " rescheduled to " + date_text + " "
          + time_text + ".")


def cancel_appointment():
    print("\n--- Cancel Appointment ---")
    appt_id = input("Enter appointment ID: ").strip().upper()

    if appt_id in appt_list:
        del appt_list[appt_id]
        print("Appointment " + appt_id + " cancelled.")
    else:
        print("Appointment ID not found.")


def main():
    print("Hospital Appointment Scheduler")
    print("Available doctors: Dr. Mehta, Dr. Rao")

    while True:                       # keeps showing the menu again and again
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_appointments()
        elif choice == "3":
            reschedule_appointment()
        elif choice == "4":
            cancel_appointment()
        elif choice == "5":
            print("Thank you. Program closed.")
            break                     # stops the while loop
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()