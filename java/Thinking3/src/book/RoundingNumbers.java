package book;

public class RoundingNumbers {
	public static void main(String[] args) {
		
		double above=0.7,below=0.4;
		float fabove=0.7f,fbelow=0.4f;//不加F会报错，默认的0.4
		//是double类型，不能直接复制给float类型
		System.out.println("above="+Math.round(above));
		System.out.println("below="+Math.round(below));
		System.out.println("fabove="+Math.round(fabove));
		System.out.println("fbelow="+Math.round(fbelow));

	}

}
