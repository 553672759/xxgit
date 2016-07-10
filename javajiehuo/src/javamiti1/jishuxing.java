package javamiti1;

public class jishuxing{
	public static void main(String[] args) {
		System.out.println(new jishuxing().isOdd(-5));
		
	}
	
	public static boolean isOdd(int i){//如果是负奇数则会返回错误结果
		return i%2==1;
	}
	public static	boolean isOdd2(int i){//解决了负奇数的问题。
		return i%2!=0;
	}
	public static boolean isOdd3(int i){//适合临界性能环境中使用。
		return (i&1)!=0;
	}
	

}
