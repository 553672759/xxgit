		
public class WhileTest {
	static boolean condition(){
		boolean result=Math.random()<0.99;
		System.out.println(result+",");
		return result;
	}
	public static void main(String[] args) {
		while(condition()){//数字不可以直接当作boolean类型，编译会报。
			System.out.println("Inside 'while'");
			System.out.println("Exited 'while'");
		}
		
	}
}
