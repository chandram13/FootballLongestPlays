# Marvish Chandra

# Football algorithm to compare longest plays
# Factors: comparison method for given player's distance to potential maximum distance
# givenDistance, totalDistance / maximum distance


# 109 yds longest play in NFL history
def comparisonMethod(givenDistance):
    # Calculate a percentage of the given longest play compared to the record
    longestPlay = (givenDistance / 336) * 100
    print(longestPlay)


comparisonMethod(118)

