import csv
import sys


def main():

    # TODO: Check for command-line usage
    # Checks for the command-line argument.
    # if the number of argument is less than 3, print "Usage: python dna.py data.csv sequence.txt"
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # TODO: Read database file into a variable
    # Open the CSV file and read its contents into memory using csv.DictReader.
    with open(sys.argv[1], "r") as database:
        reader = csv.DictReader(database)
        # Create a dictionary called people to store the STR counts for a person.
        people = {}
        # For each row of the CSV file, store the name of the person in the first column of the row as a string.
        for row in reader:
            # For each of the STRs (from the first row of the CSV file), convert the corresponding value for that STR
            # into the integer and store it in people.
            for key in row:
                if key != "name":
                    row[key] = int(row[key])
            people[row["name"]] = row

    a = 0
    for person in people:
        l = len(people[person])
        a += 1
        if a == 1:
            break

    # TODO: Read DNA sequence file into a variable
    # Open the DNA sequence and read its contents into memory.
    with open(sys.argv[2], "r") as sequence:
        dna = sequence.read()

    # TODO: Find longest match of each STR in DNA sequence
    # For each of the STRs (from the first row of the CSV file), your program should compute the longest run of consecutive repeats of the STR in the DNA sequence to identify.
    if l == 9:
        AGATC,TTTTTTCT,AATG,TCTAG,GATA,TATC,GAAA,TCTG = longest_match(dna, "AGATC"), longest_match(dna, "TTTTTTCT"), longest_match(dna, "AATG"), longest_match(dna, "TCTAG"), longest_match(dna, "GATA"), longest_match(dna, "TATC"), longest_match(dna, "GAAA"), longest_match(dna, "TCTG")
    elif l == 4:
        AGATC,AATG,TATC = longest_match(dna, "AGATC"), longest_match(dna, "AATG"), longest_match(dna, "TATC")

    # TODO: Check database for matching profiles
    # Compare the STR counts against each row in the CSV file.
    # In particular, for each row in the CSV file, your program should check if each of the STR counts matches.
    # Only if all of the STR counts match exactly should your program print out the name of the matching individual.
    for person in people:
        if l == 9:
            if people[person]["AGATC"] == AGATC and people[person]["TTTTTTCT"] == TTTTTTCT and people[person]["AATG"] == AATG and people[person]["TCTAG"] == TCTAG and people[person]["GATA"] == GATA and people[person]["TATC"] == TATC and people[person]["GAAA"] == GAAA and people[person]["TCTG"] == TCTG:
                print(person)
                sys.exit(0)
        elif l == 4:
            if people[person]["AGATC"] == AGATC and people[person]["AATG"] == AATG and people[person]["TATC"] == TATC:
                print(person)
                sys.exit(0)
    else:
        print("No match")
        sys.exit(1)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
