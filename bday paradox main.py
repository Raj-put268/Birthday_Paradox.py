from birthday_paradox import BirthdayParadox

def main():
    bp1 = BirthdayParadox(num_people=23 , num_trials=1000)
    bp1.show_probability()

    bp2 = BirthdayParadox(num_people=60 , num_trials=1000)
    bp2.show_probability()

if __name__ == "__main__":
    main()
    
