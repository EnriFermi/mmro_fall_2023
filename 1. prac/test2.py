def find_max_substring_occurrence(input_string):
    for k in range(1, len(input_string) + 1):
        div = len(input_string) // k
        if len(input_string) % k == 0 and \
                input_string[:k] * div == input_string:
            return div
