import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.*;

class Untitled {
	public static void main(String[] args) {
		Console c = System.console();
		String name = c.readLine("Name?\n");
		String formatted = name.format("Hello %s", name);
		System.out.print(formatted);
		
		
		//Calculator
		
		

	}
}