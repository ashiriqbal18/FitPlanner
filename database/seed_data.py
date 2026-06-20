EXERCISES = [
    # Muscle gain - beginner
    ("Push-ups", "chest,triceps,shoulders", "chest", "bodyweight", 5, "moderate", "muscle_gain", "beginner", 7.0, 3, "12 reps", 60, "Classic upper-body strength exercise."),
    ("Bodyweight Squats", "quads,glutes,hamstrings", "quads", "bodyweight", 5, "moderate", "muscle_gain", "beginner", 6.5, 3, "15 reps", 45, "Foundation lower-body strength movement."),
    ("Walking Lunges", "quads,glutes", "quads", "bodyweight", 6, "moderate", "muscle_gain", "beginner", 7.0, 3, "12 reps each leg", 60, "Unilateral leg strength and balance."),
    ("Glute Bridge", "glutes,hamstrings", "glutes", "bodyweight", 5, "low", "muscle_gain", "beginner", 4.5, 3, "15 reps", 45, "Glute activation and posterior-chain control."),
    ("Pike Push-ups", "shoulders,triceps", "shoulders", "bodyweight", 6, "moderate", "muscle_gain", "beginner", 6.0, 3, "10 reps", 60, "Bodyweight shoulder pressing pattern."),
    ("DB Curl", "biceps", "biceps", "dumbbells", 6, "moderate", "muscle_gain", "beginner", 5.0, 3, "12 reps", 60, "Dumbbell biceps isolation."),
    ("Goblet Squat", "quads,glutes", "quads", "dumbbells", 7, "moderate", "muscle_gain", "beginner", 7.5, 3, "12 reps", 60, "Squat pattern with dumbbell resistance."),
    ("Lat Pulldown", "back,biceps", "back", "gym", 7, "moderate", "muscle_gain", "beginner", 6.5, 3, "12 reps", 75, "Machine pull for back strength."),

    # Muscle gain - intermediate
    ("Diamond Push-ups", "triceps,chest", "triceps", "bodyweight", 5, "high", "muscle_gain", "intermediate", 8.0, 3, "10 reps", 60, "Triceps-focused push-up variation."),
    ("Pull-ups", "back,biceps", "back", "pull_up_bar", 7, "high", "muscle_gain", "intermediate", 8.0, 4, "8 reps", 90, "Upper-body pulling strength."),
    ("Chin-ups", "biceps,back", "biceps", "pull_up_bar", 7, "high", "muscle_gain", "intermediate", 8.0, 4, "8 reps", 90, "Biceps-focused vertical pull."),
    ("DB Shoulder Press", "shoulders,triceps", "shoulders", "dumbbells", 7, "moderate", "muscle_gain", "intermediate", 6.0, 3, "10 reps", 75, "Overhead pressing strength."),
    ("DB Row", "back,biceps", "back", "dumbbells", 7, "moderate", "muscle_gain", "intermediate", 6.5, 3, "10 reps each side", 75, "Dumbbell rowing for back thickness."),
    ("Romanian Deadlift", "hamstrings,glutes,back", "hamstrings", "dumbbells", 8, "moderate", "muscle_gain", "intermediate", 7.5, 3, "10 reps", 75, "Hip-hinge strength for posterior chain."),
    ("Bench Press", "chest,triceps,shoulders", "chest", "gym", 8, "high", "muscle_gain", "intermediate", 7.5, 4, "8 reps", 90, "Barbell chest strength exercise."),
    ("Leg Press", "quads,glutes", "quads", "gym", 8, "high", "muscle_gain", "intermediate", 8.0, 4, "10 reps", 90, "Machine lower-body strength exercise."),

    # Muscle gain - advanced
    ("Archer Push-ups", "chest,triceps,shoulders", "chest", "bodyweight", 7, "high", "muscle_gain", "advanced", 9.0, 4, "8 reps each side", 90, "Advanced unilateral push-up variation."),
    ("Pistol Squat", "quads,glutes,core", "quads", "bodyweight", 8, "high", "muscle_gain", "advanced", 9.0, 4, "6 reps each leg", 90, "Advanced single-leg squat."),
    ("Weighted Pull-up", "back,biceps", "back", "pull_up_bar", 8, "high", "muscle_gain", "advanced", 9.5, 4, "6 reps", 120, "Heavy vertical pull for strength."),
    ("DB Bulgarian Split Squat", "quads,glutes", "quads", "dumbbells", 8, "high", "muscle_gain", "advanced", 9.0, 4, "8 reps each leg", 90, "Advanced unilateral leg strength."),
    ("Deadlift", "back,glutes,hamstrings", "back", "gym", 9, "high", "muscle_gain", "advanced", 9.5, 4, "5 reps", 120, "Compound posterior-chain strength lift."),
    ("Barbell Squat", "quads,glutes,hamstrings", "quads", "gym", 9, "high", "muscle_gain", "advanced", 9.0, 4, "6 reps", 120, "Heavy compound lower-body lift."),

    # Fat loss - beginner
    ("Marching in Place", "cardio,legs", "cardio", "bodyweight", 5, "low", "fat_loss", "beginner", 6.0, 3, "45 seconds", 30, "Low-impact cardio warm-up."),
    ("Step Jacks", "cardio,shoulders,legs", "cardio", "bodyweight", 5, "moderate", "fat_loss", "beginner", 7.0, 3, "45 seconds", 30, "Beginner-friendly jumping jack alternative."),
    ("Bodyweight Good Morning", "hamstrings,glutes", "hamstrings", "bodyweight", 5, "moderate", "fat_loss", "beginner", 5.5, 3, "15 reps", 45, "Hip-hinge conditioning drill."),
    ("Low-impact Skaters", "glutes,cardio", "glutes", "bodyweight", 6, "moderate", "fat_loss", "beginner", 7.5, 3, "40 seconds", 45, "Lateral cardio with low impact."),
    ("DB Thruster", "legs,shoulders,cardio", "full_body", "dumbbells", 7, "moderate", "fat_loss", "beginner", 8.0, 3, "10 reps", 60, "Squat-to-press conditioning movement."),
    ("Cable Row Intervals", "back,cardio", "back", "gym", 7, "moderate", "fat_loss", "beginner", 7.5, 3, "45 seconds", 60, "Machine row performed at a conditioning pace."),

    # Fat loss - intermediate
    ("Jump Squats", "quads,glutes,calves", "quads", "bodyweight", 5, "high", "fat_loss", "intermediate", 10.0, 3, "12 reps", 60, "Explosive squat for calorie burn."),
    ("Mountain Climbers", "core,cardio", "core", "bodyweight", 5, "high", "fat_loss", "intermediate", 11.0, 3, "30 seconds", 45, "Dynamic core and cardio drill."),
    ("High Knees", "cardio,legs", "cardio", "bodyweight", 5, "high", "fat_loss", "intermediate", 10.5, 4, "30 seconds", 45, "Fast-paced cardio drill."),
    ("Kettlebell-style DB Swings", "glutes,hamstrings,cardio", "glutes", "dumbbells", 6, "high", "fat_loss", "intermediate", 10.0, 4, "15 reps", 60, "Dumbbell swing for conditioning."),
    ("Renegade Row", "back,core,chest", "core", "dumbbells", 7, "high", "fat_loss", "intermediate", 9.0, 3, "8 reps each side", 75, "Core-heavy dumbbell conditioning exercise."),
    ("Assisted Pull-up Intervals", "back,biceps,cardio", "back", "pull_up_bar", 7, "moderate", "fat_loss", "intermediate", 8.5, 4, "6 reps", 75, "Pulling intervals with controlled rest."),
    ("Rowing Machine Sprint", "cardio,back,legs", "cardio", "gym", 8, "high", "fat_loss", "intermediate", 11.0, 4, "45 seconds", 75, "High-output rowing interval."),

    # Fat loss - advanced
    ("Burpees", "full_body,cardio", "full_body", "bodyweight", 8, "high", "fat_loss", "advanced", 12.0, 4, "10 reps", 90, "Full-body calorie-burning exercise."),
    ("Sprawl to Jump", "full_body,cardio", "full_body", "bodyweight", 8, "high", "fat_loss", "advanced", 12.5, 4, "8 reps", 90, "Explosive advanced conditioning drill."),
    ("Pull-up Burpee", "full_body,back,cardio", "full_body", "pull_up_bar", 9, "high", "fat_loss", "advanced", 13.0, 4, "6 reps", 120, "Burpee combined with a pull-up."),
    ("DB Snatch", "full_body,shoulders,cardio", "full_body", "dumbbells", 8, "high", "fat_loss", "advanced", 11.5, 4, "8 reps each side", 90, "Powerful single-arm conditioning lift."),
    ("Battle Rope Intervals", "shoulders,cardio", "shoulders", "gym", 8, "high", "fat_loss", "advanced", 12.0, 5, "30 seconds", 75, "High-intensity rope intervals."),
    ("Treadmill Hill Sprint", "legs,cardio", "cardio", "gym", 9, "high", "fat_loss", "advanced", 13.0, 5, "30 seconds", 90, "Advanced incline sprint workout."),

    # Endurance - beginner
    ("Plank", "core,shoulders", "core", "bodyweight", 4, "low", "endurance", "beginner", 4.0, 3, "45 seconds", 30, "Core stability hold."),
    ("Wall Sit", "quads,glutes", "quads", "bodyweight", 4, "low", "endurance", "beginner", 4.5, 3, "45 seconds", 30, "Lower-body muscular endurance hold."),
    ("Bird Dog", "core,glutes", "core", "bodyweight", 5, "low", "endurance", "beginner", 3.5, 3, "10 reps each side", 30, "Core control and stability exercise."),
    ("Dead Bug", "core", "core", "bodyweight", 5, "low", "endurance", "beginner", 3.5, 3, "10 reps each side", 30, "Beginner core endurance drill."),
    ("Farmer Carry", "grip,core,shoulders", "core", "dumbbells", 6, "moderate", "endurance", "beginner", 5.5, 3, "40 meters", 45, "Loaded carry for core endurance."),
    ("Stationary Bike Easy Ride", "legs,cardio", "cardio", "gym", 8, "low", "endurance", "beginner", 6.0, 1, "8 minutes", 30, "Low-intensity cardio endurance ride."),

    # Endurance - intermediate
    ("Side Plank", "core,obliques", "core", "bodyweight", 5, "moderate", "endurance", "intermediate", 5.0, 3, "30 seconds each side", 30, "Lateral core endurance hold."),
    ("Bear Crawl", "core,shoulders,legs", "core", "bodyweight", 6, "moderate", "endurance", "intermediate", 7.0, 3, "30 seconds", 45, "Full-body crawling endurance drill."),
    ("Tempo Push-ups", "chest,triceps,core", "chest", "bodyweight", 6, "moderate", "endurance", "intermediate", 6.5, 3, "10 slow reps", 45, "Controlled pushing endurance."),
    ("Pull-up Hang", "grip,back,shoulders", "back", "pull_up_bar", 5, "moderate", "endurance", "intermediate", 5.0, 4, "30 seconds", 45, "Grip and shoulder endurance hold."),
    ("DB Walking Carry", "core,grip,legs", "core", "dumbbells", 7, "moderate", "endurance", "intermediate", 6.5, 4, "40 meters", 45, "Weighted carry for whole-body endurance."),
    ("Elliptical Intervals", "cardio,legs", "cardio", "gym", 8, "moderate", "endurance", "intermediate", 7.5, 4, "60 seconds", 45, "Sustainable cardio intervals."),

    # Endurance - advanced
    ("Plank Shoulder Taps", "core,shoulders", "core", "bodyweight", 6, "high", "endurance", "advanced", 7.5, 4, "30 seconds", 45, "Anti-rotation core endurance exercise."),
    ("Hollow Body Hold", "core", "core", "bodyweight", 5, "high", "endurance", "advanced", 6.0, 4, "30 seconds", 45, "Advanced anterior core endurance hold."),
    ("Toes-to-Bar", "core,grip", "core", "pull_up_bar", 8, "high", "endurance", "advanced", 9.0, 4, "8 reps", 75, "Advanced hanging core endurance."),
    ("DB Complex", "full_body,cardio", "full_body", "dumbbells", 9, "high", "endurance", "advanced", 10.0, 4, "6 reps each move", 90, "Multiple dumbbell movements chained together."),
    ("Sled Push", "legs,cardio", "legs", "gym", 8, "high", "endurance", "advanced", 11.0, 5, "20 meters", 90, "High-output lower-body endurance drill."),
    ("Assault Bike Sprint", "cardio,legs,arms", "cardio", "gym", 8, "high", "endurance", "advanced", 12.0, 5, "30 seconds", 75, "Advanced total-body conditioning interval."),
]
