package javamiti1;

public class JoyOfHex {
	public static void main(String[] args) {
		System.out.println(Long.toHexString(0x100000000L+0xcafebabe));
		/*
		 * 这个相加，本应该是1cafebabe，
		 * 但结果打印cafebabe
		 * 
		 * 在这种混合类型的计算，作操作数是long，右操作数是int
		 * 先把int类型转换为一个数值相等的long类型，再将两个long类型相加。
		 */
		//解决办法：
		System.out.println(Long.toHexString(0x100000000L+0xcafebabeL));
	}
}
