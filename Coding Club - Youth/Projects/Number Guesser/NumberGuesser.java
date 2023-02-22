// Step 1
import java.util.Random;
import java.util.Scanner;

public class NumberGuesser {
    static void runGame() {
        boolean playAgain = true;

        Random rand = new Random();
        Scanner scanByte = new Scanner(System.in);
        Scanner scanString = new Scanner(System.in);

        // Step 2
        while(playAgain) {
            byte generateNumber = (byte)(rand.nextFloat() * 10);
            
            // Step 3
            System.out.println("\nGuess a number between 0 and 10 inclusive!");
            System.out.println("\nWhat is your guess?");
            byte yourGuess = scanByte.nextByte();

            // Step 4
            if(generateNumber == yourGuess) {
                System.out.println("You won! Your guess was " + yourGuess + " and so was the answer!");
            } else {
                System.out.println("You lost. Your guess was " + yourGuess + " and the number was " + generateNumber);
            }
            
            // Step 5
            System.out.println("Do you want to play again (Y or N)? ");
            String yesNo = (scanString.nextLine()).toUpperCase();
            if(yesNo.equals("N")) {
                playAgain = false;
            }
        }
        scanByte.close();
        scanString.close();
        return;
    }
    public static void main(String[] args) {
        runGame();
    }
}