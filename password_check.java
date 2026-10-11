import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.List;
import java.util.ArrayList;


public class password_check {
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        Pattern p = Pattern.compile("[^a-zA-Z0-9]"); //special character
        Pattern d = Pattern.compile("[0-9]"); //number
        Pattern u = Pattern.compile("[A-Z]");  //capital letter
        //defined requirements scope

        
        while (true) {
            System.out.print("Please enter a password: ");
            String password = scanner.nextLine(); 
            
            //find in input
            boolean hasSpecialChar = p.matcher(password).find(); 
            boolean hasDigit = d.matcher(password).find();
            boolean hasUpperCase = u.matcher(password).find();

            boolean hasValidLength = password.length() >= 8;

            List<String> missingReqs = new ArrayList<>(); //list for unmet requirements; added to and finally outputted

            //begin if statements - adding to missingReqs list if unmet
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
                System.out.println("Password must contain: " + String.join(", ", missingReqs)); //joins all unmet requirements.
            } 
        }
    scanner.close(); //outside of while loop
    }
}
