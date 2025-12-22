from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Ładujemy bazowy model i tokenizer
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Przygotowujemy dane treningowe, na przykład jakiś zbiór tekstów
dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="train[:1%]")  # bierzemy na przykład 1% danych dla przykładu

# Tokenizujemy dane
def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length")

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Ustawiamy argumenty treningu
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=2,
    num_train_epochs=1,  # dla przykładu tylko 1 epoka
)

# Tworzymy trener i trenujemy model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
)

trainer.train()

# Zapisujemy dostrojony model
model.save_pretrained("./fine-tuned-model")