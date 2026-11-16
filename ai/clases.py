# class Dog:
#     def __init__(self, name, weight):
#         self.name = name  # self.name belongs to this specific dog
#         self.weight = weight
# # Using positional argument
# dog1 = Dog(name="Buddy", weight="24kg")

# # Using named argument (same result)
# dog2 = Dog(name="Max", weight="20kg")

# # Each dog has its own name
# print(dog1.name)  # Buddy
# print(dog2.name)  # Max
# print(dog1.weight)
# print(dog2.weight)

#Real-world example: configuration

class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000