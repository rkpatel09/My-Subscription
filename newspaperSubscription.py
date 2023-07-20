class Newspaper:
    def __init__(self, name, prices):
        self.name = name
        self.prices = prices
        self.sum = sum(self.prices)

    def __str__(self):
        return self.name



def find_subscriptions(weekly_budget, newspapers):
    def backtrack(index, remaining_budget, current_combination):
        if remaining_budget < 0:
            return

        if remaining_budget == 0:
            combinations.append(list(current_combination))
            return

        if index >= len(newspapers):
            return
        
        for i in range(index, len(newspapers)):
            if newspapers[i].sum <= remaining_budget and newspapers[i].name not in current_combination:
                current_combination.append(newspapers[i].name)
                backtrack(i + 1, remaining_budget - newspapers[i].sum, current_combination)
                combinations.append(list(current_combination))
                current_combination.pop()

    combinations = []
    backtrack(0, weekly_budget, [])

    return combinations


if __name__ == "__main__":

    # Define the newspapers and their prices

    toi = Newspaper("TOI", [3, 3, 3, 3, 3, 5, 6])
    hindu = Newspaper("Hindu", [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4])
    et = Newspaper("ET", [4, 4, 4, 4, 4, 4, 10])
    bm = Newspaper("BM", [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5])
    ht = Newspaper("HT", [2, 2, 2, 2, 2, 4, 4])
 
    newspapers_list = [toi, hindu, et, bm, ht]

    # Input: Weekly budget
    weekly_budget = int(input("Input Weekly Budget/Amount: "))

    # Calculate all possible subscriptions for the given budget
    combinations = find_subscriptions(weekly_budget, newspapers_list)

    # Output
    print("Possible Subscriptions:")
    
    for combination in combinations:
        if len([str(news) for news in combination])>1:
            print([str(news) for news in combination]) 