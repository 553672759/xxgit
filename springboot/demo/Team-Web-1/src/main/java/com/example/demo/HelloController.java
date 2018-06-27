package com.example.demo;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.dao.videoInt;

import model.Users;

/**
 * 测试控制器
 *
 * @author: @我没有三颗心脏
 * @create: 2018-05-08-下午 16:46
 */
@RestController
public class HelloController {
	
	@Autowired  
    private videoInt repository;

    @RequestMapping("/hello")
    public String hello() {
        return "Hello Spring Boot!";
    }
    
    @RequestMapping("/find")
    public Object find() {
    	List u= repository.findAll();
        //Users u =repository.findByname("xx");
    	return u;
    }
    
    @RequestMapping("/add")
    public Object add() {
    	Users user=new Users();
    	user.setName("WDC");
    	user.setAge(34);
    	
    	//repository.save(user);
    	return "Ok";
    }
    @RequestMapping("/signup")
    public Object signup() {
    	
    	
    	return "signup";
    }
}