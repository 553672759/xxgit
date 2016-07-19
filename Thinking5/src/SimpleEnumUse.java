
public class SimpleEnumUse {
	///:~
	public static void main(String[] args) {
		Spiciness howHot=Spiciness.MEDIUM;
		System.out.println(howHot);
		for(Spiciness s:Spiciness.values())
			System.out.println(s+",ordinal "+s.ordinal());
		/*
		 * 枚举类型编译器会自动的添加toString()方法，ordinal()方法。
		 */
	}
}
