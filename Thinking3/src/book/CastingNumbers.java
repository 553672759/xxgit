package book;
/*
 * ��ȡʱ��double,floatת��Ϊint��ʱ�ὫС�����ֽ�ȡ��ֻȡ������
 */
public class CastingNumbers {
	public static void main(String[] args){
		double above=0.7,below=0.4;
		float fabove=0.7f,fbelow=0.4f;//����F�ᱨ��Ĭ�ϵ�0.4
		//��double���ͣ�����ֱ�Ӹ��Ƹ�float����
		System.out.println("(int)above="+(int)above);
		System.out.println("(int)below="+(int)below);
		System.out.println("(int)fabove="+(int)fabove);
		System.out.println("(int)fbelow="+(int)fbelow);
	}
	
}
