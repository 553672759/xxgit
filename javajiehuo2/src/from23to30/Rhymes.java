package from23to30;
import java.util.Random;
public class Rhymes {
	private static Random rnd=new Random();
	public static void main(String[] args) {
		StringBuffer word =null;
		switch(rnd.nextInt(2)){
		case 1: word=new StringBuffer('P');
		case 2: word=new StringBuffer('G');
		default:word=new StringBuffer('M');
		}
		/*错误1：
		 * rnd.nextInt(2);表示从0到2（永远取不到2）的区间
		 * 所以有一个分支永不回执行
		 * 这种错误叫栅栏柱错误。
		 * 错误2：
		 * 没有break语句
		 * 错误3：
		 * StringBuffer用法不对。
		 * 
		 * 要熟悉AIP，掌握这些常用的用法。
		 */
		word.append('a');
		word.append('i');
		word.append('n');
		System.out.println(word);
	}

}
