import ratemyprofessor

UCI_RMP_OBJ = ratemyprofessor.get_school_by_name("UC Irvine")

class UCI_Prof:
    def __init__(self, name: str):
        self._professor = ratemyprofessor.get_professor_by_school_and_name(UCI_RMP_OBJ, name)
    
    def get_avg_difficulty(self):
        return self._professor.difficulty
    
    def get_retake_percentage(self):
        return self._professor.would_take_again
    

# Basic testing
if __name__ == '__main__':
    shindler = UCI_Prof("Michael Shindler")
    print("Avg difficulty: ", shindler.get_avg_difficulty())
    print("Retake rate: ", shindler.get_retake_percentage(), "%")