package test1;

public class Dog {
	String name;
	String says;
	
	public static void main(String[] args) {
		Dog dog1=new Dog();
		Dog dog2=new Dog();
		dog1.name="spot";
		dog1.says="RUFF!";
		dog2.name="scruffy";
		dog2.says="Wurf!";
		Dog dog3=dog1;
		System.out.println(dog3==dog1);
		System.out.println(dog3.equals(dog1));
	}

}
