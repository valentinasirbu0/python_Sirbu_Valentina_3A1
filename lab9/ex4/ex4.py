from secure_password_generator import password_generator


length = 16
include_special_chars = True
include_numbers = True
include_uppercase = True

generated_password = password_generator.generate_password(
    length=length,
    include_special_chars=include_special_chars,
    include_numbers=include_numbers,
    include_uppercase=include_uppercase
)

print(f"Generated Password: {generated_password}")