
public class NewVarArray {
	static void printArray(Object... args){//这样写参数？就是可变参数列表？
		for(Object obj:args)
			System.out.println(obj+" ");
		System.out.println();
	}
	public static void main(String[] args) {
		printArray(new Integer(47),new Float(3.14),new Double(11.11));
		printArray(47,3.14F,11.11);
		printArray("one","two","three");
		printArray(new A(),new A(),new A());
		printArray((Object[])new Integer[]{1,2,3,4});
		printArray();
		
	}
}
class A{
	static{
		System.out.println("this is A's static block");
	}
	A(){
		System.out.println("this is A's 构造");
	}
}