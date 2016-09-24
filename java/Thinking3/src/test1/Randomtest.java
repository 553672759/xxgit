package test1;

import java.util.Random;

public class Randomtest {
	public static void main(String[] args) {
		Random rand=new Random(47);
		//有随机数种子，则会生产固定的随机数
		Random rand2=new Random();
		//没有随机数种子，则会每次输出不一样
		System.out.println(rand.nextInt());
		System.out.println(rand2.nextInt());
	}
}
