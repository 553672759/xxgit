package model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;




@Document(collection="Users")
public class Users {

   

    //id属性是给mongodb用的，用@Id注解修饰

    @Id
    private String id;

   
    @Field("name")
    private String name;

   

    private int age;

   

 

    public String getName() {

       return name;

    }

 

    public void setName(String name) {

       this.name = name;

    }

 

    public int getAge() {

       return age;

    }

 

    public void setAge(int age) {

       this.age = age;

    }

 

    @Override
    public String toString() {

       return "DemoInfo [id=" + id + ", name=" + name + ", age=" + age + "]";

    }

}