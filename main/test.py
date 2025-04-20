import os
import sys

print("Current dir:", os.getcwd())
print("Files in current dir:", os.listdir())
print("Checking parent:")
print(os.listdir(".."))

try:
    from login import login_page
    print("✅ Import reușit!")
except ModuleNotFoundError as e:
    print("❌ Eroare la import:", e)