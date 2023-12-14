seeds = []
# int to check which mapping we are reading
mode = 0

closest_location = -1

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

with open("day5_input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if "seeds" in line:
            # Handle the list of seeds
            seeds = [int(seed) for seed in line.split(": ")[1].split(" ")]
        elif "map" in line:
            mode += 1
        elif len(line) > 5:  # data line, not blank
            match mode:
                case 1:
                    seed_to_soil.append([int(data) for data in line.split(" ")])
                case 2:
                    soil_to_fertilizer.append([int(data) for data in line.split(" ")])
                case 3:
                    fertilizer_to_water.append([int(data) for data in line.split(" ")])
                case 4:
                    water_to_light.append([int(data) for data in line.split(" ")])
                case 5:
                    light_to_temperature.append([int(data) for data in line.split(" ")])
                case 6:
                    temperature_to_humidity.append([int(data) for data in line.split(" ")])
                case 7:
                    humidity_to_location.append([int(data) for data in line.split(" ")])

def mapping_result(value, mapping_list):
    for mapping in mapping_list:
        destination, source, range_length = mapping
        if source <= value < source + range_length:
            return destination + (value - source)
    return value
        
# Map from seed to location:
for seed in seeds:
    soil = mapping_result(seed, seed_to_soil)
    fertilizer = mapping_result(soil, soil_to_fertilizer)
    water = mapping_result(fertilizer, fertilizer_to_water)
    light = mapping_result(water, water_to_light)
    temperature = mapping_result(light, light_to_temperature)
    humidity = mapping_result(temperature, temperature_to_humidity)
    location = mapping_result(humidity, humidity_to_location)

    # print(seed, soil, fertilizer, water, light, temperature, humidity, location)

    closest_location = min(closest_location, location) if closest_location != -1 else location

print(closest_location)
