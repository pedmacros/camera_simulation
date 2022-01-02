import sun_pos

# When:  (2022, 7, 4, 11, 20, 0, -6)
# Where:  (40.602778, -104.741667)
# Azimuth:  121.38
# Elevation:  61.91

year = 2022
month = 7
day = 4
hour = 11
minute = 20
second = 0
timezone = -6
latitude = 40.602778
longitude = -104.741667

when = year, month, day, hour, minute, second, timezone
where = latitude, longitude

azimuth, elevation = sun_pos.sunpos(when, where,False)

print("Azimuth: ", azimuth)
print("elevation: ", elevation)