def check_age(age):
  if age < 18:
    raise ValueError("Age must be 18 or older.")
    return True  # This line will never be reached if age < 18
