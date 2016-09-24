import java.util.regex.Pattern;
public class Me {	
	/*
	 * 谜题20、21
	 */
	public static void main(String[] args) {
		System.out.println(Me.class.getName().replaceAll(Pattern.quote("."),"/")+".class");
	}

}
