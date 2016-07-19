class Soup1{
	private Soup1(){}
	public static Soup1 makeSoup(){
		System.out.println("you get a soup by soup1");
		return new Soup1();
	}
}

class Soup2{
	private Soup2(){}
	private static Soup2 ps1=new Soup2();
	public static Soup2 access(){
		return ps1;
	}
	public void f(){}
}

public class Lunch {
	public static void main(String[] args) {	//
		new Lunch().testStatic();
		new Lunch().testSingleton();
	}
	void testPrivate(){
		
	}
	void testStatic(){
		Soup1 soup=Soup1.makeSoup();
	}
	void testSingleton(){
		Soup2.access().f();
	}

}
