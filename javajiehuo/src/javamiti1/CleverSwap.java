package javamiti1;

public class CleverSwap {
	public static void main(String[] args) {
		int x=1984;
		int y=2001;
		x^=y^=x^=y;
		System.out.println("x="+x+";y="+y);
		/*
		 * ���������^���Ա�����ʱ����������һ����ִ�С�
		 * ��Ҫ�ٵ������ʽ�ж���ͬ�ı����������Ρ�
		 */
	}
}
