import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.List;
import java.util.ArrayList;


public class password_check {
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        Pattern p = Pattern.compile("[^a-zA-Z0-9]");
        Pattern d = Pattern.compile("[0-9]");
        Pattern u = Pattern.compile("[A-Z]"); 

        while (true) {
            System.out.print("Please enter a password: ");
            String password = scanner.nextLine(); 
            
            // 1. Run find() ONCE and save the boolean results
            boolean hasSpecialChar = p.matcher(password).find(); 
            boolean hasDigit = d.matcher(password).find();
            boolean hasUpperCase = u.matcher(password).find();

            boolean hasValidLength = password.length() >= 8;

            List<String> missingReqs = new ArrayList<>();

            // 2. Evaluate using the boolean variables
            if (!hasSpecialChar) {
                missingReqs.add(" at least special character");
            }  if (!hasDigit) {
                missingReqs.add(" at least one number");
            }  if (!hasUpperCase) {
                missingReqs.add(" at least one uppercase letter");
            }  if (!hasValidLength) {
                missingReqs.add(" at least 8 characters");
            }
            
            if (missingReqs.isEmpty()) {
                System.out.println("Passowrd is valid.");
                break;
            }
            else {
                System.out.println("Password must contain: " + String.join(", ", missingReqs));
            } 
        }
    scanner.close(); //outside of while loop
    }
}