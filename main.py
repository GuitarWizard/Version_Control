def version_compare(version1, version2):
    """Returns a value of 1 if the first software version is latest, -1 if the second is latest, 0 if they are
    identical"""

    def splitter(sequence):
        """Takes the sequence of software version numbers, splits them by the dot notation and returns a list of
         values"""
        values = sequence.split('.')
        # print(values)
        # convert strings to ints
        # print(values)
        return values

    def validation(sequence):
        """Validates the input after splitter converts the name into a list"""
        try:
            sequence = [int(n) for n in sequence]
            return True
        except ValueError:
            print('User input error')
            return False

    def type_converter(values):
        """Converts all the values in the sequence to an int"""
        values = [int(n) for n in values]
        return values



    def full_name(values):
        """Extends any software name shorthand so that all names have five identifying numbers
        I.e. 2.0 becomes 2.0.0.0.0, or 3.0.1 becomes 3.0.1.0.0"""
        if len(values) > 5:
            pass
        while len(values) < 5:
            values.append(0)
        return values

    def hierarchy(set_one, set_two):
        """Identifies the latest software release based on the lists provided via splitter. Collects comparisons
        and compiles them into a single result"""
        result = []

        for n in range(0, len(set_one)):
            if set_one[n] > set_two[n]:
                result.append(1)
            elif set_one[n] < set_two[n]:
                result.append(-1)
            else:
                result.append(0)


        final_result = 0
        for n in range(0,5):
            if set_one[n] > set_two[n]:
                result = 1
                return result

            elif set_one[n] < set_two[n]:
                result = -1
                return result
            else:
                continue
        # print(final_result)

    # Capture the delimited values of the software identification values.
    values1 = splitter(sequence=version1)
    values2 = splitter(sequence=version2)

    # validate the input
    if (validation(sequence=values1) is True) and (validation(sequence=values2) is True):
        values1 = type_converter(values=values1)
        values2 = type_converter(values=values2)

        # create a full name set, i.e. extend from shorthand
        full_set_one = full_name(values1)
        full_set_two = full_name(values2)
        # print(full_set_one)
        # print(full_set_two)

        # identify the hierarchy
        final_output = (hierarchy(set_one=full_set_one, set_two=full_set_two))
        return final_output
