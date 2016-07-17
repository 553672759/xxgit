package javamiti1;

public class DosEquis {
		public static void main(String[] args) {
			char x='X';
			int i=0;
			System.out.println(true?x:0);
			System.out.println(false?i:x);
			/*
			 * 结果：
			 * 	X
			 * 88
			 * 原因：
			 * 条件表达式的核心：
			 * 1.如果第二个和第三个操作符具有相同类型，那么他就是条件表达式类型。
			 * 2.如果一个操作数的类型是T，T表示byte，short，char，而另一个操作数是一个int类型
			 * 的常量表达式，他得知可以可以用类型T，表示，那么条件表达式的类型就是T
			 * 3.否则，将对操作数类型运用二进制数字提升，而条件表达式的类型就是第二个和第三个操
			 * 作数被提升之后的类型。
			 */
		}

}
