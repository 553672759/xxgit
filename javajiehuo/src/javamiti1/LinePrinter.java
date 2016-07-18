
public class LinePrinter {
	public static void main(String[] args) {
		//Note: \u000A  is Unicode representation of linefeed(LF)
		//上一行的十六进制数把上一行的注释终止掉了
		char c =0x000A;
		System.out.println(c);
	}

}
