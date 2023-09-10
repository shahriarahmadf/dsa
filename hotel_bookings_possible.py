class Solution:
    # @param arrive: list of integers
    # @param depart: list of integers
    # @param K: integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        # Sort the arrive and depart date lists
        arrive.sort()
        depart.sort()

        # Declare pointers to loop through date lists: i for arrive and j for depart
        i = 0
        j = 0

        # How many people are staying right now in the hotel
        booking = 0

        while True:
            # If booking number is more than capacity/room, return FALSE
            if booking > K:
                return False

            # If looping through both arrive and depart is finished, BREAK
            if i >= len(arrive) and j >= len(depart):
                break

            # If looping through arrive is finished, we only consider depart
            if i >= len(arrive):
                j += 1  # Take depart list pointer to the next
                booking -= 1  # Decrease booking
                continue

            # Opposite case as the above one
            if j >= len(depart):
                i += 1
                booking -= 1
                continue

            # If current pointed arrive date is earlier than depart date, we consider that date
            if arrive[i] < depart[j]:
                i += 1  # Increase pointer of arrive list by 1
                booking += 1  # Increase booking
                continue

            # Opposite of the above case
            if arrive[i] > depart[j]:
                j += 1
                booking -= 1
                continue

            # In case both dates in arrive and depart are the same, we consider both of them
            if arrive[i] == depart[j]:
                # However for that particular day, both persons who are arriving
                # and the other person is about to leave both are staying in the hotel.
                # So check this condition
                if (booking + 1) > K:
                    return False
                # Increase pointers of both arrive and depart
                i += 1
                j += 1
                continue

        return True
