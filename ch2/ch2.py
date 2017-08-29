
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

#print(standard_deviation([996, 868, 855, 956, 867, 933, 866, 887, 936, 901, 818, 956]))

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


# for 1.c
def histo_stats(data):
    # 10 bits == 1024
    hist = [None] * 1024 # Should be 1024 in size, for 0 to 1023 as values

    # Init to 0
    for i in range(len(hist)):
        hist[i] = 0

    for val in data:
        hist[val] += 1

    mean = 0
    for i in range(len(hist)):
        mean += i * hist[i]   # i == value, hist[i] == num occurrences of value

    mean /= len(data)

    variance = 0
    for i in range(len(hist)):
        variance += hist[i] * (i - mean)**2
    variance /= len(data) - 1
    std = variance ** .5



