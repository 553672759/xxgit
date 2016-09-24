public class LabeledFor {
	public static void main(String[] args) {
		int i = 0;
		outer: for (; true;) {
			inner: for (; i < 10; i++) {
				System.out.println("i=" + i);
				if (i == 2) {
					System.out.println("continue");
					continue;
				}
				if (i == 3) {
					System.out.println("break");
					i++;
					break;
				}
				if (i == 7) {
					System.out.println("continue outer");
					i++;
					continue outer;//结束本次 外部循环，执行下一次外部循环
				}
				if (i == 8) {
					System.out.println("break outer");
					break outer;//结束本次外部循环，循环结束 。
				}
				for (int k = 0; k < 5; k++) {
					if (k == 3) {
						System.out.println("continue inner:"+k+" "+i);
						continue inner;
					}
				}
			}
		}
	}

}
