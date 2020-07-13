import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String input = in.readLine();
		if (divide(input).equals("9|2/9/:|4/7|8|4/2/1/2/9/")) {
			System.out.println("Congratulations! Flag: rgbCTF{" + input + "}");
		} else {
			System.out.println("Incorrect, try again.");
		}
	}
	
	public static String divide(String text) {
		String ans = "";
		for (int i = 0; i < text.length(); i++) {
			ans += (char)(text.charAt(i) / 2);
			ans += text.charAt(i) % 2 == 0 ? "|" : "/";
		}
		return ans;
	}
}
