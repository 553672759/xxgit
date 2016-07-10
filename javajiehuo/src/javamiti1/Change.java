package javamiti1;

import java.math.BigDecimal;

public class Change {
	public static void main(String[] args) {
		System.out.println(2.00-1.10);
		/*
		 * 输出0.8999999999999999
		 * 原因在于1.10并不能精确地表示程double。被表示成近似值。
		 */
		
		System.out.printf("%.2f%n",2.00-1.10);
		/*
		 * JDK5.0或更新版本可用
		 * 拙略的解决方案，并不是在底层解决了问题，仍然是二进制浮点数的double运算。
		 */
		System.out.println((200-110)+"cents");
		/*
		 * 改变单位使用整数类型解决问题。
		 */
		System.out.println((new BigDecimal("2.00")).subtract(new BigDecimal("1.10")));
		/*
		 * BigDecimal执行精确的小数运算，但一定要用BigDecimal(String)构造器，不要用BigDecimal(double)
		 * 不然会返回一个"精确"的小数.
		 * 但是，java并没有BigDecimai提供任何语言上的支持，速度可能会慢。
		 */

	}
	
}
