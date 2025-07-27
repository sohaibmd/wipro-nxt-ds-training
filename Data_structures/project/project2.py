# Sample input
scores = [2, 3, 6, 6, 5]

unique_scores = list(set(scores))

unique_scores.sort(reverse=True)

if len(unique_scores) >= 2:
    runner_up = unique_scores[1]
    print("Runner-up score:", runner_up)
else:
    print("Not enough unique scores to determine a runner-up.")
