
public class ABC {
	public static void main(String[] args) {
		String letters="ABC";
		char[] numbers={'1','2','3'};
		System.out.println(letters+"easy as"+numbers);//numbers代表的是数组的地址
		//解决1
		System.out.print(letters+"easy as ");
		System.out.println(numbers);
		//解决2
		System.out.println(letters+"easy as "+String.valueOf(numbers));
	}

}
