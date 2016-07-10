package javamiti1;

public class LongDivision {
	public static void main(String[] args) {
		final long MICROS_PER_DAY=24*60*60*1000*1000;
		final long MILLIS_PER_DAY=24*60*60*1000;
		System.out.println(MICROS_PER_DAY/MILLIS_PER_DAY);
		/*
		 * 原本结果式1000
		 * 实际运行结果式5
		 * 愿意是在计算的过程中已经超过了int所保存的极限，没有超过long所保存的极限
		 * 但在计算中是以int的形式计算的，在计算完成后在提升为long类型的。
		 */
		final long MICROS_PER_DAY2=24L*60*60*1000*1000;
		final long MILLIS_PER_DAY2=24L*60*60*1000;
		System.out.println(MICROS_PER_DAY/MILLIS_PER_DAY);
		/*
		 * 解决办法是将第一个数字声明为long类型的，这样就会以long类型计算。
		 * 对大数据操作的时候，提防溢出！！！
		 */
		
	}
}
