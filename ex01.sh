echo "Enter the student Name:"
read student_name
echo "Enter The Age:"
read student_age
echo "Enter the marks of Subject 1:"
read sub1
echo "Enter the marks of Subject2:"
read sub2
echo "Enter the marks of subject 3:"
read sub3
total=$((sub1+sub2+sub3))
avg=$((total/3))
echo "Subject 1: $sub1"
echo "Subject 2: $sub2"
echo "subject 3: $sub3"
echo "average marks of student $student_name : $avg"

