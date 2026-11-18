# Hospital Appointment Scheduler
# Name: Ayush Raj
# ERP: RU-26-01929
# Course: B.Tech CSE - First Semester

from datetime import datetime


# The program stores all appointments in this dictionary.
# Appointment ID is the key and the appointment details are the value.
appt_list = {}
next_id = 101

DOCTORS = ["Dr. Mehta", "Dr. Rao"]
START_TIME = "09:00"
END_TIME = "16:30"


def show_menu():
    print("\n===== HOSPITAL APPOINTMENT SCHEDULER =====")
    print("1. Book Appointment")
    print("2. View All Appointments")
    print("3. Reschedule Appointment")
    print("4. Cancel Appointment")
    print("5. Exit")


def get_appointment_datetime(date_text, time_text):
    """Check the date, time and 30-minute slot, then return a datetime value."""

    # Check date format and also check whether the date really exists.
    try:
        date_value = datetime.strptime(date_text, "%d-%m-%Y")
        if date_value.strftime("%d-%m-%Y") != date_text:
            raise ValueError
    except ValueError:
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return None

    # Check time format.
    try:
        time_value = datetime.strptime(time_text, "%H:%M")
        if time_value.strftime("%H:%M") != time_text:
            raise ValueError
    except ValueError:
        print("Invalid time. Please enter the time as HH:MM.")
        return None

    # Appointment slots are from 09:00 to 16:30, with a gap of 30 minutes.
    start_value = datetime.strptime(START_TIME, "%H:%M")
    end_value = datetime.strptime(END_TIME, "%H:%M")

    if time_value < start_value or time_value > end_value:
        print("Invalid slot. Appointments are available from 09:00 to 16:30.")
        return None

    if time_value.minute not in (0, 30):
        print("Invalid slot. Please choose a 30-minute slot.")
        return None

    return datetime.strptime(date_text + " " + time_text, "%d-%m-%Y %H:%M")


def find_conflict(doctor, new_datetime, ignore_id=None):
    """Return True when the same doctor already has this date and time."""

    for appt_id in appt_list:
        if appt_id == ignore_id:
            continue

        appointment = appt_list[appt_id]
        old_datetime = datetime.strptime(
            appointment["date"] + " " + appointment["time"],
            "%d-%m-%Y %H:%M"
        )

        if appointment["doctor"] == doctor and old_datetime == new_datetime:
            return True

    return False


def book_appointment():
    global next_id

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

    new_datetime = get_appointment_datetime(date_text, time_text)
    if new_datetime is None:
        return

    if find_conflict(doctor, new_datetime):
        print(
            "Slot unavailable: " + doctor + " already has an appointment on "
            + date_text + " at " + time_text + "."
        )
        return

    appt_id = "A" + str(next_id)
    appt_list[appt_id] = {
        "patient": patient,
        "doctor": doctor,
        "date": date_text,
        "time": time_text
    }
    next_id = next_id + 1

    print(
        "Appointment booked. ID: " + appt_id + " | " + patient + " | "
        + doctor + " | " + date_text + " " + time_text
    )


def view_appointments():
    print("\n--- All Appointments ---")

    if len(appt_list) == 0:
        print("No appointments found.")
    else:
        for appt_id in appt_list:
            appointment = appt_list[appt_id]
            print(
                appt_id + " | " + appointment["patient"] + " | "
                + appointment["doctor"] + " | " + appointment["date"]
                + " | " + appointment["time"]
            )

    print("Total appointments: " + str(len(appt_list)))


def reschedule_appointment():
    print("\n--- Reschedule Appointment ---")
    appt_id = input("Enter appointment ID: ").strip().upper()

    if appt_id not in appt_list:
        print("Appointment ID not found.")
        return

    date_text = input("New date (DD-MM-YYYY): ").strip()
    time_text = input("New time (HH:MM): ").strip()

    new_datetime = get_appointment_datetime(date_text, time_text)
    if new_datetime is None:
        return

    doctor = appt_list[appt_id]["doctor"]

    # ignore_id prevents the appointment from conflicting with itself.
    if find_conflict(doctor, new_datetime, appt_id):
        print(
            "Slot unavailable: " + doctor + " already has an appointment on "
            + date_text + " at " + time_text + "."
        )
        return

    appt_list[appt_id]["date"] = date_text
    appt_list[appt_id]["time"] = time_text

    print(
        "Appointment " + appt_id + " rescheduled to " + date_text + " "
        + time_text + "."
    )


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

    while True:
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
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()