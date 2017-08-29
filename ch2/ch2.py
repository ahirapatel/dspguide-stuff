
# From table 2-1 in the book
def calc_mean(data):
    mean = 0
    for val in data:
        mean += val
    mean /= len(data)
    return mean

# From table 2-1 in the book
def standard_deviation(data):
    variance = 0
    mean = calc_mean(data)
    for val in data:
        variance += (val - mean)**2
    variance /= len(data) - 1
    std = variance ** .5
    return std


def calc_running_stats(data):
    # Three needed params for running stats
    num_processed_samples = 0
    sum_of_samples = 0
    sum_of_squares_of_samples = 0

    for i in range(len(data)):
        # Update three params
        num_processed_samples += 1
        sum_of_samples += data[i]
        sum_of_squares_of_samples += data[i] ** 2

        mean = sum_of_samples / num_processed_samples

        std = 0
        if num_processed_samples != 1:
            std = sum_of_squares_of_samples - ((sum_of_samples**2) / num_processed_samples)
            std /= num_processed_samples - 1
            std = std ** .5


# Modified to work as 1b. in non-computer exercise wants to work
def calc_running_stats_modded(data):
    # Three needed params for running stats
    num_processed_samples = 0
    sum_of_samples = 0
    sum_of_squares_of_samples = 0

    for i in range(len(data)):
        # Update three params
        num_processed_samples += 1
        sum_of_samples += data[i]
        sum_of_squares_of_samples += data[i] ** 2

    mean = sum_of_samples / num_processed_samples

    std = 0
    if num_processed_samples != 1:
        std = sum_of_squares_of_samples - ((sum_of_samples**2) / num_processed_samples)
        std /= num_processed_samples - 1
        std = std ** .5


# I think we are supposed to assume pre-binned data, atleast for 1c on non-computer?
# Let's assume data is a dict here, where mapping is k,v => sample_value, sample_occurrences
# EDIT: OH FROM TABLE-2.3 ... which is a 404
def histo_mean(data):
    #mean = 0
    #for sample_value, sample_occurrences in data.items():
    #    mean += 
