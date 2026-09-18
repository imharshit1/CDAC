echo "Name of all the courses: "
courses=$(cut -d',' -f2 students.csv | sort -u) 
echo "$courses"

for course in $courses
do
count_students=$(grep -oi "$course" students.csv | wc -l)
echo "Number of students in $course = $count_students"
done

