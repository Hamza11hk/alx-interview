#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid  UTF-8 encoding.
    """
    num_b = 0

    m_1 = 1 << 7
    m_2 = 1 << 6

    for i in data:

        m_b = 1 << 7

        if num_b == 0:

            while m_b & i:
                num_b += 1
                m_b = m_b >> 1

            if num_b == 0:
                continue

            if num_b == 1 or num_b > 4:
                return False

        else:
            if not (i & m_1 and not (i & m_2)):
                    return False

        num_b -= 1

    if num_b == 0:
        return True

    return False
