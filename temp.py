import math

def calculate_cells(city_size, population_density, avg_calls_per_user, avg_call_duration, num_channels_available, max_channels_per_base_station, reuse_factor, sectoring_level):
    # Calculate the total number of users in the city
    total_users = city_size * population_density

    # Calculate the total number of calls happening simultaneously
    total_calls = total_users * avg_calls_per_user

    # Calculate the number of channels required to handle simultaneous calls
    num_channels_required = math.ceil(total_calls / avg_call_duration)

    # Calculate the number of cells required based on the given reuse factor and sectoring level
    num_cells_required = math.ceil(num_channels_required / (num_channels_available / (reuse_factor * sectoring_level)))

    return num_cells_required

# Example usage
city_size = 100  # in Km2
population_density = 500  # users per Km2
avg_calls_per_user = 2
avg_call_duration = 5  # in minutes
num_channels_available = 100
max_channels_per_base_station = 10
reuse_factor = 7

sectoring_levels = [10, 120, 180, 360]

for sectoring_level in sectoring_levels:
    num_cells = calculate_cells(city_size, population_density, avg_calls_per_user, avg_call_duration, num_channels_available, max_channels_per_base_station, reuse_factor, sectoring_level)
    print("Number of cells required for sectoring level", sectoring_level, ":", num_cells)
