import pytz
from datetime import datetime

def convert_timezone(dt, from_tz, to_tz):
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    localized_dt = from_timezone.localize(dt)
    converted_dt = localized_dt.astimezone(to_timezone)
    return converted_dt

def get_timezone_list():
    timezones = pytz.all_timezones
    timezones.sort()
    return timezones

# Conversione da fuso orario italiano a fuso orario mondiale
def italian_to_world():
    italian_timezone = 'Europe/Rome'
    target_timezones = get_timezone_list()

    print("Fuso orario italiano: ", italian_timezone)
    dt_string = input("Inserisci data e ora nel formato 'YYYY-MM-DD HH:MM:SS': ")
    dt = datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S')

    print("\nConversione in fusi orari mondiali:\n")
    for tz in target_timezones:
        converted_dt = convert_timezone(dt, italian_timezone, tz)
        print(f"{tz}: {converted_dt}")

# Conversione da fuso orario mondiale a fuso orario italiano
def world_to_italian():
    italian_timezone = 'Europe/Rome'
    target_timezones = get_timezone_list()

    print("Fuso orario italiano: ", italian_timezone)
    target_timezone = input("Inserisci il fuso orario mondiale di destinazione: ")
    dt_string = input("Inserisci data e ora nel formato 'YYYY-MM-DD HH:MM:SS': ")
    dt = datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S')

    converted_dt = convert_timezone(dt, target_timezone, italian_timezone)
    print(f"\nFuso orario italiano: {converted_dt}")

# Menù principale
def main():
    print("Benvenuto nel convertitore di fusi orari!")
    print("1. Fuso orario italiano a fuso orario mondiale")
    print("2. Fuso orario mondiale a fuso orario italiano")
    choice = input("Seleziona un'opzione (1 o 2): ")

    if choice == '1':
        italian_to_world()
    elif choice == '2':
        world_to_italian()
    else:
        print("Opzione non valida.")

if __name__ == '__main__':
    main()