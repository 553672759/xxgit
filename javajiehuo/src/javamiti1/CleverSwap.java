package javamiti1;

public class CleverSwap {
	public static void main(String[] args) {
		int x=1984;
		int y=2001;
		x^=y^=x^=y;
		System.out.println("x="+x+";y="+y);
		/*
		 * 曾经，异或^可以避免临时变量，但不一定都执行。
		 * 不要再单个表达式中对相同的变量复制两次。
		 */
	}
}
