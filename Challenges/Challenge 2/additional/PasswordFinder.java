import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class PasswordFinder {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String[] passwords = {
                "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon",
                "123123", "baseball", "abc123", "football", "monkey", "letmein", "696969", "shadow", "master", "666666",
                "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321", "pussy", "superman", "1qaz2wsx",
                "7777777", "fuckyou", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer",
                "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew", "tigger", "sunshine",
                "iloveyou", "fuckme", "2000", "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars",
                "klaster", "112233", "george", "asshole", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn",
                "555555", "11111111", "131313", "freedom", "777777", "pass", "fuck", "maggie", "159753", "aaaaaa", "ginger",
                "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "6969", "nicole", "chelsea", "biteme",
                "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix", "minecraft"
        };

        String targetHash = "1b568753dbd11c8fd64489fe8f8b71c1b07ea48e5584b4d2307f9642d1b3bbca";

        for (String password1 : passwords) {
            for (String password2 : passwords) {
                for (int i = 0; i < 100; i++) {
                    // Format the number to two digits
                    String number = String.format("%02d", i);

                    // Concatenate the two passwords with the number in between
                    String candidatePassword = password1 + number + password2;

                    // Hash the candidate password using SHA-256
                    String hash = hashSHA256(candidatePassword);

                    // Compare the hash with the target hash
                    if (hash.equals(targetHash)) {
                        System.out.println("Password found: " + candidatePassword);
                        return;
                    }
                }
            }
        }

        System.out.println("Password not found.");
    }

    // Method to hash a string using SHA-256
    private static String hashSHA256(String input) throws NoSuchAlgorithmException {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hashBytes = digest.digest(input.getBytes());

        // Convert the byte array to a hexadecimal string
        StringBuilder hexString = new StringBuilder();
        for (byte b : hashBytes) {
            String hex = Integer.toHexString(0xff & b);
            if (hex.length() == 1) hexString.append('0');
            hexString.append(hex);
        }
        return hexString.toString();
    }
}
