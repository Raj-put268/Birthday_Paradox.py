import random
class BirthdayParadox:
    def __init__(self, num_people, num_trials=1000):
        self.num_people = num_people
        self.num_trials = num_trials

    @property
    def num_people(self):
        return self._num_people
    
    @num_people.setter
    def num_people(self, value):
        if value < 0:
            raise ValueError("num_people must be positive integer")
        self._num_people = value
    
    @property
    def num_trials(self):
        return self._num_trials
    
    @num_trials.setter
    def num_trials(self, value):
        if value <= 0:
            raise ValueError("num_trials must be positive integer")
        self._num_trials = value
        

    def generate_birthdays(self):
        birthdays = []
        for i in range(self.num_people):
            days = random.randint(1,365)
            birthdays.append(days)
        return birthdays
        
    def has_duplicate(self, birthdays):
        size = len(birthdays)
        for i in range(size):
            for j in range(i+1, size):
                if birthdays[i] == birthdays[j]:
                    return True
        return False
    
    def calculate_probability(self):
        match_count = 0
        for i in range(self.num_trials):
            birthdays = self.generate_birthdays()
            if self.has_duplicate(birthdays):
                match_count += 1
        probability = match_count/self.num_trials
        return probability
    
    def show_probability(self):
        probability = self.calculate_probability()
        print(f"For {self.num_people} peoples → probability ≈ {probability:.3f}")
        

        

