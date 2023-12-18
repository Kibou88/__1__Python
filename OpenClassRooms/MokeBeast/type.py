def beast_type(animal_type):
  match animal_type.lower():
      case "fire":
          print("\033[0;31m") # Red
      case "earth":
          print("\033[0;33m") # Brown
      case "wind":
          print("\033[0m") # Default (white)
      case "water":
          print("\033[0;36m") # Cyan
      case "lightning":
          print("\033[1;33m") # Yellow
      case _:
          print(f"The type {animal_type} doesn't exist")