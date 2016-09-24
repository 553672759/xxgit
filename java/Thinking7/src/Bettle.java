
class Insect{
	private int i=9;
	protected int j;
	Insect(){
		System.out.println("i="+i+",j="+j);
		j=39;
	}
	private static int x1=printInit("static Insect.x1 initialized");
	static int printInit(String s){
		System.out.println(s);
		return 47;
	}
}
public class Bettle extends Insect	{
	private int k=printInit("Beetle.k initialized");
	public Bettle(){
		System.out.println("k="+k);
		System.out.println("j="+j);
	}
	private static int x2=printInit("static Beetle.x2 initialized");
	public static void main(String[] args) {
		System.out.println("Bettle constructor");
		Bettle b=new Bettle();
	}
}
/*
 * 结果：
 * static Insect.x1 initialized//先对父类静态属性加载
 *static Beetle.x2 initialized//再加载子类静态属性
 *Bettle constructor//打印输出
 *i=9,j=0//父类构造方法
 *Beetle.k initialized//子类的属性赋值	
 *k=47
 *j=39 
 */
