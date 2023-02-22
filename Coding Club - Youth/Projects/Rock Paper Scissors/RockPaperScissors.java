// Step 1
import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {
    static void runGame() {
        boolean playAgain = true;
        byte playerScore = 0, computerScore = 0,
                playerSymbol = -1,
                computerSymbol = -1;

        Random rand = new Random();
        Scanner scanString = new Scanner(System.in);
        
        // Step 2
        while(playAgain) {
            System.out.println("\nWhat is your move (R, P, S)? ");
            String playerMove = (scanString.nextLine()).toUpperCase();

            // Step 3
            if(playerMove.equals("R")) {
                playerMove = "rock";
                playerSymbol = 0;
            } else if(playerMove.equals("P")) {
                playerMove = "paper";
                playerSymbol = 1;
            } else if(playerMove.equals("S")) {
                playerMove = "scissors";
                playerSymbol = 2;
            } else {
                playerMove = "invalid";
                playerSymbol = -1;
            }

            // Step 4
            computerSymbol = (byte)(Math.floor(rand.nextFloat() * 3)); // between 0 and 2 inclusive
            String computerMove = "";

            if(computerSymbol == 0) {
                computerMove = "rock";
            } else if(computerSymbol == 1) {
                computerMove = "paper";
            } else if(computerSymbol == 2) {
                computerMove = "scissors";
            } else {
                computerMove = "unknown";
            }

            // Step 5
            if (playerSymbol > computerSymbol) {
                if (computerSymbol == 0 && playerSymbol == 2) {
                    playerScore += 1;
                } else {
                    computerScore += 1;
                }
            } else if (computerSymbol > playerSymbol) {
                if (playerSymbol == 0 && computerSymbol == 2) {
                    playerScore += 1;
                } else {
                    computerScore += 1;
                }
            } else {
                System.out.println("It was a tie!");
            }

            // Step 6
            System.out.println("The player's move was " + playerMove + " and the computer's move was " + computerMove);
            System.out.println("The player's score is " + playerScore);
            System.out.println("The computer's score is " + computerScore);

            // Step 7
            System.out.println("Do you want to play again (Y or N)? ");
            String yesNo = (scanString.nextLine()).toUpperCase();
            if(yesNo.equals("N")) {
                playAgain = false;
            }

        }
        scanString.close();
        return;
    }
    public static void main(String[] args) {
        runGame();
    }
}
