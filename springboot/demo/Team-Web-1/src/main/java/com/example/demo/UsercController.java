package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.impl.UserImpl;

import model.Users;

@RestController
public class UsercController {
	
	@Autowired
	UserImpl userImpl;

	
	 @RequestMapping("/add2")
	    public Object add() {
	    	Users user=new Users();
	    	user.setName("WZP");
	    	user.setAge(24);
	    	userImpl.Add(user);
	    	//repository.save(user);
	    	return "Ok";
	    }
}
