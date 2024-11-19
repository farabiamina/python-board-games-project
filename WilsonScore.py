import math
# from DataParse import game_rating_freq_dictionary
# from DataParse import game_with_max_ratings
# print(game_with_max_ratings)

pandemic = ('Pandemic',
 {10.0: 6500,
  9.999: 1,
  9.9978: 1,
  9.99: 3,
  9.98: 1,
  9.97: 2,
  9.95: 1,
  9.93: 1,
  9.92167: 1,
  9.92: 1,
  9.90667: 1,
  9.9: 29,
  9.86: 1,
  9.85: 5,
  9.81333: 1,
  9.8: 39,
  9.76: 1,
  9.75: 8,
  9.74: 1,
  9.73: 1,
  9.72: 2,
  9.7: 22,
  9.68: 1,
  9.65: 1,
  9.64: 1,
  9.62: 4,
  9.6: 30,
  9.55: 1,
  9.54: 2,
  9.52: 1,
  9.5: 814,
  9.45333: 1,
  9.44: 2,
  9.435: 1,
  9.4: 42,
  9.38: 1,
  9.35556: 1,
  9.35: 1,
  9.32: 1,
  9.3: 55,
  9.28: 1,
  9.26667: 1,
  9.25: 30,
  9.248: 1,
  9.24: 3,
  9.233: 1,
  9.23: 2,
  9.215: 1,
  9.2: 71,
  9.19333: 1,
  9.19: 1,
  9.18: 2,
  9.17333: 1,
  9.16: 1,
  9.151: 1,
  9.15: 2,
  9.14667: 2,
  9.13188: 1,
  9.13: 2,
  9.12: 1,
  9.11: 1,
  9.10667: 1,
  9.1: 65,
  9.08667: 1,
  9.08: 1,
  9.05937: 1,
  9.05333: 1,
  9.05: 2,
  9.04562: 1,
  9.03: 2,
  9.02: 3,
  9.011: 1,
  9.01: 2,
  9.00667: 2,
  9.004: 1,
  9.0: 14715,
  8.99: 4,
  8.987: 1,
  8.98667: 1,
  8.97: 1,
  8.96: 3,
  8.95: 3,
  8.92: 2,
  8.91: 2,
  8.9: 89,
  8.895: 1,
  8.89: 1,
  8.88667: 1,
  8.88: 1,
  8.87333: 2,
  8.87: 1,
  8.85: 3,
  8.84: 2,
  8.83: 1,
  8.81111: 1,
  8.81: 1,
  8.8: 153,
  8.78667: 1,
  8.78: 3,
  8.77: 1,
  8.76: 2,
  8.7599: 1,
  8.75: 71,
  8.74667: 2,
  8.74: 4,
  8.73333: 1,
  8.72: 2,
  8.71: 1,
  8.7: 142,
  8.68: 3,
  8.66: 2,
  8.65333: 1,
  8.65: 3,
  8.64444: 1,
  8.64: 3,
  8.62813: 1,
  8.62667: 1,
  8.625: 1,
  8.62: 2,
  8.601: 1,
  8.6: 96,
  8.59333: 1,
  8.59: 2,
  8.58: 1,
  8.57812: 1,
  8.57: 1,
  8.567: 1,
  8.56667: 1,
  8.56: 5,
  8.55562: 1,
  8.55333: 1,
  8.55: 7,
  8.54667: 1,
  8.54: 2,
  8.5375: 1,
  8.52: 10,
  8.51: 4,
  8.50667: 1,
  8.5: 3177,
  8.49333: 1,
  8.49: 1,
  8.4875: 1,
  8.48312: 1,
  8.48: 1,
  8.472: 1,
  8.47: 1,
  8.46: 4,
  8.45: 5,
  8.44687: 1,
  8.44667: 1,
  8.44: 5,
  8.43333: 2,
  8.42667: 1,
  8.42: 6,
  8.41333: 1,
  8.41: 1,
  8.4: 108,
  8.39083: 1,
  8.39: 1,
  8.38: 3,
  8.37333: 1,
  8.37: 1,
  8.365: 1,
  8.36: 3,
  8.35: 5,
  8.34: 1,
  8.33: 4,
  8.32: 4,
  8.311: 1,
  8.31: 1,
  8.3: 129,
  8.27: 1,
  8.26: 3,
  8.25333: 1,
  8.25187: 1,
  8.25: 101,
  8.246: 1,
  8.24: 5,
  8.23: 2,
  8.225: 1,
  8.22: 2,
  8.217: 1,
  8.20667: 1,
  8.2: 215,
  8.19333: 2,
  8.19: 1,
  8.18667: 1,
  8.175: 1,
  8.17: 1,
  8.16: 3,
  8.15: 8,
  8.14: 2,
  8.13333: 1,
  8.125: 1,
  8.112: 1,
  8.11: 2,
  8.1045: 1,
  8.1: 123,
  8.09: 2,
  8.075: 1,
  8.07: 2,
  8.06667: 1,
  8.06: 4,
  8.05417: 1,
  8.05333: 2,
  8.05: 5,
  8.04: 7,
  8.03: 2,
  8.02667: 1,
  8.02222: 2,
  8.0215: 1,
  8.02: 7,
  8.01333: 1,
  8.01111: 1,
  8.01: 9,
  8.009: 1,
  8.00667: 1,
  8.005: 1,
  8.003: 1,
  8.001: 1,
  8.0: 29737,
  7.9975: 1,
  7.99333: 1,
  7.99: 2,
  7.98: 2,
  7.97333: 1,
  7.97: 1,
  7.96: 8,
  7.95556: 1,
  7.95: 6,
  7.94: 2,
  7.93387: 1,
  7.93333: 1,
  7.92: 7,
  7.9181: 1,
  7.918: 1,
  7.912: 1,
  7.91: 1,
  7.90667: 1,
  7.9: 193,
  7.89: 3,
  7.881: 1,
  7.88: 1,
  7.87778: 1,
  7.875: 1,
  7.86: 1,
  7.85333: 1,
  7.85: 9,
  7.84: 2,
  7.835: 1,
  7.83: 1,
  7.82833: 1,
  7.82667: 2,
  7.82: 3,
  7.81: 2,
  7.8: 433,
  7.79: 1,
  7.789: 1,
  7.78667: 1,
  7.785: 1,
  7.78: 11,
  7.77: 2,
  7.76: 1,
  7.75: 212,
  7.74: 3,
  7.73333: 1,
  7.72222: 2,
  7.72: 3,
  7.71958: 1,
  7.71111: 1,
  7.7: 223,
  7.69522: 1,
  7.69: 2,
  7.68889: 1,
  7.68: 3,
  7.67: 1,
  7.66: 5,
  7.65556: 1,
  7.65333: 1,
  7.65: 4,
  7.643: 1,
  7.64: 4,
  7.62667: 1,
  7.62: 5,
  7.61333: 3,
  7.61: 2,
  7.6: 213,
  7.59875: 1,
  7.59: 1,
  7.58667: 2,
  7.58: 2,
  7.57: 3,
  7.568: 1,
  7.565: 1,
  7.563: 1,
  7.56: 7,
  7.55: 4,
  7.54667: 2,
  7.54: 2,
  7.536: 1,
  7.53: 2,
  7.52222: 1,
  7.52: 3,
  7.517: 1,
  7.5125: 1,
  7.51: 1,
  7.50812: 1,
  7.50667: 3,
  7.5: 5229,
  7.49333: 2,
  7.49: 2,
  7.48889: 1,
  7.48: 2,
  7.47778: 1,
  7.46667: 1,
  7.46: 4,
  7.45333: 1,
  7.45: 5,
  7.44: 4,
  7.438: 1,
  7.43333: 1,
  7.43: 2,
  7.42667: 1,
  7.42: 3,
  7.41333: 1,
  7.4: 159,
  7.39937: 1,
  7.39: 2,
  7.38: 3,
  7.37333: 2,
  7.365: 1,
  7.36: 1,
  7.35: 3,
  7.34667: 1,
  7.33333: 1,
  7.33: 1,
  7.325: 1,
  7.32: 4,
  7.31: 1,
  7.3: 222,
  7.29333: 1,
  7.29063: 1,
  7.28: 1,
  7.265: 1,
  7.26: 3,
  7.25: 125,
  7.24444: 1,
  7.24: 1,
  7.23: 1,
  7.22667: 2,
  7.223: 1,
  7.22: 4,
  7.21333: 1,
  7.21: 1,
  7.20667: 1,
  7.2: 226,
  7.16: 2,
  7.15: 5,
  7.14: 3,
  7.12667: 1,
  7.125: 2,
  7.12: 3,
  7.10667: 1,
  7.1: 131,
  7.09562: 1,
  7.09: 2,
  7.08: 3,
  7.07: 1,
  7.06667: 1,
  7.06: 1,
  7.05333: 1,
  7.05: 2,
  7.04667: 1,
  7.04: 3,
  7.03333: 1,
  7.028: 1,
  7.02: 2,
  7.01875: 1,
  7.01: 3,
  7.0: 24811,
  6.99333: 1,
  6.99: 3,
  6.98: 5,
  6.9725: 1,
  6.97: 1,
  6.96: 1,
  6.95333: 1,
  6.95: 2,
  6.94: 2,
  6.93333: 1,
  6.932: 1,
  6.92222: 1,
  6.92: 1,
  6.91111: 1,
  6.91: 1,
  6.90667: 1,
  6.903: 1,
  6.9: 112,
  6.88: 2,
  6.85333: 1,
  6.85: 3,
  6.8355: 1,
  6.83: 1,
  6.82: 2,
  6.8: 166,
  6.76: 1,
  6.75: 65,
  6.72: 1,
  6.71438: 1,
  6.7: 68,
  6.68: 1,
  6.67: 1,
  6.66667: 1,
  6.64444: 1,
  6.64: 1,
  6.635: 1,
  6.62: 1,
  6.61333: 1,
  6.61: 1,
  6.60667: 1,
  6.6: 53,
  6.58: 1,
  6.57333: 2,
  6.56667: 1,
  6.56: 4,
  6.55333: 1,
  6.55: 3,
  6.54667: 1,
  6.54: 1,
  6.53333: 1,
  6.53: 1,
  6.52: 3,
  6.50667: 1,
  6.5: 1886,
  6.49: 1,
  6.46: 4,
  6.45333: 1,
  6.45: 3,
  6.44: 1,
  6.42222: 1,
  6.42: 1,
  6.4: 45,
  6.39: 1,
  6.38: 1,
  6.33333: 1,
  6.33: 2,
  6.3: 39,
  6.28667: 1,
  6.27: 1,
  6.25: 20,
  6.22: 1,
  6.2: 36,
  6.18: 5,
  6.17778: 1,
  6.15: 1,
  6.12: 2,
  6.10667: 1,
  6.1: 22,
  6.09333: 1,
  6.085: 1,
  6.08: 2,
  6.07: 1,
  6.06667: 1,
  6.06: 3,
  6.05: 1,
  6.04: 1,
  6.03333: 1,
  6.03: 1,
  6.02667: 1,
  6.02: 2,
  6.01: 1,
  6.0075: 1,
  6.0: 10627,
  5.98: 3,
  5.9: 15,
  5.891: 1,
  5.85: 1,
  5.8: 14,
  5.75: 7,
  5.73: 1,
  5.7: 17,
  5.68: 1,
  5.66: 2,
  5.62: 1,
  5.6: 5,
  5.58: 2,
  5.56: 2,
  5.54: 1,
  5.52667: 1,
  5.5: 322,
  5.48: 1,
  5.46: 1,
  5.44: 1,
  5.4376: 1,
  5.42: 1,
  5.4: 9,
  5.34: 1,
  5.336: 1,
  5.33: 1,
  5.31: 1,
  5.3: 7,
  5.29: 1,
  5.26: 1,
  5.25: 4,
  5.2: 6,
  5.18: 1,
  5.16: 1,
  5.12: 1,
  5.1: 5,
  5.09: 1,
  5.08: 1,
  5.04: 1,
  5.0: 3490,
  4.9: 5,
  4.8: 5,
  4.75: 2,
  4.7: 1,
  4.67413: 1,
  4.6: 1,
  4.5: 79,
  4.4: 2,
  4.35: 1,
  4.3: 2,
  4.29333: 1,
  4.29: 1,
  4.25: 3,
  4.2: 4,
  4.02667: 1,
  4.0: 1277,
  3.986: 1,
  3.95: 1,
  3.9: 1,
  3.88: 2,
  3.85: 1,
  3.84: 1,
  3.76667: 1,
  3.75: 2,
  3.7: 1,
  3.55: 1,
  3.5: 30,
  3.35: 1,
  3.33: 2,
  3.3: 1,
  3.1: 3,
  3.0: 654,
  2.8: 1,
  2.76: 1,
  2.75: 1,
  2.5: 7,
  2.41: 2,
  2.2: 1,
  2.0: 269,
  1.5: 4,
  1.2: 1,
  1.1: 2,
  1.02: 1,
  1.0: 18})

def score_formula(p,n,z = 1.96):
    term1 = p + (z**2) / (2 * n)
    term2 = z * math.sqrt((p * (1 - p) + (z**2) / (4 * n)) / n)
    denominator = (1 + (z**2) / n)
    
    upper_bound = (term1 + term2) / denominator
    lower_bound = (term1 - term2) / denominator
    return (upper_bound, lower_bound)

# game_rating_freq_dictionary = game_rating_freq_dictionary[:1]
example = [('文絵のために (For Fumie)', {9.0: 1, 8.0: 1, 7.6: 1, 7.0: 9, 6.8: 1, 6.3: 1, 6.0: 7, 5.0: 6, 4.0: 2, 3.0: 2})]

def confidence_interval(games):
    results = []
    for game in games:
        # print(game) #('文絵のために (For Fumie)', {9.0: 1, 8.0: 1, 7.6: 1, 7.0: 9, 6.8: 1, 6.3: 1, 6.0: 7, 5.0: 6, 4.0: 2, 3.0: 2})
        rating_freq = game[1]
        # print(rating_freq)  {10.0: 3, 9.0: 8, 8.5: 1, 8.0: 13, 7.5: 1, 7.47: 1, 7.0: 10, 6.5: 3, 6.0: 9, 5.0: 2, 3.0: 1}
        n = sum(rating_freq.values())
        weighted_upper_score = 0
        weighted_lower_score = 0
        for k,v in rating_freq.items():
            p = v/n
            bounds = score_formula(p,n)
            weighted_upper_score += k * bounds[0]
            weighted_lower_score += k * bounds[1]
            average_score = weighted_upper_score/2 + weighted_lower_score/2
            # print(score_formula(p,n)) # (0.14533409093271313, 0.005061361365853357),...
        result = (game[0], (weighted_lower_score, weighted_upper_score, average_score))
        results.append(result)    
    return results
# print(confidence_interval([pandemic]))




