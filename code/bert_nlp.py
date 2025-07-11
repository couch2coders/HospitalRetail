from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
labels = ["Beverage", "Dessert", "Sandwich", "Breakfast", "Salad"]
result = classifier("egg and cheese bagel", labels)
print(result)