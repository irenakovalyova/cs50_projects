from sys import argv, exit
import csv


def str_repeats(sequence, STR):
    # Legnth of each STR
    L = len(STR)
    
    # Initialize maximum repeats of the STR
    repeats_max = 0
    for i in range(len(sequence)):
        
        # Initialise the counter for STR repeats
        repeats = 0

        if sequence[i: i + L] == STR:
            # Start counting - first match
            repeats += 1
            # Continue counting repeats
            while sequence[i: i + L] == sequence[i + L: i + (2 * L)]:
                repeats += 1
                # Incrementing i for the legnth of the STR
                i += L

        # If current number of repeats is greater than the previous one, update
        if repeats > repeats_max:
            repeats_max = repeats

    return repeats_max


def main():
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    STRs = []
    person_profiles = []

    # Read database file
    with open(argv[1], mode="r") as profile_database:
        reader = csv.DictReader(profile_database)
        # Populate list of STRs
        STRs = reader.fieldnames[1:]
        for row in reader:
            # Add person to profiles
            person_profiles.append(row)

    # Initialise dictionary for sequence file
    seq_str_count = dict.fromkeys(STRs, 0)

    # Read sequence file
    with open(argv[2], mode="r") as sequence_file:
        # Get the first line of the txt file
        sequence = sequence_file.readline()
        # Go through all STRs from the database
        for STR in STRs:
            # Update the dictionary for a sequence file with maximum repeats
            seq_str_count[STR] = str_repeats(sequence, STR)

    # Check if there is a match in the database
    for profile in person_profiles:
        match_count = 0

        for STR in STRs:
            if int(profile[STR]) != seq_str_count[STR]:
                continue
            match_count += 1

        if match_count == len(STRs):
            print(profile['name'])
            exit(0)

    print("No match")
    exit(1)


if __name__ == "__main__":
    main()
        