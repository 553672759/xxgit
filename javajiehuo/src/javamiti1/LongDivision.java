package javamiti1;

public class LongDivision {
	public static void main(String[] args) {
		final long MICROS_PER_DAY=24*60*60*1000*1000;
		final long MILLIS_PER_DAY=24*60*60*1000;
		System.out.println(MICROS_PER_DAY/MILLIS_PER_DAY);
		/*
		 * ԭ�����ʽ1000
		 * ʵ�����н��ʽ5
		 * Ը�����ڼ���Ĺ������Ѿ�������int������ļ��ޣ�û�г���long������ļ���
		 * ���ڼ���������int����ʽ����ģ��ڼ�����ɺ�������Ϊlong���͵ġ�
		 */
		final long MICROS_PER_DAY2=24L*60*60*1000*1000;
		final long MILLIS_PER_DAY2=24L*60*60*1000;
		System.out.println(MICROS_PER_DAY/MILLIS_PER_DAY);
		/*
		 * ����취�ǽ���һ����������Ϊlong���͵ģ������ͻ���long���ͼ��㡣
		 * �Դ����ݲ�����ʱ��������������
		 */
		
	}
}
