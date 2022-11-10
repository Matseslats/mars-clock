# Convert julian date to MSD and MTC
# https://en.wikipedia.org/wiki/Timekeeping_on_Mars#Formulas_to_compute_MSD_and_MTC
# Leap seconds https://www.ietf.org/timezones/data/leap-seconds.list

# Some code from https://github.com/jtauber/mars-clock/blob/gh-pages/index.html
import time
import math
import sys




positions = {
    "Perseverance": 77.43,
    "InSight": 135.970,
    "Curiosity": 137.42
}
landingsol = {
    "Perseverance": 52304,
    "InSight": 51511,
    "Curiosity": 49268
}

def print_missions():
    for entry in positions:
        print("\t%s" % entry)


if len(sys.argv) != 2:
    print("Please enter the name of a mission!\nOptions:")
    print_missions()
    exit(0)

input = sys.argv[1]

unixTimestamp = int(time.time())
tai_offset = 37  # International Atomic Time, leap seconds since 1 January 2017

JDutc = unixTimestamp / 86400 + 2440587.5  # Julian date, UTC
JDtt = JDutc + (tai_offset + 32.184) / 86400  # Julian date in terrestrial time
MSD = (JDtt - 2405522.0028779) / 1.0274912517  # Mars Sol date
MTC = (MSD % 1) * 24

if input in positions:  # does the lander exist?
    # do nothing
    print("Data for %s:" % input)
else:
    print("No lander named '%s'\nLanders in database:" % input)
    print_missions()
    exit(0)


lambda_ = 360 - positions[input]
sol = math.floor(MSD - lambda_ / 360) - landingsol[input]
hours = (MTC - lambda_ * 24 / 360) % 24
minutes = hours % 1 * 60  # Get fractional part, multiply by 60 to get mins
seconds = minutes % 1 * 60  # Get fractional part, multiply by 60 to get secs
print("%s sol = %d" % (input, sol))
print("HH:MM:SS = %d:%d:%d" % (hours, minutes, seconds))
