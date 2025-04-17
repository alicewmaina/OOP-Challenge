from pet import Pet

def main():
    # Create a new pet
    my_pet = Pet("Buddy")

    # Display initial status
    my_pet.get_status()

    # Perform some actions
    print("\nBuddy is eating...")
    my_pet.eat()
    my_pet.get_status()

    print("\nBuddy is playing...")
    my_pet.play()
    my_pet.get_status()

    print("\nBuddy is sleeping...")
    my_pet.sleep()
    my_pet.get_status()

    # Teach Buddy some tricks
    print("\nTeaching Buddy a new trick: 'roll over'")
    my_pet.train("roll over")
    my_pet.get_status()

    print("\nTeaching Buddy another trick: 'play dead'")
    my_pet.train("play dead")
    my_pet.get_status()

    # Show all tricks
    print("\nShowing Buddy's tricks:")
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
