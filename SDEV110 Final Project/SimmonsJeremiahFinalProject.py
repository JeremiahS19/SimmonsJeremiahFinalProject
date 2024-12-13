import tkinter as tk
from tkinter import PhotoImage, Label, messagebox

class WorkoutPlanApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Workout Plan with Image Viewer")

        # Load and display the image
        self.image = PhotoImage(file="Image.png")
        self.label = Label(master, image=self.image)
        self.label.pack()

        # Adding a label to prompt user selection
        prompt_label = tk.Label(master, text="Which body parts would you like to work on today?")
        prompt_label.pack()

        # Checkboxes for body parts
        self.legs_var = tk.BooleanVar()
        self.back_var = tk.BooleanVar()
        self.biceps_var = tk.BooleanVar()
        self.cardio_var = tk.BooleanVar()
        self.core_var = tk.BooleanVar()

        tk.Checkbutton(master, text="Legs", variable=self.legs_var).pack()
        tk.Checkbutton(master, text="Back", variable=self.back_var).pack()
        tk.Checkbutton(master, text="Biceps/Triceps", variable=self.biceps_var).pack()
        tk.Checkbutton(master, text="Cardio", variable=self.cardio_var).pack()
        tk.Checkbutton(master, text="Core", variable=self.core_var).pack()

        # Submit button
        submit_button = tk.Button(master, text="Submit", command=self.get_selection)
        submit_button.pack()

        # Exit button
        exit_button = tk.Button(master, text="Exit", command=master.quit)
        exit_button.pack()

    # Function to display exercises based on user selection
    def show_exercises(self, selected_parts):
        exercises = {
            'legs': ['Squats', 'Lunges', 'Leg Press', 'Single Leg Deadlift', 'Calf Raises'],
            'back': ['Deadlifts', 'Pull-ups', 'Bent-over Rows', 'Dumbbell Row', 'Dumbbell Shrugs', 'Seated Row'],
            'biceps/triceps': ['Bicep Curls', 'Tricep Dips', 'Skull Crushers', 'Dumbbell Curls', 'Barbell Curl', 'Hammer Curls'],
            'cardio': ['Running', 'Cycling', 'Jump Rope', 'Swimming', 'Stair Climbing', 'Lateral Shuffle'],
            'core': ['Planks', 'Sit-ups', 'Russian Twists', 'Crunches', 'Reverse Crunch', 'Bear Crawl', 'Flutter Kicks', 'Ab Rollout']
        }

        selected_exercises = []
        for part in selected_parts:
            selected_exercises.extend(exercises.get(part, []))

        exercise_window = tk.Toplevel(self.master)
        exercise_window.title("Today's Exercises")

        exercise_list = tk.Listbox(exercise_window)
        for exercise in selected_exercises:
            exercise_list.insert(tk.END, exercise)
        exercise_list.pack()

        back_button = tk.Button(exercise_window, text="Back", command=exercise_window.destroy)
        back_button.pack()

        exit_button = tk.Button(exercise_window, text="Exit", command=self.master.quit)
        exit_button.pack()

    # Function to get user selection
    def get_selection(self):
        selected_parts = []
        if self.legs_var.get():
            selected_parts.append('legs')
        if self.back_var.get():
            selected_parts.append('back')
        if self.biceps_var.get():
            selected_parts.append('biceps/triceps')
        if self.cardio_var.get():
            selected_parts.append('cardio')
        if self.core_var.get():
            selected_parts.append('core')

        if selected_parts:
            self.show_exercises(selected_parts)
        else:
            messagebox.showwarning("Selection Error", "Please select at least one body part.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkoutPlanApp(root)
    root.mainloop()


