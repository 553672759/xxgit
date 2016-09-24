
public class AnimalFram {
	public static void main(String[] args) {
		final String pig="length: 10";
		final String dog="length: "+pig.length();
		
		System.out.println("Animal are equal:"+pig==dog);
		//实际是
		System.out.println(("Animal are equal:"+pig)==dog);
		System.out.println("Animal are equal:"+(pig==dog));
		//解决
		System.out.println("Animal are equal:"+pig.equals(dog));
		/*
		 * 结果
		 * false
		 * false
		 * Animal are equal:false
		 * Animal are equal:true
		 */
	}

}
