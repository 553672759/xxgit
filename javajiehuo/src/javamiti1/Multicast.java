package javamiti1;

public class Multicast {
	public static void main(String[] args) {
		System.out.println((int)(char)(byte)-1);
		/*
		 * 结果是65535
		 * 第一个转型将32位窄化到8位
		 * 第二个数值将8位拓宽到16位。
		 * 最后一个转型从16位拓宽到32位。
		 * 原因：
		 * java再存放负数的时候是以补码的形式存放，
		 * 第一次窄化的时候，留下了低8位，仍表示-1
		 * 从byte到char时，char不能表示负数，所以从byte到char的转型，
		 * 叫做拓宽并窄化原始类型的转换。
		 * byte被转换成int，而int右被转换成了char 
		 */
	}
}
