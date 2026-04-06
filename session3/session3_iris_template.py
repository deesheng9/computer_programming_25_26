
correct = 0      # Count of correct predictions
wrong = 0        # Count of wrong predictions
total = 0        # Total samples processed
y_pred_list = []  # List of all predictions made
threshold = 2.0
feature_name = "petal_length"
positive_label = "setosa"
negative_label = "not_setosa"
label_key = "species"


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
    if sample[feature_name] < threshold:
        y_pred = positive_label
    else:
        y_pred = negative_label

    if sample[label_key] == positive_label:
        y_true = positive_label
    else:
        y_true = negative_label

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

print(f"\nTotal Samples: {total}")
print(f"Correct Predictions: {correct}")
print(f"Wrong Predictions: {wrong}")
print(f"Accuracy: {accuracy:.2f}")
print(f"Predictions: {y_pred_list}")
