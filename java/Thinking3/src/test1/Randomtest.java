package test1;

import java.util.Random;

public class Randomtest {
	public static void main(String[] args) {
		Random rand=new Random(47);
		//����������ӣ���������̶��������
		Random rand2=new Random();
		//û����������ӣ����ÿ�������һ��
		System.out.println(rand.nextInt());
		System.out.println(rand2.nextInt());
	}
}
