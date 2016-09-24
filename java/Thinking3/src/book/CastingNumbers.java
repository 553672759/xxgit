package book;
/*
 * 截取时，double,float转换为int型时会将小数部分截取，只取整数。
 */
public class CastingNumbers {
	public static void main(String[] args){
		double above=0.7,below=0.4;
		float fabove=0.7f,fbelow=0.4f;//不加F会报错，默认的0.4
		//是double类型，不能直接复制给float类型
		System.out.println("(int)above="+(int)above);
		System.out.println("(int)below="+(int)below);
		System.out.println("(int)fabove="+(int)fabove);
		System.out.println("(int)fbelow="+(int)fbelow);
	}
	
}
