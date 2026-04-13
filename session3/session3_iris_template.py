# Session 2 continuity variables (Rule settings). Do not change these.
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"
LABEL_KEY = "species"

correct = 0      # Count of correct predictions
wrong = 0        # Count of wrong predictions
total = 0        # Total samples processed
y_pred_list = []  # List of all predictions made

flower1 = {
    "id": "flower1",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 1: Create A dictionary for second flower
flower2 = {
    "id": "flower2",
    "sepal_length": 4.9,
    "sepal_width": 3.0,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 2: Create list of dictionaries
dataset = [flower1, flower2]

# Task 3: Create a for loop to process the dataset
for sample in dataset:
    print(sample["id"], sample["petal_length"], sample["species"])

# Task 4: Use an if-else statement to classify each sample
    if sample[FEATURE_NAME] < THRESHOLD:
        y_pred = POSITIVE_LABEL
    else:
        y_pred = NEGATIVE_LABEL

    if sample[LABEL_KEY] == POSITIVE_LABEL:
        y_true = POSITIVE_LABEL
    else:
        y_true = NEGATIVE_LABEL

    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1

    total += 1
    y_pred_list.append(y_pred)
    print(
        f"id={sample['id']} | true={y_true} | pred={y_pred} | petal_length={sample['petal_length']}"
    )

# Task 5: Print final results
if total > 0:
    accuracy = (correct / total) * 100
else:
    accuracy = 0.0

print("Correct:", correct)
print("Wrong:", wrong)
print("Total:", total)
print("Accuracy (%):", accuracy)
print("All predictions:", y_pred_list)
