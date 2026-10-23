import java.util.Scanner;

public


class StudentResult {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in );

int marks;
char grade;

System.out.print("Enter student marks: ");
marks = sc.nextInt();

// Pass / Fail
if (marks >= 40) {
System.out.println("Status: Pass");
} else {
System.out.println("Status: Fail");
}

// Grade using switch
int m = marks / 10;

switch (m) {
case 10:
    case


9: \
    grade = 'A';
break;

case
8:
grade = 'B';
break;

case
7:
grade = 'C';
break;

case
6:
grade = 'D';
break;

default:
grade = 'F';
}

System.out.println("Grade: " + grade);

// Remarks
if (grade == 'A')
System.out.println("Remark: Excellent");
else if (grade == 'B')
System.out.println("Remark: Very Good");
else if (grade == 'C')
System.out.println("Remark: Good");
else if (grade == 'D')
System.out.println("Remark: Average");
else
System.out.println("Remark: Needs Improvement");

sc.close();
}
}