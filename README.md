# 🧠 FitPlanner AI

An AI-Powered Workout Planning and Optimization System that generates personalized workout schedules based on a user's fitness goal, experience level, available equipment, workout duration, and weekly training frequency.

FitPlanner AI combines database-driven exercise management with Design and Analysis of Algorithms (DAA) concepts, specifically **Backtracking** and **Branch & Bound**, to generate optimized workout plans that maximize workout effectiveness while respecting user constraints.

---

# 📌 Project Overview

Finding an effective workout plan can be challenging because every individual has different fitness goals, available equipment, fitness levels, and time constraints.

FitPlanner AI solves this problem by:

* Collecting user preferences
* Filtering suitable exercises from a database
* Applying optimization algorithms
* Generating a personalized weekly workout schedule

The system ensures that selected exercises fit within the user's daily workout time limit while maximizing workout value.

---

# 🚀 Features

### 🎯 Personalized Workout Generation

Generate workout plans based on:

* Fitness Goal

  * Muscle Gain
  * Weight Loss
  * Endurance

* Fitness Level

  * Beginner
  * Intermediate
  * Advanced

* Available Equipment

  * Bodyweight Only
  * Dumbbells
  * Pull-up Bar
  * Full Gym Equipment

* Daily Workout Duration

* Number of Workout Days

---

### ⚡ Branch & Bound Optimization

The system uses a Branch & Bound algorithm to:

* Explore exercise combinations
* Maximize calorie expenditure
* Respect workout duration constraints
* Eliminate unnecessary search branches

This provides better performance than exhaustive search approaches.

---

### 🔄 Weekly Exercise Rotation

To avoid repetitive workout sessions:

* Previously selected exercises are tracked
* Exercises are rotated across workout days
* Repetition is minimized until the exercise pool is exhausted

---

### 💾 SQLite Database Integration

The application stores exercise information in a local SQLite database including:

* Exercise Name
* Muscle Groups
* Equipment Requirements
* Difficulty Level
* Workout Goal
* Duration
* Calories Burned
* Sets/Reps
* Description

---

### 🎨 Modern User Interface

Built using:

* HTML5
* CSS3
* Flask Templates (Jinja2)

Features:

* Responsive Design
* Glassmorphism Styling
* Interactive Dashboard
* Workout Summary Cards
* Day-wise Workout Tables

---

# 🏗️ Project Structure

```text
FitPlannerAI/
│
├── app.py
│
├── algorithms/
│   ├── backtracking.py
│   └── branch_bound.py
│
├── database/
│   ├── db.py
│   ├── seed_data.py
│   ├── init_db.py
│   ├── insert_db.py
│   ├── view_db.py
│   └── exercises.db
│
├── templates/
│   ├── index.html
│   ├── form.html
│   └── result.html
│
├── static/
│   └── style.css
```

---

# 🧮 Algorithms Used

## 1. Backtracking

Backtracking explores all valid exercise combinations recursively.

### Approach

For each exercise:

* Include the exercise
* Exclude the exercise

The algorithm explores every possible combination that satisfies the time constraint.

### Complexity

Worst Case:

```text
O(2^n)
```

where n is the number of exercises.

---

## 2. Branch & Bound

Branch & Bound improves efficiency by pruning branches that cannot outperform the current best solution.

### Objective Function

Maximize:

```text
Total Calories Burned
```

Subject to:

```text
Total Workout Time ≤ Daily Time Limit
```

### Bounding Strategy

The algorithm calculates an optimistic upper bound using remaining exercise calories.

If a branch cannot exceed the current best solution, it is discarded immediately.

### Complexity

Worst Case:

```text
O(2^n)
```

Average performance is significantly improved due to pruning.

---

# 🗄️ Database Design

## Exercise Table

| Field            | Description                |
| ---------------- | -------------------------- |
| id               | Exercise ID                |
| name             | Exercise Name              |
| muscle_groups    | Targeted Muscle Groups     |
| primary_muscle   | Main Muscle Group          |
| equipment        | Required Equipment         |
| duration_min     | Duration in Minutes        |
| intensity        | Exercise Intensity         |
| goal             | Fitness Goal               |
| level            | Fitness Level              |
| calories_per_min | Calories Burned Per Minute |
| sets             | Number of Sets             |
| reps             | Number of Repetitions      |
| rest_sec         | Rest Duration              |
| description      | Exercise Description       |

---

# 🔄 Workflow

```text
User Input
      ↓
Filter Exercises
      ↓
Branch & Bound Optimization
      ↓
Generate Daily Plan
      ↓
Weekly Rotation Logic
      ↓
Display Personalized Workout Plan
```

---

# 🛠️ Technologies Used

### Backend

* Python
* Flask

### Database

* SQLite

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Algorithms

* Backtracking
* Branch & Bound

---

# 🎓 Academic Relevance

This project was developed as a Design and Analysis of Algorithms (DAA) project to demonstrate:

* Recursive Backtracking
* Branch & Bound Optimization
* Search Space Pruning
* Constraint Satisfaction
* Time Complexity Analysis
* Database-Driven Decision Making

---

# 🔮 Future Enhancements

* User Authentication
* Workout History Tracking
* PDF Workout Export
* Progress Analytics Dashboard
* AI-Based Exercise Recommendations
* Machine Learning-Based Personalization
* Nutrition Planning Module
* Exercise Demonstration Videos

---

# 👨‍💻 Author

**Muhammad Ashir Iqbal**

FitPlanner — AI-Powered Workout Optimization System
