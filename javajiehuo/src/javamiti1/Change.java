package javamiti1;

import java.math.BigDecimal;

public class Change {
	public static void main(String[] args) {
		System.out.println(2.00-1.10);
		/*
		 * ���0.8999999999999999
		 * ԭ������1.10�����ܾ�ȷ�ر�ʾ��double������ʾ�ɽ���ֵ��
		 */
		
		System.out.printf("%.2f%n",2.00-1.10);
		/*
		 * JDK5.0����°汾����
		 * ׾�ԵĽ���������������ڵײ��������⣬��Ȼ�Ƕ����Ƹ�������double���㡣
		 */
		System.out.println((200-110)+"cents");
		/*
		 * �ı䵥λʹ���������ͽ�����⡣
		 */
		System.out.println((new BigDecimal("2.00")).subtract(new BigDecimal("1.10")));
		/*
		 * BigDecimalִ�о�ȷ��С�����㣬��һ��Ҫ��BigDecimal(String)����������Ҫ��BigDecimal(double)
		 * ��Ȼ�᷵��һ��"��ȷ"��С��.
		 * ���ǣ�java��û��BigDecimai�ṩ�κ������ϵ�֧�֣��ٶȿ��ܻ�����
		 */

	}
	
}
