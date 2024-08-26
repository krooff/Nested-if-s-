# Task 1: Code Correction
attendees = int(input("Enter number of attendees: "))
venue = "large hall"
if attendees >= 100:
    print(venue)
else:
    print("conference room")

# Task 2: Venue Selection
# Recommend additional equipment based on the number of attendees
if attendees >= 100:
    print("Use the audio system.")
if attendees >= 50:
    print("Don't forget the projector.")

# Task 3: Catering Choices
vegetarian = input("Do you want vegetarian food? (yes/no): ")

if vegetarian == "yes":
    caterer = "Veggie Delight Caterers"
else:
    caterer = "Gourmet Meals Caterers"

print(caterer)
