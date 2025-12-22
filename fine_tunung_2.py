from transformers import T5ForConditionalGeneration, T5Tokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Ładujemy model T5 i tokenizer
model_name = "t5-small"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Ładujemy zbiór danych do podsumowywania (na przykład CNN/DailyMail)
dataset = load_dataset("cnn_dailymail", "3.0.0", split="train[:1%]")  # mały podzbiór danych

# Funkcja do tokenizacji i przygotowania danych
def preprocess_function(examples):
    inputs = ["summarize: " + doc for doc in examples["article"]]
    model_inputs = tokenizer(inputs, max_length=512, truncation=True)

    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["highlights"], max_length=128, truncation=True)

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Przetwarzamy dane
tokenized_datasets = dataset.map(preprocess_function, batched=True)

# Ustawiamy parametry treningu
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=2,
    num_train_epochs=1,
)

# Tworzymy trenera i trenujemy model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
)

trainer.train()

# Zapisujemy dostrojony model
model.save_pretrained("./t5-summarization-model")
